import utils
import datetime

class BudgetGenerator(object):

   monthlyBillsThisPaycheck = []
   thisPaycheckBills = []
   totalOutgoing = 0

   def __init__(self, paycheckDate):
      self.paycheckDate = paycheckDate

   def totalOutgoing(self):
      if len(self.thisPaycheckBills) < 1:
         self.thisPaycheckExpenses()
      sum = 0
      for bill in self.thisPaycheckBills:
         sum += bill.amount
      self.totalOutgoing = sum

   def fillMonthlyBillsThisPaycheck(self):
      for bill in utils.monthlyBills:
         billDate = utils.buildBillDate(bill, self.paycheckDate)
         if (billDate >= self.paycheckDate) and (billDate <= utils.twoWeeksFromDate(self.paycheckDate)):
            self.monthlyBillsThisPaycheck.append(bill)

   def thisPaycheckExpenses(self):
      #populate this list if it hasn't been done already
      if len(self.monthlyBillsThisPaycheck) < 1:
         self.fillMonthlyBillsThisPaycheck()

      for bill in self.monthlyBillsThisPaycheck:
         self.thisPaycheckBills.append(bill)

      for bill in utils.perPaycheckBills:
         self.thisPaycheckBills.append(bill)

      for bill in utils.perPaycheckBudgets:
         self.thisPaycheckBills.append(bill)
         
      self.totalOutgoing()

def main():
   paycheckDate = utils.buildPaycheckDate()
   myBudget = BudgetGenerator(paycheckDate)
   #print myBudget.thisPaycheckBills







main()





# TODO: Ask for user input of amount in different accounts and output stats and info on bills. i.e. amount in savings for

# TODO: Make accompanying savings tracking spreadsheet

# TODO: Output "Transfer x amount to y account ...
#               x amont goes towards (monthly bill) ... for savings tracking spreadsheet
