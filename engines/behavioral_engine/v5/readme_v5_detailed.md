# Guitar Diagnostic System — Version 5

## Overview

Version 5 introduces a significant refinement in the diagnostic system by improving how user data is interpreted and transformed into meaningful feedback.

This version evolves from simple frequency-based analysis to a **hybrid diagnostic model**, combining statistical relevance with pattern recognition.

---

## Goal

Improve diagnostic accuracy by:

* Handling multiple dominant signals (ties in tag frequency)
* Introducing profile-based classification
* Providing more consistent and realistic feedback to the user

---

## What’s New in Version 5

### 1. Multiple Dominant Tags Handling

* The system no longer relies on a single most frequent tag
* It supports **ties**, allowing multiple dominant limitations and strengths
* This results in a more realistic representation of the user’s condition

---

### 2. User Level Classification

User level is now determined by comparing the number of:

* **Limitations**
* **Capabilities**

#### Logic:

* More limitations → `Beginner`
* Balanced → `Intermediate`
* More capabilities → `Advanced`

---

### 3. Profile-Based Diagnosis

A new classification layer was introduced using predefined profiles.

Each profile represents a **specific combination of dominant tags**, enabling more precise and contextual feedback.

#### Example profiles:

* **Balanced Player**
* **False Advanced**
* **Rhythm Blocked**

If a user matches a profile exactly, the system prioritizes this diagnosis.

---

### 4. Hybrid Diagnostic System

The system now follows this decision flow:

1. **Profile Matching**

   * If a known pattern is detected → use profile diagnosis

2. **Fallback Logic**

   * If no profile matches → use isolated tag-based analysis

---

### 5. Primary vs Secondary Signals

* **Primary Tags**
  Used to define the main diagnosis
  (`base`, `rhythm`, `chord switching`, `chord building`)

* **Secondary Tags**
  Treated as additional observations
  (`resistance`, `continuity`, `barre limitations`, etc.)

---

### 6. Conditional Question Flow

* Questions are dynamically skipped based on previous answers
* Example:

  * If the user does not know what a barre chord is → skip dependent questions
  * Automatically assumes a base limitation

---

### 7. Multiple Answer Support (Question 9)

* The system now supports **multiple selections**
* Each selected option contributes independently to the diagnostic tags

---

### 8. Natural Language Variation

* Level feedback includes multiple phrasing options
* A random variation is selected using `random.choice()`
* Prevents repetitive and robotic responses

---

## How It Works

1. User answers the questions
2. Tags are collected (limitations and capabilities)
3. Tag frequency is calculated using `Counter`
4. Most frequent tags are identified (including ties)
5. User level is determined
6. System attempts to match a predefined profile
7. If no profile matches → fallback diagnostic is generated
8. Additional signals are appended as complementary feedback

---

## Current Limitations

* No weighting between different types of signals
* Profile matching currently requires exact combinations (no partial matching).
* Diagnosis still depends on frequency rather than contextual depth
* No persistence or historical tracking of user progress

---

## Key Insight

> Once user data is structured and measurable,
> it becomes possible to translate patterns into meaningful feedback.

Version 5 represents the transition from:

* **Simple analysis → Structured interpretation**
* **Static logic → Adaptive diagnostic system**

---

## Next Steps (Future Improvements)

* Introduce weighted scoring system
* Improve profile flexibility (partial matches)
* Convert system into functions or API
* Integrate with front-end (JavaScript)
* Store user history for progress tracking

---

## Author’s Note

This version marks a major step toward building a **real diagnostic engine**, not just a questionnaire.

The system now reflects more closely how a human teacher would interpret a student’s strengths and weaknesses.
