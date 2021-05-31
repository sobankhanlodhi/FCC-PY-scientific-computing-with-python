class Category:

    def __init__(self, description):
        self.description = description
        self.ledger = []

    def __str__(self):
        ledger_str = (self.description).center(30, '*') + '\n'
        for entry in self.ledger:
            ledger_str =  ledger_str + ((entry["description"]).ljust(23))[:23] + str("{:.2f}".format(entry["amount"])).rjust(7) + "\n"
        ledger_str =  ledger_str + "Total: " + str(self.get_balance())
        return ledger_str

    #A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    def deposit (self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    #A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    def withdraw (self, amount, description=""):
        balance = self.get_balance()
        if balance >= amount:
            amount = amount * -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False   

    #A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance (self):
        balance = 0
        for entry in self.ledger:
            balance = balance + entry["amount"]
        return balance

    #A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer (self,amount,category):
        if self.check_funds(amount):
            self.withdraw (amount, ("Transfer to " + category.description))
            category.deposit (amount, ("Transfer from " + self.description))
            return True
        else:
            return False


    #A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    def check_funds (self, amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False
    
#Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart
def create_spend_chart(categories = []):
    cat_total_spend = {}
    cat_perc_spend = {}
    grand_total_spend = 0
    for category in categories:
        total = 0
        
        for entry in category.ledger:
            if entry["amount"] < 0:
                total = total + (entry["amount"] * -1)
        cat_total_spend[category.description] = total
        grand_total_spend += cat_total_spend[category.description]

    for category in categories:
        cat_perc_spend[category.description] = int((100 / grand_total_spend * cat_total_spend[category.description]) // 10) * 10


    counter = 100
    chart = "Percentage spent by category\n"
    while counter >= 0:
        chart = chart + (str(counter) + "|").rjust(4) + " "
        for category in categories:
            if cat_perc_spend[category.description] >= counter:
                chart = chart + "o  "
            else:
                chart = chart + "   "
        chart = chart + '\n'
        counter -= 10
    chart = chart + "    " + ("---" * len(categories)) + "-"
    
    loop = True
    counter = 0
    while loop == True:
        line = "\n     "
        checknamelength = False
        for category in categories:
            if len(category.description) >= counter + 1:
                line = line + category.description[counter] + "  "
                checknamelength = True
            else:
                line = line + "   "

        if checknamelength == False:
            loop = False
        else:
            chart = chart + line
        counter += 1
    return chart
