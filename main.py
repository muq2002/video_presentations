import cv2
import os

def video_to_frames(video_path, output_folder, interval_seconds):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (FPS) of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval_frames = int(fps * interval_seconds)

    # Frame count
    count = 0
    frame_number = 0

    while True:
        # Read the next frame
        ret, frame = cap.read()

        # If the frame was not retrieved, break the loop
        if not ret:
            break

        # Save the frame at the specified intervals
        if frame_number % interval_frames == 0:
            frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            count += 1

        frame_number += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {count} frames every {interval_seconds} seconds to {output_folder}")

if __name__ == "__main__":
    video_folder = "videos"
    video_filename = "1.mp4"  # Replace with your video file name
    video_path = os.path.join(video_folder, video_filename)
    
    output_folder = os.path.join(video_folder, "images")

    interval_seconds = 5  # Replace with the desired interval in seconds

    video_to_frames(video_path, output_folder, interval_seconds)
