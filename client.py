from typing import Dict, Any, List, Optional

class HierarchicalMemoryConsolidationCompressor:
    """
    Filters ephemeral conversational chatter and distills high-salience persistent facts,
    preferences, and commitments into permanent long-term memory blocks.
    """
    SALIENT_INDICATORS = [
        "prefer", "always", "never", "my name is", "remember that", "important",
        "credential", "api key", "password", "objective", "deadline", "budget"
    ]

    def consolidate_dialogue_turns(
        self,
        turns: List[Dict[str, Any]],
        importance_threshold: float = 0.60
    ) -> Dict[str, Any]:
        retained_memories = []
        discarded_chatter = 0

        for turn in turns:
            role = turn.get("role", "user")
            content = turn.get("content", "").strip()
            low = content.lower()

            matches = [ind for ind in self.SALIENT_INDICATORS if ind in low]
            # Salience calculation
            salience_score = min(1.0, len(matches) * 0.4 + (0.2 if role == "user" else 0.1))

            if salience_score >= importance_threshold:
                retained_memories.append({
                    "turn_id": turn.get("id"),
                    "role": role,
                    "extracted_fact": content,
                    "salience_score": round(salience_score, 2),
                    "trigger_keywords": matches
                })
            else:
                discarded_chatter += 1

        compression_ratio = round((discarded_chatter / max(1, len(turns))) * 100, 1)

        return {
            "total_turns": len(turns),
            "retained_memories_count": len(retained_memories),
            "discarded_chatter_count": discarded_chatter,
            "token_compression_pct": compression_ratio,
            "consolidated_semantic_memory": retained_memories
        }
