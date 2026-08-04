import cv2
import face_recognition
import os
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import pyaudio
import csv

# -------------------------
# AUDIO SETUP
# -------------------------
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD = 600

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# -------------------------
# LOAD FACES
# -------------------------
known_encodings = []
known_names = []

def load_faces():
    global known_encodings, known_names

    known_encodings = []
    known_names = []

    if not os.path.exists("known_faces"):
        os.makedirs("known_faces")

    for file in os.listdir("known_faces"):
        if file.endswith(".jpg") or file.endswith(".png"):
            image = face_recognition.load_image_file("known_faces/" + file)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(file)[0])

load_faces()

# -------------------------
# GLOBALS
# -------------------------
video = cv2.VideoCapture(0)
running = False
current_frame = None
last_logged = {}
LOG_DELAY = 3

# CSV log setup
log_file = open("log.csv", "a", newline="")
csv_writer = csv.writer(log_file)

# Write header if empty
if os.stat("log.csv").st_size == 0:
    csv_writer.writerow(["Time", "Name", "Event"])

# -------------------------
# CAMERA LOOP
# -------------------------
def update_frame():
    global current_frame

    if not running:
        return

    ret, frame = video.read()
    if not ret:
        return

    current_frame = frame.copy()
    rgb = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    detected_names = []

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        detected_names.append(name)

        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # -------------------------
    # AUDIO DETECTION
    # -------------------------
    data = stream.read(CHUNK, exception_on_overflow=False)
    audio_data = np.frombuffer(data, dtype=np.int16)
    volume = np.linalg.norm(audio_data)

    speaking = volume > THRESHOLD

    current_time = datetime.now()
    display_text = "Silent"

    if speaking and len(detected_names) > 0:
        speaker = detected_names[0]
        display_text = "Speaking: " + speaker

        last_time = last_logged.get(speaker)

        if last_time is None or (current_time - last_time).seconds > LOG_DELAY:
            csv_writer.writerow([current_time.strftime("%H:%M:%S"), speaker, "Speaking"])
            log_file.flush()
            last_logged[speaker] = current_time

    status_label.config(text=display_text)

    # Convert to Tk image
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    root.after(10, update_frame)

# -------------------------
# BUTTON FUNCTIONS
# -------------------------
def start_camera():
    global running
    if not running:
        running = True
        update_frame()

def stop_camera():
    global running
    running = False

def add_face():
    global current_frame

    if current_frame is None:
        status_label.config(text="No frame")
        return

    name = name_var.get()

    if name == "":
        status_label.config(text="Enter name")
        return

    rgb = current_frame[:, :, ::-1]
    faces = face_recognition.face_locations(rgb)

    if len(faces) == 0:
        status_label.config(text="No face")
        return

    top, right, bottom, left = faces[0]
    face_img = current_frame[top:bottom, left:right]

    filename = "known_faces/" + name + ".jpg"
    cv2.imwrite(filename, face_img)

    load_faces()
    update_dropdown()

    status_label.config(text="Saved: " + name)

def update_dropdown():
    menu = dropdown["menu"]
    menu.delete(0, "end")

    for name in known_names:
        menu.add_command(label=name, command=lambda value=name: name_var.set(value))

# -------------------------
# GUI
# -------------------------
root = tk.Tk()
root.title("Final Face + Voice Tracker")
root.geometry("700x600")

video_label = tk.Label(root)
video_label.pack()

controls = tk.Frame(root)
controls.pack(pady=10)

tk.Button(controls, text="Start", command=start_camera, width=15).grid(row=0, column=0, padx=5)
tk.Button(controls, text="Stop", command=stop_camera, width=15).grid(row=0, column=1, padx=5)

name_var = tk.StringVar()

tk.Entry(controls, textvariable=name_var, width=20).grid(row=1, column=0)
tk.Button(controls, text="Add Face", command=add_face, width=15).grid(row=1, column=1)

dropdown = tk.OptionMenu(controls, name_var, "")
dropdown.grid(row=2, column=0, columnspan=2)

update_dropdown()

status_label = tk.Label(root, text="Idle", font=("Arial", 14))
status_label.pack(pady=10)

# -------------------------
# CLEANUP
# -------------------------
def on_close():
    global running
    running = False
    video.release()
    stream.stop_stream()
    stream.close()
    audio.terminate()
    log_file.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
