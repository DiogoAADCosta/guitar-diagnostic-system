# Guitar Skill Assessment System

This repository documents my learning journey in Python, with a focus on logic, problem-solving, and system design.

Instead of collecting random exercises, the goal is to build and evolve a real-world system while improving programming fundamentals.

## Structure

This repository is organized as a system evolution log:

- Core Project (Guitar Level Assessment System)
- Engine Development (logic and architecture evolution)
- Supporting Experiments (isolated tests when necessary)

## Main Project

### 🎸 Guitar Level Assessment System

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
   - (Future) Musical Phrasing

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

## Project Evolution

Each version of the system improves:

- Data structure design
- Code readability
- Logic clarity
- Scalability

All versions are documented to show the evolution of the system.

---

**Goal:** Build strong programming fundamentals while designing a real diagnostic system.
