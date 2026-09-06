import json
from client import HierarchicalMemoryConsolidationCompressor

def main():
    compressor = HierarchicalMemoryConsolidationCompressor()
    dialogue = [
        {"id": 1, "role": "user", "content": "Hi, how are you today?"},
        {"id": 2, "role": "assistant", "content": "I am great! How can I help?"},
        {"id": 3, "role": "user", "content": "Remember that I always prefer dark mode and my budget is $5000."},
        {"id": 4, "role": "assistant", "content": "Understood, noted dark mode and budget."}
    ]
    res = compressor.consolidate_dialogue_turns(dialogue)
    print("Memory Consolidation Result:")
    print(json.dumps(res, indent=2))
    assert res["retained_memories_count"] == 1
    assert res["consolidated_semantic_memory"][0]["turn_id"] == 3
    print("Memory consolidation compressor verification: PASS")

if __name__ == "__main__":
    main()
