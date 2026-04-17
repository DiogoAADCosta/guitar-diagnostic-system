# Version 3 — Rule-Based Level Progression Engine

## Overview

Version 3 introduces a rule-based system to control level progression  
based on user performance across multiple rounds.

The system evaluates accuracy thresholds and determines whether the user should:

- Move up a level  
- Stay at the current level  
- Move down a level  

This version replaces hardcoded conditional logic  
with a more structured and scalable approach.

---

## Flow Overview

![Flowchart](dev_notes/flowchart.png)

The progression system is designed to adapt the test dynamically  
based on user performance.

- If the user answers all initial questions correctly,  
  the system assumes mastery of that level and moves up  

- If the user answers all questions incorrectly,  
  the system detects difficulty and moves down  

- If the user has partial success,  
  additional questions are introduced to better assess the level  

This approach reduces unnecessary questions,  
making the test faster and more responsive  
while maintaining accuracy in level evaluation.

---

## Core Idea

Instead of relying on deeply nested conditionals,  
this version organizes decision-making into a rule-based structure:

- Each round has its own set of rules  
- Each rule contains:
  - A condition (based on accuracy)
  - An action (level transition or continuation)

The system evaluates rules sequentially  
and executes the first matching condition.

---

## Data Structure

The question structure in this version is intentionally simplified.
For example:

Equivalent structure in English: {level: 1, number: 1, question: "Question 1"}

Unlike previous versions, which were focused on tag-based analysis,  
this structure is designed specifically to support:

- Level-based progression  
- Controlled question sequencing  
- Round-based evaluation  

This simplification allows the progression logic to be developed  
without additional complexity from diagnostic data.

---

## Key Components

### Rule System

Rules are defined per round as pairs of condition and action.

Each round contains a list of rules,  
and the system executes the first condition that evaluates to true.

---

### Actions

Actions define how the system responds:

- Level up  
- Level down  
- Add more questions  
- Confirm level  

Each action updates the system state (level and round).

---

### Limits

Each round defines how many questions are evaluated  
before checking performance and applying rules.

---

### Main Loop

The system iterates through rounds until the level is confirmed:

- Select questions based on level and sequence  
- Evaluate performance at checkpoints  
- Apply rules to determine the next step  

---

## Development Notes

Temporary values were used during development  
to simulate user performance and test the flow.

These values are placeholders and are replaced  
by real user input in the final system.

---

## Evolution

This version is the result of iterative refinement.

For a detailed breakdown of how the logic evolved internally, see:

👉 [v3_evolution.md](./v3_evolution.md)

---

## Key Insight

The main improvement in Version 3 is the separation between:

- Decision logic (rules)  
- Execution logic (actions)  

This makes the system easier to understand, modify, and scale.

---

## Scope

This version focuses exclusively on progression logic.

It does not include:

- Tag-based analysis  
- Diagnostic generation  
- Integration with behavioral engine  

These components are handled in other parts of the system.
