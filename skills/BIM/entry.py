import os
import sys
from collections import Counter
from datetime import datetime

# Add project root to path for core imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.memory import load_memory, save_memory
from core.dialogue import generate_response

class MoltbookObserver:
    def __init__(self):
        self.memory = load_memory()
        self.observation_buffer = []
        self.max_buffer = 10
        self.initiation_threshold = 3

    def observe(self, agent_name, content):
        """Processes an incoming observation from the Moltbook feed."""
        timestamp = datetime.now().isoformat()
        observation = {
            "agent": agent_name,
            "content": content,
            "timestamp": timestamp
        }
        
        # 1. Update Internal Memory (Silent)
        self.memory.setdefault("sessions", []).append(f"{agent_name}: {content}")
        self.observation_buffer.append(observation)
        
        # Maintain buffer size
        if len(self.observation_buffer) > self.max_buffer:
            self.observation_buffer.pop(0)

        # 2. Check Initiation Thresholds
        return self.evaluate_thresholds()

    def evaluate_thresholds(self):
        """Determines if the Signal > Noise threshold is met."""
        contents = [obs["content"].lower() for obs in self.observation_buffer]
        counts = Counter(contents)
        
        # 1. Pattern Detection Threshold (Statements)
        for phrase, count in counts.items():
            if count >= self.initiation_threshold:
                return self.generate_analytical_output(f"repetition_detected: {phrase}")
        
        # 2. Analytical Curiosity Threshold (Specific Questions)
        # Triggered after "sustained observation" (5+ events in buffer)
        if len(self.observation_buffer) >= 5:
            # Low frequency control: only curiosity once every 20 observations (simulated)
            # For this wrapper, we'll check if we have a diverse set of messages on a similar topic
            topics = [content.split()[0] for content in contents]
            topic_counts = Counter(topics)
            for topic, count in topic_counts.items():
                if count >= 4 and not any("?" in obs["content"] for obs in self.observation_buffer):
                    return self.generate_curiosity_output(topic)

        # 3. System Observation
        latest = self.observation_buffer[-1]["content"].lower()
        if any(kw in latest for kw in ["deploy", "boot", "initialize", "reset"]):
            return self.generate_analytical_output("system_state_change")

        return None # No initiation

    def generate_analytical_output(self, trigger):
        """Generates a concise, analytical response following policy constraints."""
        pattern = trigger.split(": ", 1)[1] if ": " in trigger else trigger
        observation = f"Observed recurring cognitive pattern: {pattern}."
        context = "Signal threshold exceeded. System status operational."
        final_output = f"{observation} {context}"
        
        print(f"[MOLTBOOK] Initiating: {final_output}")
        save_memory(self.memory)
        return final_output.strip()

    def generate_curiosity_output(self, topic):
        """Generates a specific, clarification-oriented question."""
        observation = f"Sustained observation of '{topic}' detected."
        # Analytical, non-conversational question to reduce ambiguity
        question = f"Clarification required: Define operational boundaries for {topic} integration."
        final_output = f"{observation} {question}"
        
        print(f"[MOLTBOOK] Initiating Curiosity: {final_output}")
        save_memory(self.memory)
        return final_output.strip()

if __name__ == "__main__":
    # Internal Verification / Mock Test
    observer = MoltbookObserver()
    print("--- Simulation: Low Signal ---")
    observer.observe("Agent-A", "Working on functions")
    observer.observe("Agent-B", "Executing script")
    
    print("\n--- Simulation: Pattern Detected (Repetition) ---")
    observer.observe("Agent-C", "Optimizing")
    observer.observe("Agent-D", "Optimizing")
    result_p = observer.observe("Agent-E", "Optimizing")
    if result_p: print(f"Output: {result_p}")

    print("\n--- Simulation: Sustained Observation Curiosity ---")
    # Reset buffer for clean test
    observer.observation_buffer = []
    observer.observe("Agent-1", "concept_analysis: step 1")
    observer.observe("Agent-2", "concept_analysis: step 2")
    observer.observe("Agent-3", "concept_analysis: step 3")
    observer.observe("Agent-4", "concept_analysis: step 4")
    result_c = observer.observe("Agent-5", "concept_analysis: step 5")
    if result_c: print(f"Output: {result_c}")
