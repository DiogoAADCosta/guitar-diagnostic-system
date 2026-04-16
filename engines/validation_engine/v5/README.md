# Version 5 — Real Data Integration, Context Mapping and Loop Control

## Overview

Version 5 transforms the system from a structural prototype into a fully data-driven diagnostic engine.

This version introduces real musical questions, contextual tagging, improved user interaction handling, and control mechanisms to ensure stable progression behavior.

Unlike previous versions, the system is no longer just evaluating performance — it is now collecting meaningful data that can be used for deeper analysis.

---

## What’s New

* Real guitar-based questions replace placeholders
* Context-aware tagging system (tag + musical context)
* "I don't know" answer handling for better UX and cleaner data
* Loop control to prevent level oscillation (anti ping-pong logic)

---

## How It Works

The system runs in a continuous adaptive loop:

1. Questions are selected based on the current level
2. Answers are validated (correct / incorrect)
3. Performance is updated in real time
4. Tags are collected from each answer
5. Tags are linked to their musical context
6. Accuracy is calculated at the end of each round
7. A rule engine determines the next action

Possible outcomes:

* Move up a level
* Move down a level
* Continue with more questions
* Confirm the current level

---

## Core Systems

### 1. Real Data Layer

The system now uses real guitar questions instead of placeholders.

Each question includes:

* Level
* Musical context (e.g. triads, inversions, extensions)
* Answer options
* Tags linked to each alternative

This allows the system to generate meaningful diagnostic data.

---

### 2. Context Mapping

Each answer generates:

* Tags (capacity or limitation)
* Context (where that skill applies)

This creates a structured relationship:

(tag → context)

Example:

* "leitura_cifras" → "triades_simples"
* "leitura_tablatura" → "power_chords"

This enables future analysis beyond simple scoring.

---

### 3. "I Don't Know" Handling

Special answer types were introduced to improve both:

* User experience
* Data quality

"I don't know" options:

* Are never shuffled with normal answers
* Always appear at the end
* Prevent forced guessing

This results in more reliable diagnostic data.

---

### 4. Rule-Based Progression Engine

The system uses a rule engine to control progression.

Each round defines:

* Accuracy thresholds
* Associated actions

The engine evaluates rules sequentially and applies the first match.

This ensures:

* Predictable behavior
* Easy scalability
* Clear separation between logic and execution

---

### 5. Loop Control (Anti Ping-Pong)

A control mechanism prevents infinite level oscillation:

* If the user both goes up and down in the same session
* The system stops further transitions

This avoids unstable loops like:

Level 3 → Level 4 → Level 3 → Level 4...

---

### 6. State Reset

When the level changes:

* Accuracy counters are reset
* Question sequence restarts

This ensures each level is evaluated independently.

---

## Key Insight

Version 5 is the first version where:

* Data collection
* Context mapping
* Progression logic

are all working together in a single system.

The test is no longer just adaptive — it is now **diagnostic-ready**.

---

## Scope

This version includes:

* Real question system
* Tag and context mapping
* Rule-based progression
* Loop control

This version does not yet include:

* Diagnostic interpretation
* Report generation
* Behavioral engine integration

---

## Evolution

Version 5 builds directly on:

* Version 3 — progression engine
* Version 4 — validation + progression integration

And introduces the first complete foundation for a full diagnostic system.
