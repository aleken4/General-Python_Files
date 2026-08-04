import tkinter as tk
from tkinter import Button, Label
import cv2
from PIL import Image, ImageTk
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Face + Speaker Recognition Logger")
        self.root.geometry("800x600")

        self.running = False
        self.cap = None

        # Load face detector
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # UI Elements
        self.video_label = Label(root)
        self.video_label.pack()

        self.status_label = Label(root, text="Status: Idle")
        self.status_label.pack(pady=10)

        self.start_btn = Button(root, text="Start Camera", command=self.start)
        self.start_btn.pack(pady=5)

        self.stop_btn = Button(root, text="Stop", command=self.stop)
        self.stop_btn.pack(pady=5)

    def start(self):
        if not self.running:
            self.running = True
            self.cap = cv2.VideoCapture(0)
            threading.Thread(target=self.update_frame, daemon=True).start()
            self.status_label.config(text="Status: Running")

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.status_label.config(text="Status: Stopped")

    def update_frame(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Convert to Tkinter image
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.cap.release()


# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
