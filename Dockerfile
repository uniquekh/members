# Use the official Python 3.10 image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies including ImageMagick and other required libraries
RUN apt-get update && \
    apt-get install -y \
    imagemagick \
    libimage-exiftool-perl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot when the container starts
CMD ["python", "shayari_bot.py"]
