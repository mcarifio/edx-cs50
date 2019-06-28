#!/usr/bin/env python3

def payment_schedule(initial_balance, min_payment_rate_percent, monthly_interest_rate, periods):
    balance = initial_balance
    for p in range(periods):
        payment = min_payment_rate_percent * balance
        unpaid_balance = balance - payment
        interest = monthly_interest_rate * unpaid_balance
        print(balance, payment, unpaid_balance, interest)
        balance = unpaid_balance + interest

def final_balance(initial_balance, monthly_payment, monthly_interest_rate, periods):
    """
    Variant of payment_schedule above, no printing, returns the final balance
    :param initial_balance:
    :param monthly_payment:
    :param monthly_interest_rate:
    :param periods:
    :return:
    """
    balance = initial_balance
    for p in range(periods):
        unpaid_balance = balance - monthly_payment
        interest = monthly_interest_rate * unpaid_balance
        balance = unpaid_balance + interest
    return balance


def montly_interest_rate_of(annualInterestRate):
    """
    Convert the annual interest rate into a monthly one.
    :param annualInterestRate:
    :return:
    """
    return float(annualInterestRate) / 12


def payoff_simulation(initial_balance, annualInterestRate, periods):
    """
    Try various monthly payments and see if you can get close to a negative balance after 12 payments without paying too much.
    :param initial_balance:
    :param annualInterestRate:
    :param periods:
    :return:
    """
    monthly_interest_rate = montly_interest_rate_of(annualInterestRate)
    iterations = 10
    previous_monthly_payment_guess = float(initial_balance) / periods
    monthly_payment_guess = float(1.3 * initial_balance) / periods # guess a little high
    for i in range(iterations):
        payback = final_balance(initial_balance, monthly_payment_guess, monthly_interest_rate, periods)
        if payback < 0 and payback > -monthly_payment_guess:
            return monthly_payment_guess

        if payback < 0:
            # paying too much
            monthly_payment_guess = (monthly_payment_guess + previous_monthly_payment_guess) / 2
        else:
            # paying too little
            previous_monthly_payment_guess = monthly_payment_guess
            monthly_payment_guess = 1.1 * monthly_payment_guess

    print("Didn't converge on an answer after " + iterations + " iternations.")
    return None

def payoff_calculation(initial_balance, annualInterestRate, periods):
    """
    https://brownmath.com/bsci/loan.htm#LoanPayment Calculate the exact payment
    :param initial_balance:
    :param annualInterestRate:
    :param periods:
    :return:
    """
    monthly_interest_rate =  montly_interest_rate_of(annualInterestRate)
    numerator = initial_balance * monthly_interest_rate
    denominator = 1 - pow(1 + monthly_interest_rate, -periods)
    return numerator / denominator





if __name__ == "__main__":
    initial_balance = 5000
    min_payment_rate_percent = 0.02
    annual_interest_rate = 0.18
    year_in_months = 12
    monthly_interest_rate =  annual_interest_rate / year_in_months
    # print(initial_balance, min_payment_rate_percent, monthly_interest_rate)
    # payment_schedule(initial_balance, min_payment_rate_percent, monthly_interest_rate, 12)
    print(payoff_calculation(initial_balance, annual_interest_rate, year_in_months))
    print(payoff_simulation(initial_balance, annual_interest_rate, year_in_months))
