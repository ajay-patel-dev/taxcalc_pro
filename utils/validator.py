#some condion from income tax website 

def get_validated_float(prompt, min_val=0.0):
    """Keep asking until the user gives a usable number that isn't below min_val."""
    while True:
        raw = input(prompt).replace(",", "").strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a number (e.g. 850000).")
            continue

        if value < min_val:
            print(f"  That can't be less than {min_val}.")
            continue

        return value


def get_validated_deductions():
    print("\nNow your deductions (only used for the old regime):")
    sec_80c = get_validated_float("  Section 80C (SOME PREMIUM): ")
    sec_80d = get_validated_float("  Section 80D (health insurance premium): ")
    hra = get_validated_float("  HRA exemption: ")

    if sec_80c > 150000:
        sec_80c = 150000
        print("  (80C capped at the legal limit of ₹1,50,000)")

    return {"80C": sec_80c, "80D": sec_80d, "HRA": hra}
