# Report Generator

Write a function named `build_report(records)` that turns a list of records into a summary report.

## Requirements
- Each record is a dictionary with at least `"name"` and `"score"` keys.
- Return a dictionary with:
  - `"total"`: the sum of all scores
  - `"average"`: the average score
  - `"top_student"`: the name with the highest score

## Example
```python
build_report([
    {"name": "Ana", "score": 90},
    {"name": "Ben", "score": 85},
])
# -> {"total": 175, "average": 87.5, "top_student": "Ana"}
```
