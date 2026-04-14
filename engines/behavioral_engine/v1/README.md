# Version 1 - Initial Structure

## Goal

The goal of this version is to build the basic execution flow of the test:

- Display questions
- Capture user input
- Associate answers with tags
- Store results in separate lists

## Data Model

Each question contains multiple answers, and each answer has an associated tag.

Tags are intended to represent:

- "limitadores" (limitations)
- "capacidades" (strengths)

## Key Decisions

- Tags are embedded directly within each answer
- The system separates results into two lists:
  - Limitations
  - Strengths
- The structure allows future expansion with multiple tags per answer

## Problems Identified

### 1. Inconsistent Tag Structure

Tags are not standardized:

- Sometimes stored as:
  - ['limitador', 'base']
- Sometimes stored as:
  - [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']]

This inconsistency increases processing complexity.

### 2. Complex Conditional Logic

Due to inconsistent structure, the code requires multiple conditional checks:

- Direct comparison
- Nested indexing

This reduces readability and increases cognitive load.

### 3. Data vs Logic Misalignment

Part of the complexity comes from compensating in the logic for a poorly defined data structure.

## Conclusion

This version successfully implements the core execution flow and validates the concept.

However, it exposes an important insight:

- Poor data structure design leads to unnecessary complexity in logic.

This will be the main focus of improvement in the next version.
