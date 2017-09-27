"""
Clean and Powerful program to manage Monthly, Per-Paycheck, and Financial Goals.
"""
from datetime import datetime, timedelta
import os
import sys

#########################
# ENHANCEMENTS
# 1. Use ordered dict for bills and print them out in order of date.
# 2.
#########################

PAYCHECK_AMOUNT = 1700
file = 'thisPaycheckBudget.csv'

def main():
   input = raw_input("Enter paycheck date in mm/dd/yy format:")
   dateString = input.split('/')
   paycheckDate_datetime = datetime(2000 + int(dateString[2]),int(dateString[0]) , int(dateString[1]))

   # build next paycheck datetime object
   nextPaycheck_datetime = paycheckDate_datetime + timedelta(14)

   monthlyBills = monthlyBillsThisPaycheck(paycheckDate_datetime, nextPaycheck_datetime)
   printToFile(monthlyBills, paycheckDate_datetime, nextPaycheck_datetime)

   # open the completed file
   os.startfile(file)


class Bill(object):
   def __init__(self, name, cost):
      self.name = name
      self.cost = cost


   def printInfo(self, file):
      '''
      Print object info to terminal and output file.

      :param file: Output file to output .csv data to.
      :return: None
      '''
      print 'Name : {name}, Cost = {cost}'.format(name=self.name, cost=self.cost)
      file.write(self.name + ',' + str(self.cost) + '\n')


class PaycheckBill(Bill):
   def __init__(self, name, cost):
      super(PaycheckBill, self).__init__(name, cost)


class MonthlyBill(Bill):
   def __init__(self, name, cost, dayOfMonthDue):
      super(MonthlyBill, self).__init__(name, cost)
      self.dayOfMonthDue = dayOfMonthDue
      self.dayOfMonthDue_datetime = None


   def printInfo(self, file):
      '''
      Overridden method - Print object info to terminal and output file.

      :param file: Output file to output .csv data to.
      :return: None
      '''
      print 'Due Date: {date} Name : {name}, Cost = {cost}'.format(date=self.dayOfMonthDue, name=self.name, cost=self.cost)
      info = [self.name, str(self.cost), datetimeToString(self.dayOfMonthDue_datetime)]
      file.write(','.join(info) + '\n')


perPaycheckBills = [PaycheckBill(name='Car Payment', cost=138.8),
                    PaycheckBill(name='Periodic Expenses', cost=125),
                    PaycheckBill(name='Savings', cost=150),
                    # PaycheckBill(name='Home Improvements', cost=0),
                    PaycheckBill(name='Extra Student Loan Payment', cost=137.5),
                    # PaycheckBill(name='Savings', cost=138.8),
                    ]


monthlyBills = [MonthlyBill(name='Taxes & Heat', cost=400, dayOfMonthDue=1),
                MonthlyBill(name='Home Owners Insurance', cost=30, dayOfMonthDue=10),
                MonthlyBill(name='Comcast', cost=80, dayOfMonthDue=14),
                MonthlyBill(name='HBO', cost=15, dayOfMonthDue=25),
                MonthlyBill(name='Headspace', cost=13, dayOfMonthDue=25),
                MonthlyBill(name='Spotify', cost=15, dayOfMonthDue=20),
                MonthlyBill(name='Nelnet', cost=360, dayOfMonthDue=28),
                MonthlyBill(name='Verizon', cost=85, dayOfMonthDue=28),
                MonthlyBill(name='Amica', cost=15, dayOfMonthDue=28),
                # MonthlyBill(name='Comcast', cost=80, dayOfMonthDue=14),
                # MonthlyBill(name='Comcast', cost=80, dayOfMonthDue=14),
                ]


def datetimeToString(date):
   '''
   Convert datetime to string object and return in mm/dd/yyyy format.

   :param date: Datetime object.
   :return: String in mm/dd/yyyy format for datetime object.
   '''

   return '/'.join([str(date.month), str(date.day), str(date.year)])


def monthlyBillsThisPaycheck(paycheckDate, nextPaycheck):
   '''
   Return monthly bills that fall between paycheck date and 14 days after paycheck date.

   :param paycheckDate: Must be of type datetime.
   :return: List of bills coming out of this paycheck.
   '''
   monthlyBillsThisPaycheck = []

   for i in monthlyBills:
      # create datetime object for each bill due date
      if i.dayOfMonthDue >= paycheckDate.day :
         i.dayOfMonthDue_datetime = datetime( paycheckDate.year, paycheckDate.month, i.dayOfMonthDue )
      else:
         i.dayOfMonthDue_datetime = datetime( paycheckDate.year, paycheckDate.month + 1, i.dayOfMonthDue )

      # check bill due date against this paycheck time window
      if paycheckDate <= i.dayOfMonthDue_datetime <= nextPaycheck:
         monthlyBillsThisPaycheck.append(i)

   return monthlyBillsThisPaycheck


def printToFile(monthlyBills, paycheckDate, nextPaycheck):
   '''
   Output contents of .csv file.

   :param monthlyBills: List of monthly bills.
   :param paycheckDate: paycheck date (datetime).
   :param nextPaycheck: next paycheck date (datetime).
   :return: None
   '''
   with open(file, 'w') as f:  # Note: 'a' - append to file. 'w' - overwrite.
      # If file is not empty, add 2 returns for formatting
      firstLine = True
      if os.stat("thisPaycheckBudget.csv").st_size > 10:
         firstLine = False
      if not firstLine:
         print '\n\n'

      # print paycheck dates and amount
      paycheckDate_string = datetimeToString(paycheckDate)
      nextPaycheck_string = datetimeToString(nextPaycheck)
      row1 = ['Paycheck Dates:', paycheckDate_string, nextPaycheck_string]
      f.write(','.join(row1) + '\n\n')

      # print summary
      f.write('Leftover,=B4-B5\n')
      f.write('Paycheck Amount,' + str(PAYCHECK_AMOUNT) + '\n')
      f.write('Total Bills,=SUM(B11:B50)\n\n')

      # print per paycheck bills
      f.write('Per Paycheck Bills,Cost\n')
      for bill in perPaycheckBills:
         bill.printInfo(f)

      f.write('\nMonthly Bills,Cost,Due Date\n')

      # print monthly bills
      for bill in monthlyBills:
         bill.printInfo(f)


if __name__ == '__main__':
   main()
