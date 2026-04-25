import httpx
import json
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

class LLMService:
    async def synthesize_content(self, topic: str, age: int, mission_briefing: str):
        """
        Calls local Gemma model to generate personalized educational content.
        """
        prompt = f"""
        You are KidOS, a personalized AI tutor.
        User Age: {age}
        Topic: {topic}
        Behavioral Context: {mission_briefing}
        
        Task: Generate 2 educational cards about the topic.
        Return ONLY valid JSON in this format:
        [
          {{"title": "Card Title", "body": "Simple educational text"}}
        ]
        """
        
        payload = {
            "model": "gemma3:1b", # Using a small, fast model for the hackathon demo
            "prompt": prompt,
            "stream": False,
            "format": "json"
        }
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.post(OLLAMA_URL, json=payload)
                resp.raise_for_status()
                result = resp.json()
                return json.loads(result.get("response", "[]"))
        except Exception as e:
            print(f"LLM Synthesis Error: {e}")
            return [{"title": "Error", "body": "I'm having a little trouble thinking right now. Let's try again!"}]

llm_service = LLMService()
