has_high_income = True
has_good_credit = True

# Both conditions need to be True
if has_high_income and has_good_credit:
    print("Eligible for Loan")

# Only one condition need to be True
if has_high_income or has_good_credit:
    print("Eligible for Loan")