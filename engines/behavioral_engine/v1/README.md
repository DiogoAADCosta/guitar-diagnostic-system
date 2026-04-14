# Version 1 - Initial Structure

## Goal

The goal of this version is to build the basic execution flow of the test:

- Display questions
- Capture user input
- Associate answers with tags
- Store results in separate lists

## Key Decisions

- Tags are stored directly inside each answer
- The system separates:
  - "limitadores" (limitations)
  - "capacidades" (strengths)

## Problems Identified

- Tag structure is inconsistent (sometimes flat, sometimes nested)
- Logic becomes complex when handling multiple tags
- Code readability is reduced due to conditional checks

## Conclusion

This version works as a prototype, but reveals structural issues that need to be improved in future versions.
