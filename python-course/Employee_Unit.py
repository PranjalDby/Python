import requests
class Employee_Unit :
    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    @property
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self,month):
        resp = requests.get(f"https://google.com/?q=facebook")
        if resp.ok:
            return resp.text
        
        else:
            return 'Bad Response'