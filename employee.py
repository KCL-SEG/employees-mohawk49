"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_type, amount, rate, commission_type, comm_amount, comm_rate):
        self.name = name
        self.salary_type = salary_type
        self.amount = amount
        self.rate = rate
        self.commission_type = commission_type
        self.comm_amount = comm_amount
        self.comm_rate = comm_rate

    def get_pay(self):
        pay = 0
        if self.salary_type == 'monthly':
            pay += self.amount
        elif self.salary_type == 'hourly':
            pay += self.amount * self.rate

        if self.commission_type == 'contract':
            pay += self.comm_amount * self.comm_rate
        elif self.commission_type == 'bonus':
            pay += self.comm_amount
        return pay

    def __str__(self):
        string = ''
        if self.salary_type == 'monthly':
            if self.commission_type == '':
                string = f'{self.name} works on a {self.salary_type} salary of {self.amount}.  Their total pay is {Employee.get_pay(self)}.'
            elif self.commission_type == 'contract':
                string = f'{self.name} works on a {self.salary_type} salary of {self.amount} and receives a commission for {self.comm_amount} contract(s) at {self.comm_rate}/contract.  Their total pay is {Employee.get_pay(self)}.'
            elif self.commission_type == 'bonus':
                string = f'{self.name} works on a {self.salary_type} salary of {self.amount} and receives a bonus commission of {self.comm_amount}.  Their total pay is {Employee.get_pay(self)}.'
        elif self.salary_type == 'hourly':
            if self.commission_type == '':
                string = f'{self.name} works on a contract of {self.amount} hours at {self.rate}/hour.  Their total pay is {Employee.get_pay(self)}.'
            elif self.commission_type == 'contract':
                string = f'{self.name} works on a contract of {self.amount} hours at {self.rate}/hour and receives a commission for {self.comm_amount} contract(s) at {self.comm_rate}/contract.  Their total pay is {Employee.get_pay(self)}.'
            elif self.commission_type == 'bonus':
                string = f'{self.name} works on a contract of {self.amount} hours at {self.rate}/hour and receives a bonus commission of {self.comm_amount}.  Their total pay is {Employee.get_pay(self)}.'
        return string

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000, 0, '', 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 100, 25, '', 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, 0, 'contract', 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 150, 25, 'contract', 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, 0, 'bonus', 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 120, 30, 'bonus', 600, 0)
