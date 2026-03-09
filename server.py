from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import random

app = FastAPI()

# Enable CORS (Allows your HTML files to talk to this Python server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    text: str

# 1. Home Route
@app.get("/")
def home():
    return {"message": "VidyaMitra API is running on Port 8010!"}

# 2. Scenario 1 & 3: Resume Evaluation & Roadmap
@app.post("/analyze")
async def analyze(data: UserInput):
    score = random.randint(75, 95)
    return {
        "score": score,
        "roadmap": ["Phase 1: Foundation Skills", "Phase 2: Project Portfolio", "Phase 3: Industry Certification", "Phase 4: Placement Prep"],
        "advice": "Add more technical keywords like 'API Integration' and 'Cloud' to your profile."
    }

# 3. Chatbot Route
@app.post("/chat")
async def chat(data: UserInput):
    msg = data.text.lower()
    if "resume" in msg: return {"reply": "A strong resume needs clear project impacts."}
    if "roadmap" in msg: return {"reply": "I have generated a roadmap for you in the Evaluator section!"}
    return {"reply": "I am VidyaMitra, your AI Career Assistant. How can I help?"}

# 4. Scenario 2: Mock Interview Questions
@app.get("/get-questions")
async def get_questions():
    return [
        {"id": 1, "q": "What is the difference between SQL and NoSQL?", "type": "Technical"},
        {"id": 2, "q": "How do you handle project deadlines?", "type": "HR"},
        {"id": 3, "q": "Explain the concept of REST APIs.", "type": "Technical"}
    ]
# Add this to your server.py
@app.post("/chat")
async def chat(data: UserInput):
    msg = data.text.lower()
    if "resume" in msg: return {"reply": "A strong resume needs clear projects."}
    if "roadmap" in msg: return {"reply": "I've designed a 4-phase roadmap for you in the sidebar!"}
    return {"reply": "I am VidyaMitra. I am here to help you get hired!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8010)
