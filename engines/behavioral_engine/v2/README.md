# Version 2 - Standardized Tag Structure

## Goal

Improve data structure consistency and simplify tag processing logic.

## Data Model

Each answer contains a list of tags, where each tag follows the structure:

- [type, value]

All tags are stored as a list of pairs:

- [[type, value], ...]

Where:
- type → 'limitador' or 'capacidade'
- value → specific skill (e.g., 'ritmo', 'troca_de_acorde')

## What Changed

In Version 1, the tag structure was inconsistent:

- ['limitador', 'base']
- [['capacidade', 'ritmo'], ['capacidade', 'troca_de_acorde']]

In Version 2, the structure is fully standardized:

- All tags follow the same format
- All answers support multiple tags consistently

## Key Improvements

- Eliminated the need for index-based access (e.g., tag[i], tag[i][0])
- Simplified iteration using tuple unpacking:

  for tipo, tag in alternativa['tag']

- Removed conditional branching required to handle multiple formats

## Impact

- Code is more readable
- Logic is easier to reason about
- Data model is consistent and predictable
- Structure is more scalable for future features

## Comparison with Version 1

| Aspect | Version 1 | Version 2 |
|------|--------|--------|
| Data structure | Inconsistent | Standardized |
| Iteration | Index-based | Tuple unpacking |
| Complexity | High | Reduced |
| Readability | Low | Improved |

## Key Insight

The main issue in Version 1 was not the algorithm itself,  
but the inconsistency of the underlying data model.

By fixing the data structure, the logic naturally became simpler.
