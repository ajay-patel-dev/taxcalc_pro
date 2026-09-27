# data of old 

import config


def calculate_old_regime_tax(gross_income, deductions):
    total_deductions = config.STANDARD_DEDUCTION + sum(deductions.values())
    taxable_income = max(0.0, gross_income - total_deductions)

    tax = 0.0
    previous_limit = 0.0
    for slab in config.OLD_REGIME_SLABS:
        if taxable_income <= previous_limit:
            break
        taxed_in_this_slab = min(taxable_income, slab["limit"]) - previous_limit
        tax += taxed_in_this_slab * slab["rate"]
        previous_limit = slab["limit"]

    # Section 87A rebate - no tax 
    if taxable_income <= 500000:
        tax = 0.0

    cess = tax * config.HEALTH_EDUCATION_CESS_RATE
    return {
        "taxable_income": taxable_income,
        "base_tax": tax,
        "cess": cess,
        "total_tax": tax + cess,
    }
