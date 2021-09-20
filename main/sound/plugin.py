"""
A plugin that converts text to speech and plays the resulting sound.

Requires:
- requests
- python-vlc
"""

import tempfile

import requests
import vlc


def main(text):
    player = vlc.MediaPlayer(download(convert(text)))
    player.play()


def convert(text, language="en-US", voice="en-US-Standard-B"):
    base_url = "https://freetts.com/Home/PlayAudio"
    response = requests.get(f"{base_url}?Language={language}&Voice={voice}&TextMessage={text}&type=0")
    if response.ok:
        filename = response.json().get("id")
        return f"https://freetts.com/audio/{filename}"


def download(url):
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as file:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    return file.name
