# Version 2 - Tracking Results and Tag Extraction

## Goal

Extend the validation system to track user performance  
and extract meaningful data from responses.

---

## What Changed

- Introduced counters for correct and incorrect answers  
- Added total question tracking  
- Implemented accuracy calculation  
- Started collecting capability and limitation tags from responses  

---

## How It Works

In addition to validating answers, the system now tracks:

- Number of correct answers  
- Number of incorrect answers  
- Total number of questions  

Each response also contributes associated tags:

- Correct answers → capability tags  
- Incorrect answers → limitation tags  

At the end, the system calculates overall accuracy  
and outputs both performance metrics and collected tags.

---

## Impact

- Moves from isolated validation to aggregated results  
- Enables tracking of user performance across multiple questions  
- Introduces structured data collection for future analysis  

---

## Limitations

- Tags are collected but not yet analyzed  
- No interpretation or diagnostic generation  
- No weighting between different types of tags  
- No integration with other modules  

---

## Key Insight

Validation alone is not enough.

By tracking results and collecting structured data,  
the system begins to transition from simple correctness checking  
to meaningful user analysis.
