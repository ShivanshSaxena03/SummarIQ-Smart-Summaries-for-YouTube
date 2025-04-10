from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

app = Flask(__name__)
CORS(app)  # 🔥 Allow frontend to access backend
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_video_id(url):
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
    max_chunk_size = 1000
    text_chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summary = ""
    for chunk in text_chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

@app.route("/summarize", methods=["POST"])
def summarize():
    print("🔁 /summarize route hit")
    data = request.json
    url = data.get("url")
    print("📹 URL received:", url)
    try:
        transcript = get_transcript(url)
        print("📝 Transcript fetched")
        summary = summarize_text(transcript)
        print("✅ Summary generated")
        return jsonify({"summary": summary})
    except Exception as e:
        print("❌ Error occurred:", str(e))
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
