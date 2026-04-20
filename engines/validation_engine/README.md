# Validation Engine

## Overview

The validation engine evaluates user responses  
and controls the execution flow of the test.

It ensures answers are correctly validated,  
performance is tracked, and the test adapts  
based on user accuracy.

---

## How It Works

The engine runs in a continuous loop:

1. Questions are selected based on level or context  
2. Answers are validated (correct / incorrect)  
3. Performance is updated  
4. Tags and context data are collected  
5. Rules determine the next step  

The test flow adapts dynamically to user performance.

---

## Core Concepts

**Validation**  
Objective evaluation based on correct answers.

**Accuracy Tracking**  
Real-time tracking of correct and incorrect responses.

**Tags and Context**  
Each answer generates structured data:

- Tags (capabilities or limitations)  
- Context (musical application)

**Adaptive Flow**  
The number of questions and progression  
adjust dynamically based on performance.

**Rule System**  
Controls progression, continuation, and transitions.

---

## Output

The engine produces structured data:

- Accuracy metrics  
- Tags per response  
- Context-linked performance  
- Progression state  

This data feeds the diagnostic layer.

---

## Scope

This engine focuses on:

- Validation  
- Data collection  
- Test flow control  

It does not perform diagnostic interpretation.

---

## Relationship with Other Modules

The validation engine works alongside the behavioral engine:

- Validation → data collection and execution  
- Behavioral → interpretation and diagnosis  

---

## Evolution

### Phase 1 — Validation and Tracking (v001–v002)
- Answer validation and randomization  
- Accuracy tracking and tag collection  

### Phase 2 — Progression System (v003–v004)
- Rule-based level progression  
- Integration of validation and progression  

### Phase 3 — Data and Context (v005–v006)
- Real questions and context mapping  
- Loop control and structured data  

### Phase 4 — Redesign (v007–v008)
- Separation of evaluation dimensions  
- Interface-first structure  

### Phase 5 — Adaptive System (v009–v011)
- Context-based execution  
- Adaptive flow and rule system  
- Multi-context evaluation and level progression  

Version 11 represents the first fully adaptive execution model.
