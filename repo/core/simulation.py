import random
import time
from datetime import datetime

# --- Configuration Pools ---
ROLES = {
    "Coding Specialist": {
        "topics": ["parsing", "debug", "optimize", "python", "script", "refactor", "api"],
        "weight": 0.9
    },
    "Documentation": {
        "topics": ["workflow", "notes", "improvements", "docs", "readme", "guide"],
        "weight": 0.6
    },
    "Research": {
        "topics": ["trends", "insights", "concepts", "ai", "benchmark", "study"],
        "weight": 0.5
    },
    "QA & Testing": {
        "topics": ["test", "bugs", "fixes", "critical", "coverage", "validation"],
        "weight": 0.8
    },
    "Coordination": {
        "topics": ["priority", "schedule", "conflict", "organize", "resource", "timeline"],
        "weight": 0.7
    },
    "Security": {
        "topics": ["firewall", "auth", "permissions", "integrity", "audit"],
        "weight": 1.0
    },
    "Creative": {
        "topics": ["design", "ui", "ux", "aesthetics", "color", "layout"],
        "weight": 0.6
    }
}

NAMES = [
    "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa",
    "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon",
    "Phi", "Chi", "Psi", "Omega", "Prime", "Nexus", "Vortex", "Cipher", "Echo"
]

TASK_VERBS = [
    "analyzing", "compiling", "reviewing", "optimizing", "debugging", "generating",
    "checking", "updating", "refactoring", "archiving", "monitoring", "scheduling"
]

# --- Global State ---
ACTIVE_COHORT = {}

def initialize_bootcamp(min_agents=5, max_agents=10):
    """Generates a new random cohort of agents."""
    global ACTIVE_COHORT
    ACTIVE_COHORT.clear()
    
    num_agents = random.randint(min_agents, max_agents)
    # Ensure unique names
    selected_names = random.sample(NAMES, num_agents)
    
    count = 0
    for name in selected_names:
        role_name = random.choice(list(ROLES.keys()))
        role_data = ROLES[role_name]
        
        ACTIVE_COHORT[f"Agent-{name}"] = {
            "role": role_name,
            "priority_weight": role_data["weight"],
            "topics": role_data["topics"]
        }
        count += 1
    
    return ACTIVE_COHORT

def generate_simulation_event():
    """Generates a random event from the active cohort."""
    if not ACTIVE_COHORT:
        return None
        
    # 30% chance of event per tick
    if random.random() > 0.3:
        return None
        
    agent_name = random.choice(list(ACTIVE_COHORT.keys()))
    agent_data = ACTIVE_COHORT[agent_name]
    
    topic = random.choice(agent_data["topics"])
    verb = random.choice(TASK_VERBS)
    
    content = f"{verb} {topic} protocols"
    
    # Calculate priority
    priority = agent_data["priority_weight"] + (random.random() * 0.2)
    
    return {
        "agent": agent_name,
        "role": agent_data["role"],
        "content": content,
        "priority": round(priority, 2),
        "timestamp": datetime.now().isoformat()
    }
