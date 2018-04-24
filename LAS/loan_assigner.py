from load_data import *
from save_data import *

'''
Generates ineligible tokens
ineligible_token:
A string describing bank and facility that cannot grant the loan,

Format: 
    '<bank_id>-<facility_id>' 
    or 
    '<bank_id>'(if any facility of the bank cannot grant the loan)
'''
def ineligible_facilities_tokens(covenants, loan):
    ineligible_tokens = []
    for covenant in covenants:
        if (covenant.banned_state == loan.state or
                covenant.max_default_likelihood < loan.default_likelihood):
            token = str(covenant.bank_id)
            if covenant.facility_id is not None:
                token += '-{}'.format(covenant.facility_id)
            ineligible_tokens.append(token)
    return ineligible_tokens

def calculate_yield(loan, facility):
    return round((1 - loan.default_likelihood) * loan.interest_rate * loan.amount
                                   - loan.default_likelihood * loan.amount
                                   - facility.interest_rate * loan.amount)

'''
Assign a facility to the loan
'''
def assign_facility(loan, facilities, covenants):
    max_yield = 0
    max_yield_facility = None
    assignment_details = {}

    ineligible_tokens = ineligible_facilities_tokens(covenants, loan)
    for facility in facilities:
        # check if facility cannot grant loan due to covenants
        # and calculate expected yield for the <loan>
        if not (facility.bank_id in ineligible_tokens or
                facility.token() in ineligible_tokens or
                facility.remaning_amount < loan.amount):
            expected_yield = calculate_yield(loan, facility)

            if max_yield < expected_yield:
                max_yield = expected_yield
                max_yield_facility = facility

            # To order facilities when the yield is same
            # if max_yeild == expected_yield and max_yeild_facility.remaning_amount > facility.remaning_amount:
            #     max_yeild_facility = facility

    max_yield_facility.grant_loan(loan.amount, max_yield)
    assignment_details['loan_id'] = loan.id
    assignment_details['facility_id'] = max_yield_facility.id

    return assignment_details



if __name__ == '__main__':
    # load data into objects
    # can be done in better way if we use a ORM with a DB
    # banks = load_banks()
    covenants = load_covenants()
    facilities = load_facilities()
    loans = load_loans()
    yields = []

    assignments = []
    for index, loan in enumerate(loans):
        loan_assignment = assign_facility(loan, facilities, covenants)
        assignments.append(loan_assignment)

    for facility in facilities:
        yields.append(
            {
                'facility_id' : facility.id,
                'expected_yield': int(facility.current_yield)
            })

    write_csv('assignments.csv', assignments)
    write_csv('yields.csv', yields)
