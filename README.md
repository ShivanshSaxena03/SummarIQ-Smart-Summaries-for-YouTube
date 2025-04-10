# SummarIQ-Smart-Summaries-for-YouTube
SummarIQ uses powerful AI to extract transcripts and generate smart summaries of YouTube videos. Whether it's a 2-hour lecture or a podcast episode, SummarIQ gives you the key insights in seconds.


🧠 YouTube Video Summarizer Chrome Extension
This Chrome Extension automatically summarizes any YouTube video using its transcript and AI-powered transformer models like facebook/bart-large-cnn.

📌 Features
🔗 Paste any YouTube video URL

📝 Fetches the transcript automatically

🧠 Uses HuggingFace Transformers for intelligent summarization

⚡ Summary appears instantly in the popup

✅ Works for most videos with available captions

🛠️ How It Works
Chrome Extension (Frontend)
You paste a YouTube video URL in the popup. The extension sends it to a local Python server.

Python Flask Backend (AI-Powered)

It extracts the video ID

Uses youtube-transcript-api to fetch the transcript

Feeds the transcript to a summarization model (facebook/bart-large-cnn)

Returns a smart, short summary to the extension

Summary Displayed
The extension receives the summary and shows it in the text area.

🧑‍💻 Technologies Used
Chrome Extension: HTML, JS

Python Backend: Flask, HuggingFace Transformers, YouTube Transcript API

Model: facebook/bart-large-cnn

⚙️ How to Use
🔧 1. Clone the Repo

git clone https://github.com/your-username/youtube-summarizer-extension.git
cd youtube-summarizer-extension
🧠 2. Run the Python Backend

cd backend
pip install -r requirements.txt
python app.py
Note: The backend runs on http://localhost:5000

🧩 3. Load Chrome Extension
Go to chrome://extensions

Enable Developer Mode

Click Load Unpacked

Select the extension/ folder

📽️ 4. Paste a YouTube URL & Summarize
Open the extension from Chrome toolbar

Paste a YouTube video link

Click "Summarize"

Wait for 5–10 seconds for the AI to generate the summary

🔐 Requirements
Python 3.8+

Chrome Browser

Internet Connection (for downloading model and fetching transcripts)

