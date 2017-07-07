import datetime

class Bill(object):
   def __init__(self, name, amount, periodic=False):
      self.name = name
      self.amount = amount
      self.periodic = periodic

class MonthlyBill(Bill):
   '''TODO: write in doc string'''

   def __init__(self, name, amount, dayOfMonth, auto, periodic=False):
      Bill.__init__(self, name, amount, periodic)
      self.dayOfMonth = dayOfMonth
      self.auto = auto
      self.periodic = periodic

perPaycheckBills = [Bill('Car Payment', 138.80),
                        Bill('Car Insurance', 50, periodic=True)]

perPaycheckBudgets = [Bill('Groceries', 100),
                          Bill('Gifts', 25, periodic=True),
                          Bill('Clothes', 40, periodic=True),
                          Bill('Barley', 30),
                          Bill('Eating Out', 75),
                          Bill('Savings', 100)]

monthlyBills = [MonthlyBill('Taxes and Heat', amount=425, dayOfMonth=1, auto=False),
                    MonthlyBill('Home Owners', amount=28, dayOfMonth=10, auto=False),
                    MonthlyBill('Comcast', amount=73, dayOfMonth=14, auto=False),
                    MonthlyBill('Netflix', amount=10, dayOfMonth=16, auto=True),
                    MonthlyBill('Spotify', amount=10, dayOfMonth=26, auto=True),
                    MonthlyBill('Nelnet', amount=350, dayOfMonth=28, auto=False),
                    MonthlyBill('Verizon', amount=82.14, dayOfMonth=28, auto=False),
                    MonthlyBill('Amica', amount=15, dayOfMonth=28, auto=True)]

def todaysDate():
   return datetime.datetime.now()

def twoWeeksFromDate(paycheckDate):
   return paycheckDate + datetime.timedelta(days=14)

def buildBillDate(bill, paycheckDate):
   if bill.dayOfMonth > paycheckDate.day:
      return datetime.date(paycheckDate.year, paycheckDate.month, bill.dayOfMonth)  # bill is in this month
   else:
      if paycheckDate.month == 12:  # if it's december, next month is also next year
         return datetime.date(paycheckDate.year + 1, 1, bill.dayOfMonth)   # bill is next month
      else:
         return datetime.date(paycheckDate.year, paycheckDate.month + 1, bill.dayOfMonth)

def buildPaycheckDate():
   validDate = False
   while not validDate:
      paycheckDate = raw_input("Enter Paycheck Date in form mm/dd/yy: ")

      try:
         paycheckMonth = paycheckDate.split('/')[0]
         paycheckDay = paycheckDate.split('/')[1]
         paycheckYear = '20' + paycheckDate.split('/')[2]
         builtDate = datetime.date(int(paycheckYear), int(paycheckMonth), int(paycheckDay))
      except:
         print "Invalid date entered."
      else:
         print "Valid date entered"
         validDate = True
   return builtDate


