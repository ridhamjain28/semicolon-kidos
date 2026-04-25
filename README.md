# 🌟 KidOS: The Personal AI Learning Adventure

KidOS is an **Individual Behavior Learning Model (IBLM)** powered platform designed for kids (5-13). It solves the "one-size-fits-all" problem in education by using a real-time behavioral feedback loop to synthesize personalized content locally.

## 🚀 The Innovation: The IBLM Feedback Loop

Unlike traditional platforms, KidOS doesn't just track correct answers. It tracks **Behavioral Signals**:
- **F(t) - Frustration Score**: Detects "button mashing" or fast skipping to identify when a child is overwhelmed.
- **SVI - Stimulus Value Index**: Measures "Dwell Time" to see what topics actually spark curiosity.

**The Loop:**
`Interaction -> Signal Extraction -> Brain Decision (Orchestrator) -> Personalized Synthesis (Gemma) -> Engagement`

## 🛠️ Tech Stack

- **Frontend**: Next.js 14, Tailwind CSS, Framer Motion (Glassmorphism & Micro-animations)
- **Backend**: FastAPI (Python 3.10+)
- **Brain**: IBLM Core Logic (Custom Math)
- **Intelligence**: Google Gemma (Running locally via Ollama)
- **Persistence**: Supabase (Cloud Kernels & Session Sync)

## 📦 Getting Started

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Set your SUPABASE_URL and SUPABASE_KEY in .env
uvicorn main:app --reload --port 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 3. Intelligence (Local)
Ensure [Ollama](https://ollama.ai/) is running and pull the model:
```bash
ollama pull gemma3:1b
```

## 🧠 Core Philosophy
KidOS believes that every child is unique. By combining **Behavioral Psychology** with **Generative AI**, we create a learning environment that is as dynamic and curious as the children who use it.

---
Built with ❤️ for the Semicolon Hackathon.
