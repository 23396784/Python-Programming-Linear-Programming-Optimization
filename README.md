# Results Directory

This directory contains output files from the analysis.

## Part 1: Python Programming Results

### String Operations
- Input: `s225187913`
- Reversed: `['3', '1', '9', '7', '8', '1', '5', '2', '2', 's']`

### Array Analysis (Student ID: s225187913)
| Metric | Result |
|--------|--------|
| Digits | [2, 2, 5, 1, 8, 7, 9, 1, 3] |
| Maximum | 9 at index 6 |
| Second Maximum | 8 |
| Distinct Digits | [2, 5, 1, 8, 7, 9, 3] |
| Distinct Count | 7 |
| Smaller Counts | [2, 2, 5, 0, 7, 6, 8, 0, 4] |

### 3MT Competition Results
| Rank | Student | Score |
|------|---------|-------|
| 1 | Andrew | 68.6/100 |
| 2 | Kelvin | 64.4/100 |
| 3 | Lily | 51.1/100 |
| 4 | Dina | 50.2/100 |
| 5 | Thomas | 6.3/100 |

### Magic Coins Generator
| Target | Steps | Solution |
|--------|-------|----------|
| 5 | 3 | M2(0→2), M2(0→2), M1(0→1) |
| 10 | 5 | 5× M2(0→2) |
| 17 | 9 | 8× M2(0→2), M1(0→1) |

## Part 2: Linear Programming Results

### Problem Formulation
```
Maximize:   Z = 3A + 4B
Subject to: A + 2B ≤ 14
            B ≥ 3
            A, B < 15
            A ≥ 0
```

### Optimal Solution
| Metric | Value |
|--------|-------|
| Product A | 8 units |
| Product B | 3 units |
| Maximum Revenue | $36 |

### Feasible Region Summary
- Total feasible integer solutions: 25
- Revenue range: $12 to $36
- Binding constraints: A + 2B = 14, B = 3

### Constraint Verification
| Constraint | Expression | Status |
|------------|------------|--------|
| Transportation | 8 + 2(3) = 14 ≤ 14 | ✓ BINDING |
| Minimum B | 3 ≥ 3 | ✓ BINDING |
| Maximum A | 8 < 15 | ✓ Slack |
| Maximum B | 3 < 15 | ✓ Slack |
| Non-negativity | 8 ≥ 0 | ✓ Slack |

## Visualization Files
- `lp_feasible_region.png` - Feasible region plot with optimal point
- `silhouette_analysis.png` - (If clustering included)
