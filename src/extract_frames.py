import cv2
import os

def extract_frames(video_path, output_dir, fps_skip=5):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_id = 0
    saved_id = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % fps_skip == 0:
            frame_path = os.path.join(output_dir, f"frame_{saved_id:05d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_id += 1

        frame_id += 1

    cap.release()
    print(f"[INFO] {saved_id} frames extracted in {output_dir}")