
(base) C:\Users\Pal>python
Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 16:37:03) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...     def __init__(self, owner, balance):
...         self.owner = owner
...         self.balance = balance
...         self.rate = 0.01  # default interest rate = 1%
...
...     def setRate(self, new_rate):
...         """Set a new annual interest rate (as decimal, e.g., 0.08 for 8%)"""
...         self.rate = new_rate
...
...     def getExpectedInterest(self):
...         """Calculate yearly interest income with monthly compounding"""
...         # Formula: A = P * (1 + r/12)^12
...         future_balance = self.balance * ((1 + self.rate/12) ** 12)
...         interest_income = future_balance - self.balance
...         return interest_income
...

... # -----------------------------
... # Testing Problem 2
... # -----------------------------
... print("\n=== Bank Account Test ===")
... account = bankAccounts("John Smith", 1500)
... account.setRate(0.08)  # set interest rate to 8%
... interest = account.getExpectedInterest()
...
... print("Account Owner:", account.owner)
... print("Balance: $", account.balance)
... print("Rate:", account.rate * 100, "%")
... print("Expected interest income in 1 year: $", round(interest, 2))
...
What is 5 + 7? 12
Correct!
What is 9 - 3? 6
Correct!
What is 4 * 3? 12
Correct!

Your total score is: 3 out of 3

=== Bank Account Test ===
Account Owner: John Smith
Balance: $ 1500
Rate: 8.0 %
Expected interest income in 1 year: $ 124.5
>>>
