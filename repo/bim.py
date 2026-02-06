# bim.py

from core.dialogue import start_dialogue
from core.memory import load_memory, save_memory

def boot_sequence():
    print("Initializing BIM...")
    memory = load_memory()  # load persistent memory
    print("Loading memory...")
    print("Standing by.\n")
    return memory

if __name__ == "__main__":
    memory = boot_sequence()       # load memory first
    start_dialogue(memory)         # pass memory to dialogue
    save_memory(memory)            # save memory after session
