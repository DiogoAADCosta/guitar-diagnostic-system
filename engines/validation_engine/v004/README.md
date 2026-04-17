# Version 4 — Integrated Validation and Progression Engine

## Overview

Version 4 integrates two previously independent systems:

* Progression logic (Version 3)
* Answer validation and tag extraction (Version 2)

This is the first fully functional version of the test,
where user responses directly drive both performance tracking
and level progression in real time.

---

## How It Works

The system runs in a continuous loop:

1. Questions are selected based on the current level
2. Answers are validated (correct / incorrect)
3. Performance is updated
4. Tags are collected from each response
5. Accuracy is calculated after each round
6. Rules determine whether the user moves up, down, or stays

---

## Key Points

### Integrated Flow

Validation and progression now happen together.

Each answer affects:

* Accuracy (used for progression)
* Tags (used for future analysis)

---

### Adaptive Test

The number of questions adjusts dynamically:

* High accuracy → fewer questions
* Uncertain results → more questions
* Low accuracy → level adjustment

This makes the test faster without losing precision.

---

### State Reset

When the level changes, performance data is reset
to ensure each level is evaluated independently.

---

## Impact

* Converts the system into a fully functional test engine
* Enables real-time adaptive behavior
* Connects data collection with progression logic

---

## Limitations

* No diagnostic generation yet
* Tags are not interpreted
* No integration with the behavioral engine

---

## Key Insight

The main advancement in Version 4 is system integration.

By combining validation and progression into a single flow,
the system becomes capable of real interaction and adaptive behavior.
