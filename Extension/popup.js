document.getElementById("summarizeBtn").addEventListener("click", () => {
    const url = document.getElementById("urlInput").value;
    const output = document.getElementById("output");
  
    output.value = "⏳ Summarizing...";
  
    fetch("http://127.0.0.1:5000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url })
    })
    .then(res => res.json())
    .then(data => {
      console.log("📥 Response received:", data);
      if (data.summary) {
        output.value = data.summary;
      } else {
        output.value = "❌ Error: " + (data.error || "Unknown error");
      }
    })
    .catch(err => {
      console.error("❌ Network error:", err);
      output.value = "❌ Network error: " + err.message;
    });
  });
  