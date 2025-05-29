class Bank:
    bank_name = "Alfalah"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def show_bank_name(self):
        print(f"Bank name is {self.bank_name}")

bank_1 = Bank()
bank_1.show_bank_name()
bank_1.change_bank_name("HBL")
bank_1.show_bank_name()