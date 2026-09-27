# TaxCalc

A small command-line tool that compares India's Old and New income tax regimes for a given income, and tells you which one saves you more money.

Built as a project for CSE1021 (Introduction to Problem Solving and Programming).

## What it does

- Takes your gross annual income, and (for the old regime) your deductions under 80C, 80D and HRA
- Calculates tax under both the old and new regimes using the current slab rates
- Applies the Section 87A rebate for both regimes
- Adds the 4% health & education cess
- Tells you which regime is cheaper for you, and by how much

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

Split up mainly to keep each file focused on one job: `config.py` holds the slab rates and constants in one place, `core/` does the actual tax math, and `utils/` handles input validation and printing the report.

## Running it

No external packages needed, just Python 3.

```bash
python main.py
```

Enter your gross income when prompted (or 0 to quit), then your deductions, and it prints a side-by-side comparison.

## Notes / assumptions

- Slab rates and the standard deduction (₹75,000) are hardcoded in `config.py` for the current assessment year — they'd need updating if the rates change.
- Deductions (80C, 80D, HRA) only apply under the old regime, per the actual rules.
- 80C is auto-capped at ₹1,50,000 if you enter more than that.
- This is a simplified calculator built for learning purposes. It doesn't cover every deduction, surcharge, or edge case in the real tax code, so please don't use it to actually file your taxes.

## Testing I did

Ran it manually with a few cases to sanity-check the logic:
- Negative income → rejected, asks again
- Non-numeric input (like "12Lakhs") → rejected, asks again
- 80C entered above ₹1,50,000 → gets capped automatically
- A few different income levels → both regimes calculate and the comparison picks the right one

---
**Name:** AJAY PATEL
**Register Number:** 26BCE10594
**Course:** CSE1021 – Introduction to Problem Solving and Programming
**Institution:** VIT University
