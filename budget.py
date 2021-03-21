class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def get_balance(self):
        funds = 0
        n = len(self.ledger)
        for i in range(n):
            funds = funds + self.ledger[i]['amount']
        return funds

    def check_funds(self, amount):
        funds = self.get_balance()
        if amount > funds:
            return False
        else:
            return True

    def deposit(self, funds, description=''):
        self.dep = dict()
        self.dep['amount'] = funds
        self.dep['description'] = description
        self.ledger.append(self.dep)
        return True

    def withdraw(self, amount, description=''):
        available = self.get_balance()
        if amount > available:
            return False
        else:
            self.w_draw = dict()
            self.w_draw['amount'] = -amount
            self.w_draw['description'] = description
            self.ledger.append(self.w_draw)
            print('in withdraw : ', amount, description, self.w_draw)
            return True

    def transfer(self, funds, category):
        cat = category.name
        a = self.withdraw(funds, f'Transfer to {cat}')
        b = category.deposit(funds, f'Transfer from {self.name}')
        if a:
            return True
        else:
            return False

    def get_withdrawls(self):
        withdrawl = 0
        for e in self.ledger:
            if e['amount'] < 0:
                withdrawl += e['amount']
        return withdrawl

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23} {self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        print(output)
        return output


def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier


def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())

    # Breakdown of spending rounded down to nearest 10th
    rounded = list(map(lambda x: truncate(x / total), breakdown))
    return rounded


def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = get_totals(categories)
    print('inside create spend chart', totals)
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
    return res.rstrip()+'  '
