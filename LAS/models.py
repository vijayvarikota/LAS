class Bank:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

class Covenant():
    def __init__(self, data):
        self.bank_id = data['bank_id']
        self.facility_id = data['facility_id']
        self.max_default_likelihood = float(data['max_default_likelihood'] or 1)
        self.banned_state = data['banned_state']

class Facility():
    def __init__(self, data):
        self.id = data['id']
        self.bank_id = data['bank_id']
        self.interest_rate = float(data['interest_rate'])
        self.amount = float(data['amount'])
        self.remaning_amount = float(data['amount'])
        self.current_yield = 0

    def token(self):
        return str('{}-{}'.format(self.bank_id, self.id))

    def grant_loan(self, loan_amount, max_yield ):
        self.remaning_amount -= loan_amount
        self.current_yield += max_yield

class Loan():
    def __init__(self, data):
        self.id = data['id']
        self.amount = float(data['amount'])
        self.interest_rate = float(data['interest_rate'])
        self.default_likelihood = float(data['default_likelihood'] or 1)
        self.state = data['state']

