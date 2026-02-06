import json
from datetime import datetime
from pathlib import Path

# Paths relative to the repo root (assuming cwd is repo root)
OBSERVER_DIR = Path("observer")
MEMORY_PATH = OBSERVER_DIR / "memory.json"
SESSIONS_DIR = OBSERVER_DIR / "sessions"

def load_memory():
    """Load persistent memory from JSON."""
    if MEMORY_PATH.exists():
        try:
            mem = json.loads(MEMORY_PATH.read_text())
            # Ensure new keys exist if loading old memory
            mem.setdefault("sessions", [])
            mem.setdefault("preferences", [])
            mem.setdefault("facts", [])
            mem.setdefault("learned_concepts", {})
            mem.setdefault("potential_concepts", {})
            mem.setdefault("simulation_logs", [])
            return mem
        except json.JSONDecodeError:
            return {
                "sessions": [], 
                "preferences": [], 
                "facts": [], 
                "learned_concepts": {},
                "potential_concepts": {},
                "simulation_logs": []
            }
    return {
        "sessions": [], 
        "preferences": [], 
        "facts": [], 
        "learned_concepts": {},
        "potential_concepts": {},
        "simulation_logs": []
    }

def save_memory(memory):
    """Save persistent memory to JSON."""
    # Ensure directory exists
    if not OBSERVER_DIR.exists():
        OBSERVER_DIR.mkdir(parents=True)
    
    MEMORY_PATH.write_text(json.dumps(memory, indent=2))

def log_session_file(session_data, session_start_time):
    """Write the full session log to a timestamped markdown file."""
    if not SESSIONS_DIR.exists():
        SESSIONS_DIR.mkdir(parents=True)
        
    timestamp_str = session_start_time.strftime("%Y%m%d_%H%M%S")
    filename = f"session_{timestamp_str}.md"
    file_path = SESSIONS_DIR / filename
    
    content = [f"# Session Log: {session_start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"]
    
    for entry in session_data:
        # entry is expected to be dict: {"role": "user/bim", "content": "..."}
        role = entry.get("role", "UNKNOWN").upper()
        text = entry.get("content", "")
        content.append(f"**{role}:** {text}\n")
        
    file_path.write_text("\n".join(content))
    return filename

def record_preference(memory, observation):
    """Log a preference or pattern to memory."""
    memory.setdefault("preferences", [])
    if observation not in memory["preferences"]:
        memory["preferences"].append(observation)

def verify_integrity(memory):
    """Self-check memory structure and simulation connection."""
    checks = {
        "memory_loaded": False,
        "concepts_active": False,
        "simulation_active": False,
        "logs_writable": True
    }
    
    if memory:
        checks["memory_loaded"] = True
        
    if "learned_concepts" in memory:
        checks["concepts_active"] = True
        
    if "simulation_logs" in memory:
        checks["simulation_active"] = True
        
    if not SESSIONS_DIR.exists():
        checks["logs_writable"] = False
        
    all_passed = all(checks.values())
    return all_passed, checks

