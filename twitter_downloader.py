import os
import sys
import argparse
from yt_dlp import YoutubeDL

def download_twitter_video(url, output_path=None):
    """
    Download a video from a Twitter/X URL
    
    Args:
        url (str): The Twitter/X video URL
        output_path (str, optional): Directory to save the video. Defaults to current directory.
    
    Returns:
        bool: True if download was successful, False otherwise
    """
    # Convert x.com URLs to twitter.com format
    if 'x.com' in url:
        url = url.replace('x.com', 'twitter.com')
    
    # Set output directory
    if output_path:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_template = os.path.join(output_path, '%(title)s.%(ext)s')
    else:
        output_template = '%(title)s.%(ext)s'
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Choose the best quality
        'outtmpl': output_template,
        'quiet': False,
        'no_warnings': False,
        # Add cookies for authentication if needed
        # 'cookiefile': 'cookies.txt',
    }
    
    try:
        # Create yt-dlp object and download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded video from {url}")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Download Twitter/X videos')
    parser.add_argument('url', help='Twitter/X video URL')
    parser.add_argument('-o', '--output', help='Output directory for downloaded video')
    
    args = parser.parse_args()
    
    # Call the download function
    download_twitter_video(args.url, args.output)

if __name__ == "__main__":
    main()
