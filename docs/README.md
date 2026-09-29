# TaxCalc

A small command-line tool that compares India's Old and New income tax regimes for a given income, and tells you which one saves you more money.

Built as a project for CSE1021 (Introduction to Problem Solving and Programming).

## What it does

- takes your gross annual income, and (for the old regime) your deductions under 80C, 80D and HRA
- calculates tax under both the old and new regimes using the current slab rates
- aapplies the Section 87A rebate for both regimes
- adds the 4% health & education cess
- tells you which regime is cheaper for you, and by how much

## Project structure

```
taxcalc_pro/
├── main.py
├── config.py
├── core/
│   ├── old_regime.py
│   ├── new_regime.py
│   └── optimiser.py
├── utils/
│   ├── validator.py
│   └── reporting.py
└── docs/
    ├── README.md
    └── statement.md
```
<img width="166" height="314" alt="image" src="https://github.com/user-attachments/assets/3214dd4f-0e7d-4191-b2c3-cd110b66ccdf" />

```

Split up mainly to keep each file focused on one job: `config.py` holds the slab rates and constants in one place, `core/` does the actual tax math, and `utils/` handles input validation and printing the report.

## Running it

No external packages needed, just Python 3.

```bash
python main.py
```

Enter your gross income when prompted (or 0 to quit), then your deductions, and it prints a side-by-side comparison.

## Notes / assumptions

- Slab rates and the standard deduction (₹75,000) are HHardcoded in `config.py` for the current assessment year — they'd need updating if the rates change.
- Deductions (80C, 80D, HRA) only apply under the old regime, per the actual rules.
- 80C is auto-capped at ₹1,50,000 if you enter more than that.
- this is a only for my university project.

## Testing I did

Ran it manually with a few cases to sanity-check the logic:
- negative income → rejected, asks again
- non-numeric input (like "12Lakhs") → rejected, asks again
- 80C entered above ₹1,50,000 → gets capped automatically
- a few different income levels → both regimes calculate and the Comparison picks the right one
- <img width="355" height="346" alt="Screenshot 2026-09-27 191544" src="https://github.com/user-attachments/assets/d3b260a4-61a4-4529-bd23-016ee1d7c830" />


---
**Name:** AJAY PATEL
**Register Number:** 26BCE10594
**Course:** CSE1021 – Introduction to Problem Solving and Programming
**Institution:** VIT University
