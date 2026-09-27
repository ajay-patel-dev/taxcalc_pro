#data of new 

import config


def calculate_new_regime_tax(gross_income):
    taxable_income = max(0.0, gross_income - config.STANDARD_DEDUCTION)

    tax = 0.0
    previous_limit = 0.0
    for slab in config.NEW_REGIME_SLABS:
        if taxable_income <= previous_limit:
            break
        taxed_in_this_slab = min(taxable_income, slab["limit"]) - previous_limit
        tax += taxed_in_this_slab * slab["rate"]
        previous_limit = slab["limit"]

    # Section 87A rebate under the new regime
    if taxable_income <= 1200000:
        tax = 0.0

    cess = tax * config.HEALTH_EDUCATION_CESS_RATE
    return {
        "taxable_income": taxable_income,
        "base_tax": tax,
        "cess": cess,
        "total_tax": tax + cess,
    }
