# GenPark AI Agent Skill - Hierarchical Memory Consolidation Compressor

Distills multi-turn conversational dialogue into dense, high-salience persistent semantic memory blocks.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Raw Dialogue History Stream] --> B[Ephemeral Chatter Sieve: Greetings / Small Talk]
    B --> C[Salience Pattern Classifier: preferences, constraints, facts]
    C --> D{Salience Score >= Threshold?}
    D -->|Yes| E[Promote to Permanent Long-Term Memory Tier]
    D -->|No| F[Discard from Long-Term Context Window]
```

## Features
- **Token Pruning**: Prevents context window bloat by dropping pleasantries and transient queries.
- **Zero External Dependencies**: Pure Python 3.9+ standard library.
