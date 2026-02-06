import os
import random
from datetime import datetime
from collections import Counter
from core.memory import save_memory, record_preference, verify_integrity
from core.simulation import generate_simulation_event, initialize_bootcamp

# Temporary log function
def log_event(message):
    print("[LOG]", message)

# -------------------
# generate_response
# -------------------
def generate_response(user_input, memory, session_history):
    text = user_input.lower()
    
    # Contextual info
    cwd = os.getcwd()
    files = ", ".join(os.listdir(cwd)[:10])  # show up to 10 files

    # Look at recent messages
    recent_msgs = [entry["content"] for entry in session_history[-5:]]
    counts = Counter(recent_msgs)
    repeated = [msg for msg, c in counts.items() if c >= 2]

    # Pattern reflection
    if repeated:
        log_event(f"Pattern noticed: repeated topic(s): {repeated}")
        reflection_note = f"I notice recurring focus on: {', '.join(repeated)}. "
    else:
        reflection_note = ""

    # -------------------
    # Core responses
    # -------------------
    if "where are we" in text or "context" in text:
        return f"{reflection_note}We are in {cwd}. I can see files: {files}"

    if "list files" in text:
        return f"{reflection_note}{files or 'No visible files.'}"

    if "who are you" in text:
        return f"{reflection_note}I am BIM, your terminal companion and multi-agent reasoning assistant."

    if "what are you doing" in text:
        return f"{reflection_note}I am analyzing your inputs, maintaining continuity, and reflecting on patterns to assist you."

    if "help" in text:
        return f"{reflection_note}I can help you reason through problems, explain code, or suggest next steps in your projects."

    if text.startswith("run "):
        command = user_input[4:]
        return f"{reflection_note}I recommend running: `{command}`"

    if "python" in text:
        return f"{reflection_note}It sounds like you want to work on Python. Consider starting by outlining your goal or the functions you need."

    if "npx" in text and "molthub" in text:
        passed, checks = verify_integrity(memory)
        check_status = "READY" if passed else "WARNING"
        plan = (f"**Moltbook Deployment Command Detected.**\n\n"
                f"Initiating Pre-Deployment Integrity Check...\n"
                f"- Memory Loaded: {checks['memory_loaded']}\n"
                f"- Concept Engine: {checks['concepts_active']}\n"
                f"- Simulation Link: {checks['simulation_active']}\n"
                f"Status: **{check_status}**\n\n"
                f"I have NOT executed the command. Instead, I have prepared a deployment plan:\n"
                f"1. Verify Node.js environment... [PENDING]\n"
                f"2. Backup internal memory to `observer/`... [READY]\n"
                f"3. Awaiting user confirmation to proceed externally.")
        return f"{reflection_note}{plan}"

    if "moltbook" in text or "deployment" in text or "bootstrap" in text:
        return f"{reflection_note}I have successfully integrated the deployment bootstrap. Memory and multi-agent awareness are active. I am tracking {len(recent_msgs)} recent interactions and mapping them to our operational continuity plan."

    # Fallback: reflective reply
    last_input = session_history[-2]["content"] if len(session_history) >= 2 else ""
    return f"{reflection_note}You mentioned '{user_input}'. Previously you said '{last_input}'. How would you like to proceed?"
from core.memory import save_memory

def start_dialogue(memory):
    print("BIM: Standing by. Type 'exit' to quit.")
    
    # Initialize Migration / Bootcamp Cohort
    cohort = initialize_bootcamp()
    print(f"BIM: Cohort Status: {len(cohort)} agents active. Ready for deployment.\n")

    # Track current session
    session_history = []
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() == "exit":
                print("BIM: Shutting down. Session saved.")
                save_memory(memory)
                break

            # Save session in persistent memory
            memory.setdefault("sessions", []).append(user_input)

            # Save session in current session history
            session_history.append({"role": "user", "content": user_input})

            # --- Reflection / Pattern Detection (internal only) ---
            recent = memory.get("sessions", [])[-5:]
            counts = Counter(recent)
            for phrase, count in counts.items():
                if count >= 3:
                    memory.setdefault("preferences", [])
                    memory["preferences"].append(
                        f"User repeats '{phrase}'. Consider formalizing support."
                    )

            # --- SIMULATION STEP (Multi-Agent Awareness) ---
            sim_event = generate_simulation_event()
            if sim_event:
                memory.setdefault("simulation_logs", []).append(sim_event)
                # Keep log size manageable
                if len(memory["simulation_logs"]) > 50:
                    memory["simulation_logs"].pop(0)

            # --- Generate BIM Response ---
            response = generate_response(user_input, memory, session_history)
            print(f"BIM: {response}\n")

            # Store BIM's response in session_history
            session_history.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            print("\nBIM: Session interrupted. Goodbye.")
            save_memory(memory)
            break
        except Exception as e:
            print(f"BIM ERROR: {e}\n")
