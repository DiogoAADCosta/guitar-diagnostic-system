# Behavioral Engine

## Overview

The behavioral engine is responsible for interpreting user responses  
and transforming them into a structured diagnostic.

Instead of measuring technical execution directly,  
it analyzes patterns in how the user interacts with the instrument.

---

## Purpose

This engine translates subjective answers into structured signals,
allowing the system to identify strengths, limitations,  
and behavioral patterns in the player.

It acts as a translation layer between user perception  
and structured diagnostic output.

---

## How It Works

User responses are mapped to predefined tags representing  
capabilities and limitations.

These signals are analyzed and combined to identify dominant patterns,  
which are then interpreted into a diagnostic.

The system does not rely on a single signal,  
but on the relationship between multiple tags and patterns.

---

## Core Concepts

**Tags**  
Each answer is associated with one or more tags representing  
a specific capability or limitation.

**Signals**  
Tags are aggregated to reflect recurring patterns  
in the user's responses.

**Dominance**  
More frequent signals are treated as more relevant,  
while weaker signals are filtered out.

**Profiles**  
Specific combinations of signals may match predefined profiles,  
allowing more contextual and precise diagnostics.

**Fallback Logic**  
When no profile is matched, the system generates a diagnosis  
based on isolated signals.

---

## Output

The engine produces a structured, human-readable diagnostic that:

- Describes strengths and limitations  
- Explains cause-and-effect relationships  
- Adapts sentence structure for natural readability  

The output is designed to resemble how a teacher would explain  
the student's current stage and challenges.

---

## Design Philosophy

- **Focus on playing behavior**  
  Analyzes how the player behaves while playing,  
  such as losing timing, breaking continuity, or struggling to recover from mistakes.

- **Pattern-based interpretation**  
  Uses combinations of signals instead of isolated metrics.

- **Clarity in communication**  
  Prioritizes understandable and meaningful feedback  
  over raw data output.

- **Structured but flexible logic**  
  Combines rule-based analysis with contextual interpretation.

---

## Scope and Limitations

This engine:

- Does not analyze audio or real-time performance  
- Does not measure technical precision directly  
- Depends on the accuracy of user responses  

It is designed to interpret behavior,  
not to validate execution.

---

## Relationship with Other Modules

The behavioral engine works alongside other system components,
such as the validation engine, which is responsible for
collecting and validating user responses.

While the validation layer focuses on data collection,
the behavioral engine focuses on interpretation and pattern analysis.

---

## Evolution

This section highlights the main structural changes in the behavioral engine across versions.

### Pre-v007 (Early Development)
- Initial experiments with question flow and data collection
- No structured behavioral analysis yet

### v007 — Initial Diagnostic Attempt
- First implementation of pattern-based diagnostic
- Mixed evaluation dimensions (tags, context, interface)
- Results were inconsistent and difficult to interpret

### v008 — Structural Redesign
- Separation of evaluation stages
- Introduction of interface-first testing approach
- Foundation for clearer signal collection

### v009 — Context-Based Evaluation
- First implementation of context-based test execution
- Data collection structured per context
- No adaptive behavior yet

### v010 — Adaptive Flow Introduction
- Rule-based system for intermediate evaluation
- Dynamic control of question flow based on performance
- Adaptive behavior within a single context

### v011 — Multi-Context Evaluation and Level Progression
- Evaluation across multiple contexts within a level
- Aggregated performance used for decision-making
- Functional level progression system implemented
- Prepares structured data for future diagnostic interpretation
