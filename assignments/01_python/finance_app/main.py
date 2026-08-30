try:
    from finance_tools.tax import calculate_tax
    from finance_tools.loan import calculate_emi
except ModuleNotFoundError:  # pragma: no cover - fallback for repo-root execution
    import sys
    from pathlib import Path

    app_dir = Path(__file__).resolve().parent
    if str(app_dir) not in sys.path:
        sys.path.insert(0, str(app_dir))
    from finance_tools.tax import calculate_tax
    from finance_tools.loan import calculate_emi


def main():
    income = float(input("Enter your income: "))
    tax = calculate_tax(income)

    print("Tax:", tax)

    loan = float(input("Enter loan amount: "))
    rate = float(input("Enter interest rate: "))
    years = int(input("Enter loan years: "))

    emi = calculate_emi(loan, rate, years)

    print("Monthly EMI:", round(emi, 2))


if __name__ == "__main__":
    main()