class Account:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # public
        self._balance = balance     # protected
        self.__pin = pin            # private

class SavingsAccount(Account):
    def __init__(self, owner, balance, pin):
        super().__init__(owner, balance, pin)
    __pv=1234
    def show_info(self):
        print(self.owner)       # public — accessible
        print(self._balance)    # protected — accessible in child
        print(self._Account__pin) # mangling to access private data
        # print(self.__pin)       # AttributeError — private, not accessible


s = SavingsAccount("Risan", 5000, "0000")
s.show_info()
