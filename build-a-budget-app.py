class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        current_balance = 0
        for value in self.ledger:
            current_balance += value['amount']
        return current_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount
        #if self.get_balance() < amount:
        #    return False
        #return True

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for entry in self.ledger:
            description = entry['description'][:23]
            amount = f'{entry["amount"]:.2f}'[:7]
            items += f'{description:<23}{amount:>7}\n'

        total = f'Total: {self.get_balance():.2f}'
        return title + items + total

def create_spend_chart(categories):

    withdrawals = []
    total_withdrawals = 0
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += item['amount']
                total_withdrawals += item['amount']
        withdrawals.append(total)
    print(f'{withdrawals}\n')
    
    percentages = []
    for item in withdrawals:
        percentage = int((item/total_withdrawals)*100)
        percentages.append((percentage - (percentage % 10)))
    print(f'{percentages}\n')

    chart = 'Percentage spent by category\n'

    for i in range(100, -1, -10):
        chart += f'{i:>3}|'
        for item in percentages:
            if item >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    chart += ' '*4 + '-'*(3*(len(categories))+1) + '\n'
    
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += ' '*5
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + ' '*2
            else:
                chart += ' '*3
        if i != max_length -1:
            chart += '\n'

    return chart


    return chart



