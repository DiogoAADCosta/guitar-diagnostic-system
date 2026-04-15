# Version 7 - Attempted Connector Abstraction

## Goal

Attempt to reduce code repetition by abstracting sentence connector logic into reusable functions.

---

## What Changed

- Introduced functions to handle sentence connectors  
- Attempted to centralize connector selection logic  
- Replaced part of the conditional connector logic with function calls  
- Added debug statements to track connector behavior  
- Combined function-based logic with existing conditional structure  

---

## How It Works

This version attempts to abstract connector logic into reusable functions.

Part of the sentence construction is handled by functions,  
while the remaining cases still rely on conditional logic.

---

## Impact

- Introduces an attempt at reducing repetition through abstraction  
- Highlights challenges related to state management in functions  
- Does not provide consistent improvement over Version 6
- Helps clarify limitations of the current architecture  

---

## Limitations

- Connector counters do not update outside function scope  
- Abstraction does not work reliably in the current design  
- Code complexity increased due to abstraction challenges
- System becomes hybrid (functions + manual logic)  

---

## Key Insight

Not all abstractions improve a system.

When state is not properly managed,  
attempting to simplify logic can introduce more complexity than it removes.

This version represents the step:

Working implementation → Failed abstraction attempt → Deeper understanding of system behavior

---

## Note

This version is not used as the base for further development.

Development continues from Version 6, which provides a more stable and predictable implementation.

The issue identified here is related to state management within the current structure,  
and does not imply that a function-based approach is inherently invalid —  
only that a working solution was not achieved in this version.
