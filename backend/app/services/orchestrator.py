from app.services.brain_logic import brain_logic
from app.services.supabase_service import db_service

class ContentOrchestrator:
    async def decide_next_step(self, user_id: str):
        """
        Coordinates between behavioral analysis and content strategy.
        """
        # Fetch kernel to understand threshold
        kernel = await db_service.get_kernel(user_id)
        threshold = kernel.get("frustration_threshold", 0.65) if kernel else 0.65
        
        # In a full impl, we'd fetch actual signals from the DB here
        # For this step, we'll use a mocked signal set for logic demonstration
        signals = [] 
        
        f_score = brain_logic.compute_frustration(signals)
        svi_score = brain_logic.compute_svi(signals)
        
        if f_score > threshold:
            return {
                "action": "SIMPLIFY",
                "reason": "High frustration detected",
                "mission_briefing": "User is overwhelmed. Use ultra-simple words and very short sentences. Avoid complex jargon."
            }
        elif svi_score < 0.3:
            return {
                "action": "STIMULATE",
                "reason": "Low engagement detected",
                "mission_briefing": "User is bored. Introduce a surprising, fun fact or a gamified challenge."
            }
        
        return {
            "action": "CONTINUE",
            "reason": "Optimal learning zone",
            "mission_briefing": "User is engaged. Continue with standard age-appropriate vocabulary and exploratory depth."
        }

orchestrator = ContentOrchestrator()
