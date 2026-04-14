# Guitar Diagnostic System — Version 5

For a detailed breakdown, see [README_v5_detailed.md](./README_v5_detailed.md)

## Overview

A rule-based diagnostic system that analyzes guitar students' responses and generates structured feedback based on their technical limitations and strengths.

This version introduces a hybrid approach combining statistical analysis with pattern-based classification.

---

## Key Features

* Multi-signal analysis (handles ties in dominant tags)
* User level classification (Beginner, Intermediate, Advanced)
* Profile-based diagnosis (pattern recognition)
* Conditional question flow
* Support for multiple answers
* Dynamic and human-readable feedback

---

## How It Works

1. User answers a set of questions
2. Responses are converted into tags (limitations and capabilities)
3. Tag frequency is analyzed
4. Dominant signals are identified
5. System attempts to match a predefined profile
6. If no match is found, fallback diagnostic logic is applied
7. Additional signals are appended to the final feedback

---

## Why This Matters

Instead of relying on a single dominant issue, the system considers multiple signals simultaneously, producing more realistic and consistent diagnoses.

---

## Next Steps

* Introduce weighted scoring
* Expand profile system
* Convert into API
* Integrate with frontend

---

## Note

This project represents the transition from simple rule-based analysis to a more structured diagnostic engine inspired by real teaching experience.
