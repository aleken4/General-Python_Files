import cv2
import threading

class CameraManager:
    def __init__(self, camera_indices):
        self.cameras = camera_indices
        self.caps = {}
        self.running = False
        self.callbacks = []

    def start(self):
        self.running = True
        for cam_index in self.cameras:
            cap = cv2.VideoCapture(cam_index)
            self.caps[cam_index] = cap
            threading.Thread(target=self.camera_loop, args=(cam_index,), daemon=True).start()

    def stop(self):
        self.running = False
        for cap in self.caps.values():
            cap.release()

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def camera_loop(self, cam_index):
        cap = self.caps[cam_index]
        while self.running:
            ret, frame = cap.read()
            if ret:
                for cb in self.callbacks:
                    cb(frame, cam_index)
