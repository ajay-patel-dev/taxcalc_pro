# which is better(some normal calculation )

def evaluate_best_regime(old_tax, new_tax):
    
    difference = abs(old_tax - new_tax)

    if old_tax < new_tax:
        recommendation = "OLD REGIME"
        rationale = f"Your deductions bring the old regime lower by ₹{difference:,.2f}"
    elif new_tax < old_tax:
        recommendation = "NEW REGIME"
        rationale = f"The new regime works out cheaper by ₹{difference:,.2f}"
    else:
        recommendation = "EITHER"
        rationale = "Both regimes land on the same tax amount"

    return {"recommendation": recommendation, "rationale": rationale}
