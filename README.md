# Twitter Video Downloader

A simple Python tool to download videos from Twitter/X.

## Features

- Download videos from Twitter/X URLs
- Supports both twitter.com and x.com URLs
- Customizable output directory
- Command-line interface for easy use

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/twitter-video-downloader.git
   cd twitter-video-downloader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python twitter_downloader.py "https://twitter.com/username/status/123456789"
```

### Specify Output Directory

```bash
python twitter_downloader.py "https://twitter.com/username/status/123456789" -o downloads
```

### Using as a Module in Your Own Code

```python
from twitter_downloader import download_twitter_video

# Download a video
download_twitter_video("https://twitter.com/username/status/123456789", "downloads")
```

## How It Works

This tool uses the `yt-dlp` library (a fork of youtube-dl) to handle the video downloading process. It:

1. Accepts a Twitter/X URL
2. Converts x.com URLs to twitter.com format if needed
3. Sets up the output directory
4. Configures download options
5. Downloads the video using the best available quality

## Troubleshooting

- **Authentication Issues**: Some tweets may require authentication. You can uncomment and use the `cookiefile` option in the script.
- **URL Format**: Make sure you're using the direct URL to the tweet containing the video.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
