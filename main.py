

if __name__ == "__main__":
    video_folder = "videos"
    video_filename = "1.mp4"  # Replace with your video file name
    video_path = os.path.join(video_folder, video_filename)

    output_folder = os.path.join(video_folder, "images")

    interval_seconds = 5  # Replace with the desired interval in seconds

    video_to_frames(video_path, output_folder, interval_seconds)
