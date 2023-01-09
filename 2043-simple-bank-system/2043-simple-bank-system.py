class Bank:
    bal = []
    
    def __init__(self, balance: List[int]):
        self.bal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1 < len(self.bal) and account2-1 < len(self.bal) and self.bal[account1-1] >= money:
            self.bal[account1-1] -= money
            self.bal[account2-1] += money
            return True
        else:
            return False
        
    def deposit(self, account: int, money: int) -> bool:
        if account-1 < len(self.bal):
            self.bal[account-1] += money
            return True
        else:
            return False
        
    def withdraw(self, account: int, money: int) -> bool:
        if account-1 < len(self.bal) and self.bal[account-1] >= money:
            self.bal[account-1] -= money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)