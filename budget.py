class Category:
    def __init__(self, name):
        self.name = name
        self.account = list()

    def get_balance(self):
        funds = 0
        n = len(self.account)
        for i in range(n):
            funds = funds+self.account[i]['amount']
        return funds


    def deposit(self, funds, description=''):
        self.dep=dict()
        self.dep['amount'] = funds
        self.dep['description'] = description
        self.account.append(self.dep)

    def withdraw(self, amount, description=''):
        available = self.get_balance()
        if amount > available:
            return
        else:
            self.withdraw = dict()
            self.withdraw['amount'] = -amount
            self.withdraw['description'] = description
            self.account.append(self.withdraw)

    def transfer(self, funds, category):
        cat = category.name
        a = self.withdraw(funds, f'Trasfer to {cat}')
        b = category.deposit(funds, f'Transfer from {self.name}')
        if a:
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.money)):
            items += f"{self.money[i]['description'][0:23]:23} {self.money[i]['amount']:>7.2f}" + '\n'
            total += self.money[i]['amount']

        output = title + items + "Total: " + str(total)
        return output

    def truncate(self, n):
        multiplier = 10
        return int(n * multiplier) / multiplier

    def get_totals(self, categories):
        total = 0
        breakdown = []
        for category in categories:
            total += category.get_withdrawls()
            breakdown.append(category.get_withdrawls())

        # Breakdown of spending rounded down to nearest 10th
        rounded = list(map(lambda x: self.truncate(x / total), breakdown))
        return rounded

    def create_spend_chart(self, categories):
        res = "Percentage spent by category\n"
        i = 100
        totals = self.getTotals(categories)
        while i >= 0:
            cat_spaces = " "
            for total in totals:
                if total * 100 >= i:
                    cat_spaces += "o  "
                    # print(categories[totals.index(total)].name)
                else:
                    cat_spaces += "   "
        res += str(i).rjust(3) + "|" + cat_spaces + "\n"
        i -= 10
        dashes = "-" + "---" * len(categories)
        names = []
        x_axis = ""
        for category in categories:
            names.append(category.name)

        maxi = max(names, key=len)

        for x in range(len(maxi)):
            nameStr = '     '
            for name in names:
                if x >= len(name):
                    nameStr += "   "
                else:
                    nameStr += name[x] + "  "
            nameStr += '\n'
            x_axis += nameStr

        res += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
        return res
