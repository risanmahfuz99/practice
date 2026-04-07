# @property lets you access a method like an attribute — no parentheses needed.
# It gives you control over getting, setting, and deleting an attribute while keeping a clean interface.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # private by convention (_) makes it private

    @property
    def balance(self):          # GETTER — called when you READ
        return self._balance

    @balance.setter
    def balance(self, amount):  # SETTER — called when you WRITE
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount

    @balance.deleter
    def balance(self):          # DELETER — called when you DELETE
        print("Deleting balance...")
        del self._balance


# --- Usage ---

acc = BankAccount(1000)

print(acc.balance)    # 1000  ← calls getter
acc.balance = 1500    # ← calls setter (valid)
print(acc.balance)    # 1500

acc.balance = -500    # ← calls setter → raises ValueError
# ValueError: Balance cannot be negative!

del acc.balance       # ← calls deleter
# Deleting balance...