import os
import random
import time
from moviepy.editor import *
from instagrapi import Client
import moviepy.config as mpy_config

# Set the path for ImageMagick
mpy_config.IMAGEMAGICK_BINARY = r"/usr/bin/convert"  # Adjust if using a different path for convert on Linux

# Create Shayari video with random background
def create_shayari_video(shayari_lines, output_path):
    # Parameters
    video_duration = 06  # in seconds 

    # Combine all Shayari lines into one string
    shayari_text = "\n".join(shayari_lines)

    # List of background images to randomly select from
    background_images = [
        "images/yousef-alfuhigi-yuuAGGXfe54-unsplash.jpg",  # Relative path to images in your project folder
        "images/nathan-dumlao-ciO5L8pin8A-unsplash.jpg",
        "images/henry-be-TCsCykbwSJw-unsplash.jpg"
        "images/Untitled design (1).jpg"
        "images/charlesdeluvio-pcZvxrAyYoQ-unsplash.jpg"
        "images/daoud-abismail-WU6rVJkXck8-unsplash.jpg"
    ]
    
    # Select a random background image
    background_image = random.choice(background_images)

    # Load the selected background image
    bg_clip = ImageClip(background_image, duration=video_duration)

    # Apply a zoom-in effect to the background
    bg_clip = bg_clip.fl_time(lambda t: 1 + t / video_duration, apply_to=["mask", "image"])

    # Create a single text clip
    text_clip = (
        TextClip(shayari_text, fontsize=40, color="white", font="Arial-Bold", method="caption", size=bg_clip.size)
        .set_position("center")
        .set_duration(video_duration)
    )

    # Composite the background and text clip
    final_video = CompositeVideoClip([bg_clip, text_clip])

    # Save the video to the insta_shayari folder
    output_folder = "insta_shayari"
    os.makedirs(output_folder, exist_ok=True)
    video_path = os.path.join(output_folder, "shayari_video.mp4")
    
    final_video.write_videofile(video_path, fps=24, codec="libx264", audio=False)

    return video_path

# Upload video to Instagram
def upload_to_instagram(video_path):
    # Login to Instagram using instagrapi
    client = Client()
    client.login("your_username", "your_password")  # Replace with your Instagram credentials

    # Choose a random audio from a predefined list
    audio_files = [
        "audio/audio1.mp3",  # Relative path to audio in your project folder
        "audio/audio2.mp3",
        "audio/audio3.mp3"
    ]
    selected_audio = random.choice(audio_files)

    # Load the selected audio
    audio_clip = AudioFileClip(selected_audio)

    # Load the video created earlier
    video_clip = VideoFileClip(video_path)

    # Set the audio for the video
    video_with_audio = video_clip.set_audio(audio_clip)

    # Save the video with the audio
    video_with_audio_path = video_path.replace(".mp4", "_with_audio.mp4")
    video_with_audio.write_videofile(video_with_audio_path, codec="libx264", audio_codec="aac")

    # Upload the video with audio to Instagram
    client.video_upload(video_with_audio_path, caption="Shayari for you!")

# Bot that generates and uploads videos every 8 hours
def run_bot():
    # Example Shayari list
    shayari = [
        "Zindagi ek kitab hai,", 
        "Har pal ek nayi baat hai.",
        "Samjho toh har pal mein hai khushi,", 
        "Na samjho toh yeh sirf ek raat hai."
    ]
    
    while True:
        # Create the shayari video with random background
        video_path = create_shayari_video(shayari, "insta_shayari/shayari_video.mp4")

        # Upload the video to Instagram
        upload_to_instagram(video_path)

        # Wait for 8 hours (28800 seconds) before uploading the next video
        print("Waiting for the next video upload in 8 hours...")
        time.sleep(28800)  # 8 hours in seconds

# Start the bot
run_bot()
