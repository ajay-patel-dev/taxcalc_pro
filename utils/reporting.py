# output 

def print_structured_summary(gross, deductions, old_res, new_res, optimal):
    space = "=" * 60
    space2 = "-" * 60

    print(f"\n{space}")
    print("           TAX REGIME COMPARISON REPORT")
    print(space)
    print(f" Gross Annual Income        : ₹{gross:,.2f}")
    print(f" Total Deductions Claimed   : ₹{sum(deductions.values()):,.2f}")
    print(space2)
    print(" METRIC                     | OLD REGIME     | NEW REGIME")
    print(space2)
    print(f" Taxable Income             | ₹{old_res['taxable_income']:<13,.2f} | ₹{new_res['taxable_income']:<13,.2f}")
    print(f" Tax Before Cess            | ₹{old_res['base_tax']:<13,.2f} | ₹{new_res['base_tax']:<13,.2f}")
    print(f" Health & Education Cess    | ₹{old_res['cess']:<13,.2f} | ₹{new_res['cess']:<13,.2f}")
    print(space2)
    print(f" TOTAL TAX PAYABLE          | ₹{old_res['total_tax']:<13,.2f} | ₹{new_res['total_tax']:<13,.2f}")
    print(space2)
    print(" RECOMMENDATION")
    print(f"   Go with: {optimal['recommendation']}")
    print(f"   Why    : {optimal['rationale']}")
    print(f"{space}\n")
