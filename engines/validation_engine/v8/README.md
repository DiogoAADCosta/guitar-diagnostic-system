# Version 8 — Interface-First Test Pipeline

## Overview

Version 8 introduces a structural change in how the test is built.

Instead of evaluating multiple dimensions at once,  
the system now separates the test into distinct stages, starting with a dedicated interface evaluation.

---

## What Changed

The main issue identified in Version 7 was not the analysis logic,  
but how the data was generated.

Each question was evaluating multiple dimensions simultaneously:

- Tags (capabilities and limitations)  
- Context  
- Interface  

This produced noisy and ambiguous data, making reliable diagnosis difficult.

---

## Solution

Version 8 restructures the test pipeline to isolate these dimensions.

### Stage 1 — Interface

A new dedicated stage evaluates only the user's ability to interpret different interfaces:

- Chord symbols (leitura_cifras)  
- Fretboard diagrams (diagrama_braco)  
- Tablature (leitura_tablatura)  

This stage includes:

- Complete and simplified test modes  
- Automatic fallback:
  - If the user fails the simplified test, the system switches to the complete version  
- Independent evaluation per interface  

---

### Stage 2 — Context + Tag (Next Step)

The second stage reuses the progression logic from previous versions,  
but with an important change:

- Instead of changing levels, the system changes context  

This allows the test to evaluate specific musical situations  
without mixing different dimensions in the same question.

⚠️ This stage is not implemented in Version 8 yet.
It is planned as the next step in the system evolution.

---

## Flow Design

The test flow was redesigned to support this separation.

👉 [Complete Flowchart](./dev_notes/complete_test_flowchart.png)
👉 [Interface Flowchart](./dev_notes/interface_test_flowchart.png)
👉 [Context Flowchart](./dev_notes/context_test_flowchart.jpg)

The new flow ensures:

- Clear separation between interface and content evaluation  
- Reduced noise in collected data  
- More reliable signals for future diagnostic interpretation  

---

## Key Insight

The problem was not in how the system analyzed data,  
but in how the data was structured.

By isolating each dimension of evaluation,  
the system becomes simpler, more precise, and easier to interpret.

---

## Scope

This version includes:

- Interface-based evaluation stage  
- Adaptive test behavior (simplified → complete fallback)  
- Structured question model  

This version does not yet include:

- Context-based stage implementation  
- Diagnostic interpretation  
- Final report generation  

---

## Key Takeaway

Version 8 marks the transition from a mixed evaluation model  
to a structured, stage-based test system.

This change lays the foundation for reliable diagnostic construction.
