class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']

        output = title + items + 'Total: ' + str(total)
        return output

    def deposit(self, amount, description=""):
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit must be a positive number")
        self.ledger.append({'amount':amount, 'description':description})
        
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def check_funds(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Check funds amount must be a positive number.")
        return self.get_balance() >= amount
    
    def withdraw(self, amount, description=''):
         if not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal must be a positive number")
         if self.check_funds(amount):
             self.ledger.append({'amount':-amount, 'description':description})
             return True
         return False


    def transfer(self, amount, category):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transfer must be a positive number")
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True  
        return False

    def get_withdrawls(self):
      total = 0
      for item in self.ledger:
          if item["amount"] < 0:
              total+= item["amount"]
      return total
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    """
    create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart
    """
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
          cat_spaces = " "
          for total in totals:
              if total * 100 >= i:
                  cat_spaces += "o  "
              else:
                  cat_spaces += "   "
          res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
          i-=10
      
    dashes = "-" + "---"*len(categories)
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
        
        if(x != len(maxi) -1 ):
          nameStr += '\n'

          
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res