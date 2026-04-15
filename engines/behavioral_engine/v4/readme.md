# Version 4 - Diagnostic Generation and Conditional Flow

## Goal

Generate a structured diagnosis based on user responses.

---

## What Changed

- Introduced a diagnostic system based on tag frequency  
- Mapped tags to predefined descriptive messages  
- Implemented dynamic generation of diagnostic text  
- Added conditional question flow using `skip_if`  

---

## New Features

- Human-readable diagnostic output  
- Conditional question skipping based on previous answers  
- Automatic inference of limitations when questions are skipped  

---

## How It Works

The most frequent tags are mapped to predefined messages,  
which are combined to generate a structured diagnostic.

Additionally, certain questions are skipped dynamically  
based on previous answers, avoiding redundant evaluation.

---

## Impact

- Moves from analysis to interpretation  
- Produces structured, user-facing feedback  
- Introduces adaptive behavior in the test flow  

---

## Limitations

- Diagnosis still depends on most frequent tags only  
- No weighting between different signals  
- Limited interaction between multiple factors  

---

## Key Insight

Once patterns can be identified,  
they can be translated into consistent, rule-based feedback.

This version marks the transition from:

Basic analysis → Structured diagnostic generation
