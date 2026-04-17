# Version 9 — Context-Based Test Execution

## Overview

Version 9 extends the test pipeline by implementing
the first functional version of the context-based evaluation stage.

The system now moves beyond interface validation
and begins evaluating performance within specific musical contexts.

---

## What Changed

In Version 8, the system introduced a structural separation between:

- Interface evaluation  
- Context-based evaluation (planned)

Version 9 implements this second stage.

---

## Context-Based Evaluation

The system now evaluates user responses within predefined contexts, such as:

- power_chords  
- triades_simples  

For each context, the test:

- Filters relevant questions  
- Collects answers and associated tags  
- Stores results both:
  - Globally  
  - Per context  

---

## Key Behavior

- The test currently evaluates one context per execution  
- Context selection is fixed (first in the list)  
- No progression between contexts is implemented yet  

---

## Key Insight

With the introduction of context-based evaluation,
the system begins to associate user performance
with specific musical situations.

This is a necessary step toward meaningful diagnostic interpretation.

---

## Scope

This version includes:

- Functional context-based test execution  
- Context filtering logic  
- Structured data collection (interface + context + tags)  

This version does not include:

- Context progression logic  
- Multi-context evaluation in a single run  
- Diagnostic interpretation  

---

## Key Takeaway

Version 9 marks the transition from structural design
to functional execution of context-based evaluation.

The system now collects more structured and meaningful data,
aligned with the intended diagnostic model.
