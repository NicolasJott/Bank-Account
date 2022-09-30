class bank_account:
    def __init__(self,f_name,l_name,social,dob,deposit,account_number): #Intializes account data
        self.f_name = f_name
        self.l_name = l_name
        self.social = social
        self.dob = dob
        self.deposit = deposit
        self.account_number = account_number

    def set_name(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name

    def set_social(self,social):
        self.social = social

    def set_dob(self,dob):
        self.dob = dob

    def set_deposit(self,deposit):
        self.deposit = deposit

    def set_account_number(self,account_number):
        self.account_number = account_number

                
