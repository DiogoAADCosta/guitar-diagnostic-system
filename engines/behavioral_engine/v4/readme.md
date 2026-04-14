# Version 4 - Diagnostic Generation and Conditional Flow

## Goal

Generate a structured diagnosis based on user responses.

## What Changed

- Introduced a diagnostic system based on tag frequency
- Mapped tags to predefined descriptive messages
- Implemented dynamic generation of diagnostic text
- Added conditional question flow using 'skip_if'

## New Features

- Diagnosis generation (text output)
- Conditional question skipping based on previous answers
- Automatic inference of limitations when questions are skipped

## How It Works

1. User answers questions
2. Tags are collected and categorized
3. Tag frequency is calculated using Counter
4. Most frequent limitation and strength are identified
5. Tags are mapped to predefined diagnostic messages
6. A final diagnostic is generated dynamically
7. Additional signals may add extra feedback

## Impact

- System evolves from analysis to interpretation
- Produces human-readable feedback
- Introduces adaptive behavior (dynamic flow)

## Limitations

- Diagnosis is based only on most frequent tags
- No weighting between different signals
- Limited combination logic between multiple factors

## Key Insight

Once data is structured and measurable,  
it becomes possible to translate patterns into consistent, rule-based feedback.

This version marks the transition from data analysis to user-facing interpretation.
