# Guitar Diagnostic System

This repository documents the development of a real-world system as I build my programming and software engineering skills, with a focus on logic, problem-solving, and system design.

Instead of collecting random exercises, the goal is to build and evolve a real-world system while improving programming fundamentals.

## Structure

This repository is organized as a system evolution log:

- Core Project (Guitar Level Assessment System)
- Engine Development (logic and architecture evolution)
- Supporting Experiments (isolated tests when necessary)

## Main Project

### 🎸 Guitar Diagnostic System

A behavioral-based diagnostic system designed to evaluate guitar skills using structured questions and rule-based analysis.

## How the System Works

The system follows a structured decision flow:

1. The user selects their main goal  
   (e.g., playing songs, improvising, creating music)

2. Based on the goal, the system activates relevant skill pillars:
   - Fretboard Mapping
   - Musical Understanding
   - Ear Training
   - Technique
   - (Planned) Musical Phrasing

3. The user performs a self-assessment to indicate their current level

4. The system dynamically determines the appropriate starting point

5. The user completes one or more tests:
   - Behavioral test (no right/wrong answers, pattern-based)
   - Knowledge-based test (with validation)

6. Each test generates a partial diagnosis

7. All diagnoses are combined into a final result,
   indicating strengths, limitations, and next steps
## System Design Focus

This project is not just about coding — it focuses on:

- Behavioral modeling
- Data structuring
- Rule-based diagnosis systems
- Scalability of logic
- Separation between data collection and interpretation

## Engine Design

The system is built around reusable engines:

- A response-based engine (captures user patterns)
- A validation-based engine (checks correctness)

These engines are designed to be reused across different goals and skill pillars.

## 🚀 Latest Stable Versions
- [Behavioral Engine (v009)](./engines/behavioral_engine/v009_latest_stable/code.py)
- [Validation Engine (v011)](./engines/validation_engine/v011_latest_stable/code.py)

## Project Evolution

Each version of the system improves:

- Data structure design
- Code readability
- Logic clarity
- Scalability

All versions are documented to show the evolution of the system.
Note: As I am currently progressing through my Software Engineering studies, this repository intentionally preserves previous versions (v1, v2, etc.) to document the evolution of the system's architecture and my growth as a developer.

---

**Goal:** Develop strong programming and system design skills by building and evolving a real diagnostic system from scratch.
