# Video to PDF Converter

## Overview
This tool extracts frames from a video (local file or YouTube URL), removes similar images, and converts the remaining frames into a PDF. It is useful for converting lecture recordings, presentations, or instructional videos into a document format.

## Features
- **Extract Frames from Video**: Capture frames at a defined interval.
- **Remove Similar Images**: Filters out duplicate or nearly identical frames using an adjustable similarity threshold.
- **Convert to PDF**: Generates a PDF from the extracted frames.
- **YouTube Video Download**: Automatically downloads YouTube videos for processing.
- **Customizable Output**: Allows specifying an output folder and frame extraction interval.

## Future Enhancements 🚀
- **Optical Character Recognition (OCR)**: Extract text from slides and make the PDF searchable.
- **Editable PowerPoint Output**: Convert extracted frames into editable PowerPoint slides.
- **Graphical User Interface (GUI)**: Web-based interface for ease of use.
- **Auto Slide Detection**: Automatically detect and remove non-slide frames.

## Installation

Ensure you have Python installed, then install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
Run the script with the following options:
```sh
python main.py -v /path/to/video.mp4 -o output_folder -i 5 -r -p
```

To process a YouTube video:
```sh
python main.py -v "https://www.youtube.com/watch?v=example" -d ./downloads -o output_folder -i 5 -r -p
```

### Arguments
| Argument | Description |
|----------|-------------|
| `-v`, `--video` | Path to a local video file or YouTube URL (Required) |
| `-o`, `--output` | Output folder for extracted images (Default: `images/`) |
| `-i`, `--interval` | Interval in seconds between frames (Default: `5`) |
| `-r`, `--remove_similar` | Remove duplicate images after extraction |
| `-p`, `--pdf` | Convert extracted images to PDF |
| `-d`, `--download_path` | Path to save downloaded YouTube videos (Default: `./downloads/`) |
| `-t`, `--threshold` | Similarity threshold for image comparison (Default: `0.9`) |

## Example
Extract frames every 5 seconds, remove similar images, and generate a PDF from a local video:
```sh
python main.py -v slides.mp4 -i 5 -r -p
```

Process a YouTube video, save it locally, extract frames, and generate a PDF:
```sh
python main.py -v "https://www.youtube.com/watch?v=example" -d ./downloads -o output_folder -i 5 -r -p
```

## Contributing
Feel free to contribute by adding new features or improving the existing functionality! 🚀

