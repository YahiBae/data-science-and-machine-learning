def calculate_emi(principal, rate, years):
    months = years * 12
    monthly_rate = rate / 100 / 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi