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
        FileofProductList = input()
        try:
            if ".txt" in FileofProductList:
                ProductListFromTXT = open(FileofProductList, "r")
                ProductListAsList = ProductListFromTXT.readlines()
                ProductListRemovedLines = [x.replace("\n", "") for x in ProductListAsList]
                ProductList = [x.split("\t") for x in ProductListRemovedLines]
                ProductListFromTXT.close()

                self.__priceListofProducts__.clear()
                for x in ProductList:
                    if len(x) == 3:
                        self.__priceListofProducts__.append(x)

                
            elif ".csv" in FileofProductList:
                ProductListFromCSV = pd.read_csv(FileofProductList)
                ProductList = [ProductListFromCSV.columns.tolist()] + ProductListFromCSV.to_numpy().tolist()
                self.__priceListofProducts__.clear()
                for x in ProductList:
                    self.__priceListofProducts__.append(x)
            else:
                print("Invalid file type")
        except:
            print("File not found")

        print(self.__priceListofProducts__)
        
        
        
        
        # """
        # Load the price list from the provided file.
        # The program should send a warning if the provided file
        # is invalid.
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
    
    def printPriceList(self):
        if len(self.__priceListofProducts__) == 0:
            print("No list Inputted")
        else:
            for EachProduct in self.__priceListofProducts__:
                print("{0: <4} {1: <35} {2}".format(EachProduct[0], EachProduct[1], EachProduct[2]))
        print("printPriceList")
        # """
        # Print the current price list
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
        # pass
    
    def makeNewTransaction(self):
        #Work In progress
        if len(self.__priceListofProducts__) == 0 :
            print("List of Products in Empty")
        else:
            while True:
                ProductInputted = input()
                if ProductInputted == "":
                    break
                else:
                    ProductExist = False
                    for Eachproduct in self.__priceListofProducts__:
                        if (ProductInputted == str(Eachproduct[0])) and (ProductInputted != "ID"):
                            ProductExist = True
                            break
                    if ProductExist == True:
                        print(f"Product exists {ProductInputted}")
                    else:
                        print("product does not exist")
                

        # """
        # Create a new transaction.
        # Have the user add products (given a quantity >= 1).
        # When the user inputs a blank, print the invoice.
        
        # Remove/delete the "pass" keyword below.
        # """
        # # Add your code here
         
    
    def addProductToTransaction(self, productID, quantity):
        print("H")
        
        
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