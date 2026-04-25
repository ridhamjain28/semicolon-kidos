# KidOS Technical Architecture

## Overview
KidOS operates as a feedback loop between the child and the Generative AI.

1. **The Kernel**: A persistent JSON state representing the child's age, mastery levels, and current curiosity type.
2. **The Memory**: A vector store (ChromaDB/Supabase) that holds past interactions to provide context for future content.
3. **The Brain (IBLM)**: The orchestrator that takes signals, updates the kernel, and instructs the AI on what to generate next.

## Data Flow
`User Action` -> `Signal Extraction` -> `Kernel Update` -> `Brain Decision` -> `Content Generation`
