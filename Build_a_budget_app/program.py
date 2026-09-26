class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        success = False
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -(amount),
                'description': description
            })
            success = True
        return success

    def get_balance(self):
        total = 0

        for item in self.ledger:
            total += item["amount"]

        return total

    def transfer(self, amount, other):
        success = False
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            success = True
        return success
        
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            print("Insufficient funds")
            return False
    
    def __str__(self):
        left = (30 - len(self.name)) // 2
        right = 30 - len(self.name) - left 
        teks = f"{'*'* left}{self.name}{'*'* right}"
        for value in self.ledger:
            x = value['description'][:23]
            y = f"{value['amount']:.2f}"[:7]
            teks += f"\n{x:<23}{y:>7}"
        total = self.get_balance()
        teks += f"\nTotal: {total:.2f}"
        return teks

    def __len__(self):
        return len(self.name)


def create_spend_chart(categories):
    teks_all = "Percentage spent by category"
    spents = []
    spent_total = 0
    for category in categories:
        spent_per_category = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent_per_category += -(item["amount"])
        spent_total += spent_per_category

    for category in categories:
        spent_per_category = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent_per_category += -(item["amount"])
        percentage_per_category = spent_per_category/spent_total
        spents.append((percentage_per_category*100) // 10 * 10)

    for i in range (100,-10,-10):
        teks = f"{i:>3}| "
        for spent in spents:
            if i <= spent:
                teks += "o  " 
            else:
                teks += "   "
        teks_all += "\n" + teks

    teks = f"    {'---' * len(spents)}-"
    longest_category = max(categories, key=len).name

    for i in range(len(longest_category)): 
        teks += "\n     " 
        for category in categories:
            x = list(category.name)
            if i <= len(x)-1:
                teks += f'{x[i]}  '
            else:
                teks += '   '
    teks_all += '\n' + teks
    return teks_all


    


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(700, 'groceries')
clothing = Category('Clothing')
clothing.deposit(1000, 'initial deposit')
clothing.withdraw(200, 'groceries')
auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(100, 'groceries')
print(food)
print(clothing)
print(auto)


print(create_spend_chart([food, clothing, auto]))

