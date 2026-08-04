import cv2
import face_recognition
import numpy as np

# Placeholder user database
# In real app, load embeddings from file/database
user_db = {
    "Alice": np.random.rand(128),
    "Bob": np.random.rand(128)
}

def detect_faces(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    return face_locations, face_encodings

def match_face(face_encoding):
    for user, embedding in user_db.items():
        dist = np.linalg.norm(face_encoding - embedding)
        if dist < 0.6:  # threshold
            return user, 1 - dist
    return "Unknown", 0
