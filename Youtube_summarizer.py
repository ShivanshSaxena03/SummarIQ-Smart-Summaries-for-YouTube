from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

def get_video_id(url):
    # Extract video ID from URL
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

def get_transcript(video_url):
    video_id = get_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([entry['text'] for entry in transcript])
    return text

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Split long text into chunks (HuggingFace has a 1024 token limit)
    max_chunk_size = 1000
    text_chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summary = ""
    for chunk in text_chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    try:
        print("\nFetching transcript...")
        transcript = get_transcript(video_url)
        print("Summarizing...")
        summary = summarize_text(transcript)
        print("\n📄 Video Summary:\n")
        print(summary)
    except Exception as e:
        print(f"❌ Error: {e}")
