# Problem Statement

India currently runs two personal income tax regimes in parallel: the old regime, which rewards itemised deductions like 80C and HRA, and the new regime, which has lower slab rates but no deductions. Figuring out which one actually results in less tax isn't obvious just by looking at the slabs — it depends on income level and how much someone can actually claim in deductions.

Doing this by hand, or with one unstructured script, gets messy fast and is easy to get wrong, especially with progressive slabs where different portions of income are taxed at different rates.

## What this project sets out to do

- Calculate tax under both regimes for the same income, so they can be compared directly
- Handle the progressive slab structure without hardcoding a long chain of if/elif statements
- Validate user input so bad data (negative numbers, text, etc.) doesn't crash the program
- Apply the caps and rebates that actually affect the numbers, like the 80C limit and the Section 87A rebate
- Recommend whichever regime results in lower tax, along with the reasoning

## Who this is for

- Someone who wants a quick, offline way to compare the two regimes for their own income
- Anyone reviewing this as a course project, to see how the logic and code are structured

## Design choices

- Slab data is stored as a list of dictionaries rather than hardcoded conditionals, so adding or adjusting a slab later doesn't mean rewriting the calculation logic
- Old and new regime calculations live in separate modules since the rules genuinely differ (deductions apply to one, not the other)
- Input validation is centralized in one function so every numeric prompt goes through the same checks
