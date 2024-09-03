import cv2
import os


def video_to_frames(video_path, output_folder, interval_seconds):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval_frames = int(fps * interval_seconds)

    count = 0
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_number % interval_frames == 0:
            frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            count += 1

        frame_number += 1

    cap.release()
    print(
        f"Extracted {count} frames every {interval_seconds} seconds to {output_folder}"
    )
