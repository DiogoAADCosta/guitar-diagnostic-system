# Version 10 — Adaptive Context Evaluation

## Overview

Version 10 introduces adaptive behavior within the context-based test.

The system now evaluates user performance during execution
and dynamically adjusts the number of questions based on accuracy.

---

## What Changed

Previous versions introduced the structure for context-based evaluation.

Version 10 implements the first adaptive layer within this stage.

The test no longer follows a fixed number of questions.
Instead, it reacts to user performance in real time.

---

## Adaptive Evaluation

During the test, the system:

- Tracks correct and incorrect answers  
- Calculates intermediate accuracy (score)  
- Applies rule-based decisions to control the flow  

Based on performance, the system may:

- Ask additional questions  
- Confirm the current level  
- Prepare for level adjustment (structure in place)  

---

## Rule System

The adaptive behavior is driven by a rule set (`regras`):

- Each round applies different conditions  
- Decisions are based on accuracy thresholds  
- Actions modify:
  - Number of remaining questions  
  - Test progression state  

---

## Key Behavior

- Evaluation happens in cycles (rounds)  
- Each cycle ends with an intermediate score check  
- The next action is defined dynamically  
- The test currently runs one context per execution  

---

## Limitations

- Context switching is not implemented  
- Level progression is partially implemented  
- Some progression logic is preserved as legacy structure  

---

## Scope

This version includes:

- Context-based adaptive flow  
- Rule-driven progression control  

This version does not include:

- Context switching  
- Multi-context execution  
- Final diagnostic output  

---

## Key Takeaway

Version 10 marks the transition from static evaluation
to adaptive test behavior.

The system now responds to user performance in real time,
laying the foundation for more precise diagnostics.
