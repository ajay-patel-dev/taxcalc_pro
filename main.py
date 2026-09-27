import config
from utils.validator import get_validated_float, get_validated_deductions
from utils.reporting import print_structured_summary
from core.old_regime import calculate_old_regime_tax
from core.new_regime import calculate_new_regime_tax
from core.optimiser import evaluate_best_regime


def main():
    print("=" * 60)
    print(f" {config.APP_TITLE} v{config.VERSION} - Old vs New Regime Tax Comparison")
    print("=" * 60)

    while True:
        print("\nEnter 0 to exit.")
        gross_income = get_validated_float("Gross Annual Income (₹): ")

        if gross_income == 0.0:
            print("\nGoodbye!")
            break

        deductions = get_validated_deductions()

        old_regime_results = calculate_old_regime_tax(gross_income, deductions)
        new_regime_results = calculate_new_regime_tax(gross_income)

        optimization_profile = evaluate_best_regime(
            old_regime_results["total_tax"],
            new_regime_results["total_tax"],
        )

        print_structured_summary(
            gross_income,
            deductions,
            old_regime_results,
            new_regime_results,
            optimization_profile,
        )


if __name__ == "__main__":
    main()
