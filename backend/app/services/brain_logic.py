import math
from typing import List

class IBLMBrain:
    def compute_frustration(self, signals: List[dict]) -> float:
        """
        F(t) = Sum of (Target_Duration - Actual_Duration) / Target_Duration
        Logic: Many short skips = rising frustration.
        """
        if not signals:
            return 0.0
        
        # Filter for skip signals
        skips = [s for s in signals if s.get("signal_type") == "skip"]
        if not skips:
            return 0.0
            
        # Simplified: Each skip adds 0.1 frustration, capped at 1.0
        return min(1.0, len(skips) * 0.1)

    def compute_svi(self, interactions: List[dict]) -> float:
        """
        Stimulus Value Index: Measures how much educational value the child is extracting.
        High dwell time = High SVI.
        """
        dwells = [i.get("value", 0) for i in interactions if i.get("signal_type") == "dwell"]
        if not dwells:
            return 0.5 # Default middle value
        
        avg_dwell = sum(dwells) / len(dwells)
        # Assuming 30 seconds (30000ms) is 'max value' engagement
        return min(1.0, avg_dwell / 30000)

brain_logic = IBLMBrain()
