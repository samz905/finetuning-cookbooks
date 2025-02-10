import yt_dlp
from deepgram import Deepgram
import asyncio
import os
from pathlib import Path

async def create_transcript(video_url: str) -> str:
    """
    Downloads a YouTube video as MP3 and creates its transcript.
    
    Args:
        video_url (str): YouTube video URL
    
    Returns:
        str: Path to the generated transcript file
    """
    # Create output directories if they don't exist
    Path("outputs").mkdir(exist_ok=True)
    Path("transcripts").mkdir(exist_ok=True)

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': './outputs/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'no_warnings': True,
        'cookiesfrombrowser': ('chrome',),
    }

    # Download audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        audio_file = ydl.prepare_filename(info).replace('.webm', '.mp3')

    # Initialize Deepgram
    deepgram = Deepgram(os.getenv("DEEPGRAM_API_KEY"))
    
    # Generate transcript
    with open(audio_file, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = await deepgram.transcription.prerecorded(
            source, 
            {'punctuate': True, 'tier': 'enhanced'}
        )
        
        # Extract just the transcript text
        transcript_text = response['results']['channels'][0]['alternatives'][0]['transcript']
        
        # Prepare transcript filename and path (now .txt instead of .json)
        transcript_filename = Path(audio_file).stem + '.txt'
        transcript_path = f'transcripts/{transcript_filename}'
        
        # Save transcript text
        with open(transcript_path, "w", encoding='utf-8') as outfile:
            outfile.write(transcript_text)

        os.remove(audio_file)
        
        return transcript_path

# Example usage
async def main():
    video_url = "https://www.youtube.com/watch?v=yhZAXXI83-4&pp=ygULbGV4IGZyaWRtYW4%3D"
    transcript_path = await create_transcript(video_url)
    print(f"Transcript saved to: {transcript_path}")

if __name__ == "__main__":
    asyncio.run(main())