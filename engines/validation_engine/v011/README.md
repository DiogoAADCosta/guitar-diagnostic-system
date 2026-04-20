# Version 11 — Context Evaluation with Adaptive Flow

## Overview

Version 11 implements adaptive behavior within the context-based test.

The system now evaluates user performance during execution
and dynamically adjusts the flow of questions based on accuracy.

---

## What Changed

Previous versions introduced the structure for context-based evaluation.

Version 11 adds a rule-driven system that:

- Calculates intermediate score during execution  
- Applies conditional rules to control progression  
- Adjusts the number of questions dynamically  

---

## Adaptive Context Evaluation

During the test, the system:

- Tracks correct and incorrect answers  
- Calculates accuracy after a set of questions  
- Uses a rule system to determine the next step  

Possible actions include:

- Adding more questions  
- Changing context  
- Confirming the current level  

---

## Rule System

The adaptive behavior is controlled by a rule set (`regras`):

- Each round contains condition–action pairs  
- The first matching condition defines the next action  
- Actions modify flow and progression state  

---

## Level Progression

The system evaluates performance across contexts within a level.

Based on results:

- The level may increase  
- The level may decrease  
- The level may be confirmed  

A control mechanism prevents infinite loops between levels.

---

## Scope

This version includes:

- Context-based adaptive evaluation  
- Rule-driven progression logic  
- Level transition system  
- Structured data collection (interface, context, tags)  

This version does not include:

- Diagnostic interpretation  
- Final user-facing report  

---

## Key Takeaway

Version 11 marks the transition from static execution
to adaptive and decision-based test behavior.

The system now reacts to user performance in real time,
providing a more structured foundation for future diagnostics.
