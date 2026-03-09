// Display Name
if(document.getElementById("nameDisplay")) {
    document.getElementById("nameDisplay").innerText = localStorage.getItem("username");
}

// Scenario 1: Resume Analysis
async function analyze() {
    const skills = document.getElementById("skills").value;
    const res = await fetch('http://127.0.0.1:8000/analyze', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ skills })
    });
    const data = await res.json();
    document.getElementById("results").style.display = "block";
    document.getElementById("score").innerText = data.score;
    document.getElementById("roadmap").innerText = "Roadmap: " + data.roadmap;
}

// Chatbot Logic
async function askBot() {
    const msg = document.getElementById("chatMsg").value;
    const box = document.getElementById("chatBox");
    box.innerHTML += `<p><b>You:</b> ${msg}</p>`;
    
    const res = await fetch('http://127.0.0.1:8001/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    box.innerHTML += `<p style="color:#00d2ff"><b>VidyaMitra:</b> ${data.reply}</p>`;
    document.getElementById("chatMsg").value = "";
}