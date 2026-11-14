# Problem: POS Machine

import pandas as pd

class POSMachine:
    
    def __init__(self):
        self.__priceListofProducts__ = []
        self.__StartUpSystemforWelcomeFunc__ = True
        self.__fullTransactionList__ = []
        
        """
        Initialize the fields.
        
        Make sure that the last line of this method is the following:
        self.start()
        """
        self.start()
        
        
    
    def start(self):
        """
        Update this looping interface.
        Make sure that it follows the instructions completely.
        """
        FinalDecision = False
        self.printWelcomeMessage()
        self.printAllOptions()
        try:
            inp = int(input())
            while True:
                try:
                    if inp == 1:
                        self.setPriceList()
                    elif inp == 2:
                        self.printPriceList()
                    elif inp == 3:
                        self.makeNewTransaction()
                    elif inp == 4:
                        while True:
                            inpExit = input("Are you sure you want to Exit: (Y/N) ")
                            if inpExit.upper() == "Y":
                                FinalDecision = True
                                break
                            elif inpExit.upper() == "N":
                                break
                            else:
                                continue
                    if FinalDecision == True:
                        break
                    self.printAllOptions()
                    inp = int(input())
                except:
                    continue
        except:
            self.start()
    
            

        

                
    def printWelcomeMessage(self):
        if self.__StartUpSystemforWelcomeFunc__ == True:
            print("Welcome to the Point of Sales program")
            print("You will be able to seamlessly track and process sales transactions for each product in your business")
            print("_________________________________________________________________________________")
            self.__StartUpSystemforWelcomeFunc__ = False
        
        # """
        # Print a welcome message for the user.
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
            
    def printAllOptions(self):
        # Print all actions the user can do
        print("What do you want to do today? (input the number)")
        print("1 - Set the price list")
        print("2 - Show the price list")
        print("3 - Make a new transaction")
        print("4 - Close the POS machine")
    
    def setPriceList(self):
        print("setPricelist")
        
        
        # """
        # Load the price list from the provided file.
        # The program should send a warning if the provided file
        # is invalid.
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
    
    def printPriceList(self):
        print("printPriceList")
        # """
        # Print the current price list
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
    
    def makeNewTransaction(self):
        print("makeNewTransaction")
        # """
        # Create a new transaction.
        # Have the user add products (given a quantity >= 1).
        # When the user inputs a blank, print the invoice.
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
         
    
    def addProductToTransaction(self, productID, quantity):
        print("H")
        
        # """
        # Calculate the price for the given product and quantity
        # and add this to the current invoice
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
    def createSalesInvoice(self):
        print("createSalesInvoice")
        # """
        # Print (into the console) the sales invoice, detailing
        # the price and quanity of the products purchased, and
        # the total amount.
        
        # Save the same print output as a .txt file.
        
        # Remove/delete the "pass" keyword  below.
        # """
        # # Add your code here
        # pass

Account1 = POSMachine()