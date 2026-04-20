# Version 11 — Adaptive Context Evaluation with Level Progression

## Overview

Version 11 expands the adaptive system by integrating
context-based evaluation with level progression.

The test now evaluates multiple contexts within a level
and uses aggregated performance to determine level transitions.

---

## What Changed

Version 10 introduced adaptive behavior within a single context.

Version 11 extends this by:

- Evaluating all contexts within a level  
- Aggregating performance across contexts  
- Applying level progression logic based on results  

---

## Context Evaluation

The system now:

- Runs multiple contexts per level  
- Collects results per context  
- Stores structured statistics for each context  

---

## Adaptive Behavior

During execution, the system:

- Tracks correct and incorrect answers  
- Calculates intermediate accuracy  
- Applies rule-based decisions per round  

These rules control:

- Question flow within each context  
- Transition between contexts  

---

## Level Progression

After evaluating all contexts in a level, the system:

- Increases level if performance is consistently high  
- Decreases level if performance is consistently low  
- Confirms level otherwise  

A control mechanism prevents repeated level loops.

---

## Scope

This version includes:

- Multi-context evaluation per level  
- Rule-driven adaptive flow  
- Functional level progression system  
- Structured data collection (interface, context, tags)  

This version does not include:

- Diagnostic interpretation  
- Final user-facing report  

---

## Key Takeaway

Version 11 marks the transition from isolated adaptive behavior
to a complete adaptive evaluation system.

The test now combines context evaluation and level progression,
forming a coherent and scalable foundation for diagnostics.
