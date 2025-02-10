from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from utils.create_transcript import get_video_id, get_transcript, generate_qa_pairs

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Example Lex Fridman episode URL
url = "https://www.youtube.com/watch?v=yhZAXXI83-4&pp=ygULbGV4IGZyaWRtYW4%3D"  # Replace with actual episode URL

def process_episode(url: str):
    # Get transcript
    video_id = get_video_id(url)
    transcript = get_transcript(video_id)
    
    if not transcript:
        return None
    
    # Generate Q&A pairs
    qa_pairs = generate_qa_pairs(client, transcript)
    
    # Save to file
    output_file = f"training_data/{video_id}_qa_pairs.json"
    os.makedirs("training_data", exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(qa_pairs, f, indent=2)
    
    return output_file

if __name__ == "__main__":
    output_file = process_episode(url)
    print(f"Training data saved to: {output_file}")