# Problem: POS Machine

import pandas as pd

from tkinter import *
from tkinter.scrolledtext import ScrolledText



class POSMachine:
    
    def __init__(self):
        self.__priceListofProducts__ = []
        self.__fullTransactionList__ = [] # Records of all of the invoive
        self.__TransactionHistory__ = [] # records all of the products sold from self.__fullTransactionList__
        
        """
        Initialize the fields.
        
        Make sure that the last line of this method is the following:
        self.start()
        """

        
        
    
    # def start(self): # removed for now to not make it start
    #     """
    #     Update this looping interface.
    #     Make sure that it follows the instructions completely.
    #     """
    #     FinalDecision = False
    #     self.printWelcomeMessage()
    #     while True:
    #         try:
    #             self.printAllOptions()
    #             inp = int(input())
    #             if inp == 1:
    #                 self.setPriceList()
    #             elif inp == 2:
    #                 self.printPriceList()
    #             elif inp == 3:
    #                 self.makeNewTransaction()
    #             elif inp == 4:
    #                 while True:
    #                     inpExit = input("Are you sure you want to Exit: (Y/N) ")
    #                     if inpExit.upper() == "Y":
    #                         FinalDecision = True
    #                         break
    #                     elif inpExit.upper() == "N":
    #                         break
    #             elif inp == 5:
    #                 self.SalesReport()
    #             if FinalDecision == True:
    #                 break
    #         except:
    #             continue

    
            

        

                
    def printWelcomeMessage(self):
        print("Welcome to the Point of Sales program")
        print("You will be able to seamlessly track and process sales transactions for each product in your business")
        print("_________________________________________________________________________________")

            
    def printAllOptions(self):
        # Print all actions the user can do
        print("What do you want to do today? (input the number)")
        print("1 - Set the price list")
        print("2 - Show the price list")
        print("3 - Make a new transaction")
        print("4 - Close the POS machine")
    
    def setPriceList(self, FileNameEntered):
        FileofProductList = FileNameEntered # added changes
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
    
    def printPriceList(self):
        if len(self.__priceListofProducts__) == 0:
            return "No list Inputted"
        else:
            for EachProduct in self.__priceListofProducts__:
                return "{0: <4} {1: <35} {2}".format(EachProduct[0], EachProduct[1], EachProduct[2])

    
    def makeNewTransaction(self):
        if len(self.__priceListofProducts__) == 0 :
            print("List of Products in Empty")
        else:
            while True:    
                ProductInputted = input("Input the Product ")
                if ProductInputted == "":
                    self.createSalesInvoice()
                    break # This will break the loop and print the transaction
                else:
                    ProductExist = False
                    NumCount = 0 # Since the for loop is going through each list in the list of products, it will stop the moment the loop arrives at ProductInputted
                    for Eachproduct in self.__priceListofProducts__:
                        if (ProductInputted == str(Eachproduct[0])) and (ProductInputted != "ID"):
                            ProductExist = True
                            break
                        else:
                            NumCount += 1
                    if ProductExist == True: # Since the Product that the user inputs is Valid, the code will ask the use for a number
                        QuantityExist = False
                        while True:
                            try:
                                ProductQuantity = input("Input the Quantity ")
                                if ProductQuantity == "":
                                    self.createSalesInvoice()
                                    break
                                elif int(ProductQuantity) >= 1:
                                    QuantityExist = True
                                    break
                                else:
                                    continue
                            except:
                                continue
                        if QuantityExist == True:
                            self.addProductToTransaction(ProductInputted, int(ProductQuantity))
                            # break # because instructions were unclear if the makeNewTransaction method must be constantly loop until the user gives a blank input and prints the invoice, I have added a "break" to stop the loop to go back into the main Start() method
                        else:
                            break
                    else:
                        return "Product ID does not exist. Please input the Product ID"
            

         
    
    def addProductToTransaction(self, productID, quantity):
        numCount = 0 #Similar to NumCount in the makeNewTransaction method, it will search through each of entry of the list to see which list inside the list has the same product name. NumCount acts as the final location of the selected product inside the list.
        confirmedDuplicate = False
        numCountDuplicate = 0
        for EachProduct in self.__priceListofProducts__:
            if productID == str(EachProduct[0]):
                break
            else:
                numCount += 1
        ProductPriceChecking = self.__priceListofProducts__[numCount][2]
        if ProductPriceChecking == "":
            ProductPrice = 0
        else:
            ProductPrice = int(self.__priceListofProducts__[numCount][2])
        for EachSale in self.__fullTransactionList__: # This Section determines if the product ID was previous inputted to the invoice
            if productID == str(EachSale[0]):
                confirmedDuplicate = True
                break
            else:
                numCountDuplicate += 1
        if confirmedDuplicate == True: # This Section adds the quantity and cost into the entry that has the same product
            previousQuantity = self.__fullTransactionList__[numCountDuplicate][3]
            self.__fullTransactionList__[numCountDuplicate][3] = previousQuantity + quantity
            previousTotalCost = self.__fullTransactionList__[numCountDuplicate][4]
            self.__fullTransactionList__[numCountDuplicate][4] = previousTotalCost + (quantity*ProductPrice)
        else:
            self.__fullTransactionList__.append([self.__priceListofProducts__[numCount][0], self.__priceListofProducts__[numCount][1], self.__priceListofProducts__[numCount][2], quantity, (quantity*ProductPrice)])
        

    def RemoveProductToTransaction(self, productID, quantity):
        numCount = 0 #Similar to NumCount in the makeNewTransaction method, it will search through each of entry of the list to see which list inside the list has the same product name. NumCount acts as the final location of the selected product inside the list.
        confirmedDuplicate = False
        numCountDuplicate = 0
        for EachProduct in self.__priceListofProducts__:
            if productID == str(EachProduct[0]):
                break
            else:
                numCount += 1
        ProductPriceChecking = self.__priceListofProducts__[numCount][2]
        if ProductPriceChecking == "":
            ProductPrice = 0
        else:
            ProductPrice = int(self.__priceListofProducts__[numCount][2])
        for EachSale in self.__fullTransactionList__: # This Section determines if the product ID was previous inputted to the invoice
            if productID == str(EachSale[0]):
                confirmedDuplicate = True
                break
            else:
                numCountDuplicate += 1
        if confirmedDuplicate == True: # This Section adds the quantity and cost into the entry that has the same product
            previousQuantity = self.__fullTransactionList__[numCountDuplicate][3]
            self.__fullTransactionList__[numCountDuplicate][3] = previousQuantity - quantity
            previousTotalCost = self.__fullTransactionList__[numCountDuplicate][4]
            self.__fullTransactionList__[numCountDuplicate][4] = previousTotalCost - (quantity*ProductPrice)
        else:
            self.__fullTransactionList__.remove([self.__priceListofProducts__[numCount][0], self.__priceListofProducts__[numCount][1], self.__priceListofProducts__[numCount][2], quantity, (quantity*ProductPrice)])
                
    
    def createSalesInvoice(self):
        AllProducts = []
        if len(self.__fullTransactionList__) == 0:
            print("No Transactions Listed")
        else:
            title = "Sales Invoice"
            Labels = "{0}\t{1}\t{2}\t{3}\t{4}".format("ID", "Product", "Price", "Quantity", "Total")
            AllProducts.append(title)
            AllProducts.append(Labels)
            GrandTotal = 0
            for EachProduct in self.__fullTransactionList__:
                AllProducts.append("{0}\t{1}\t{2}\t{3}\t{4}".format(EachProduct[0], EachProduct[1], EachProduct[2], EachProduct[3], EachProduct[4]))
                GrandTotal += int(EachProduct[4])
            AllProducts.append("\t\t\tGrand Total {0}".format(GrandTotal))
            NewInvoiceFile = open("invoice.txt", "w")
            for x in AllProducts:
                NewInvoiceFile.write("{0}\n".format(x))
            NewInvoiceFile.close()
            for EachProductbought in self.__fullTransactionList__:
                self.__TransactionHistory__.append(EachProductbought)
            self.__fullTransactionList__.clear()

    def SalesReport(self):
        ShownTransactionHistory = []
        for EachSalesRecord in self.__TransactionHistory__:
            DuplicateConfirmed = False
            numCountDuplicate = 0
            for EachProductInside in ShownTransactionHistory:
                if EachSalesRecord[0] == EachProductInside[0]:
                    DuplicateConfirmed = True
                    break
                else:
                    numCountDuplicate += 1
            if DuplicateConfirmed == True:
                previousQuantity = ShownTransactionHistory[numCountDuplicate][3]
                previousTotalSales = ShownTransactionHistory[numCountDuplicate][4]
                ShownTransactionHistory[numCountDuplicate][3] = previousQuantity + EachSalesRecord[3]
                ShownTransactionHistory[numCountDuplicate][4] = previousTotalSales + EachSalesRecord[4]
            else:
                ShownTransactionHistory.append(EachSalesRecord)
        Saleshistory = ""
        for Sale in ShownTransactionHistory:
            print(Sale)
            #Saleshistory = Saleshistory + "{0}\t{1}\t{2}\t{3}\t{4}".format(Sale[0], Sale[1], Sale[2], Sale[3], Sale[4])





Account1 = POSMachine()





# Sources
# Built-in functions. (n.d.-d). Python Documentation. https://docs.python.org/3/builtins/functions.html#open
# pandas.Series.tolist — pandas 2.1.4 documentation. (n.d.). https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.tolist.html
# pandas.DataFrame.to_numpy — pandas 3.1.1 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
# pandas.DataFrame.columns — pandas 3.1.1 documentation. (n.d.). https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html

window = Tk()
window.title("POS Machine")

window.geometry("500x500")

# label = Label(window, text="POS Machine")

# label.grid(row=0, column=0)

# Label2 = Label(window, text="test 1")
# Label2.grid(row=1, column=1)


# def show_frame2():
#     frame1.pack_forget()
#     frame3.pack_forget() 
#     frame2.pack(fill="both", expand=True)

# def show_frame1():
#     frame2.pack_forget()
#     frame3.pack_forget() 
#     frame1.pack(fill="both", expand=True)

# def show_frame3():
#     frame1.pack_forget()
#     frame2.pack_forget()
#     frame3.pack(fill="both", expand=True)



# frame1 = Frame(window)
# Label1 = Label(frame1, text="This is Frame 1")
# Label1.grid(row=1, column=0)
# label1A = Label(frame1, text="POS Machine")
# label1A.grid(row=0, column=0)
# Button1 = Button(frame1, text="Switch to Frame 2", command=show_frame2).grid(row=2, column=0)
# Button2 = Button(frame1, text="Switch to Frame 3", command=show_frame3).grid(row=3, column=0)

# frame2 = Frame(window)
# Label2 = Label(frame2, text="This is Frame 2").pack(pady=20)
# Button2 = Button(frame2, text="Switch to Frame 1", command=show_frame1).pack()

# frame3 = Frame(window)
# Label3 = Label(frame3, text="This is Frame 3").pack(pady=20)
# Button3 = Button(frame3, text="Switch to Frame 2", command=show_frame2).pack(pady=30)
# Button3A = Button(frame3, text="Switch to Frame 1", command=show_frame1).pack(pady=30)


# frame1.pack(fill="both", expand=True)


def show_SetPriceList():
    MainMenu.pack_forget()
    SetPriceList.pack(fill="both", expand=True)


def show_NewsTransactionWindow():
    MainMenu.pack_forget()
    NewsTransactionWindow.pack(fill="both", expand=True)


def show_ClosePOS():
    MainMenu.pack_forget()
    ClosePOS.pack(fill="both", expand=True)

def show_ShowSales():
    MainMenu.pack_forget()
    ShowSales.pack(fill="both", expand=True)

def show_mainmenu():
    SetPriceList.pack_forget()
    ClosePOS.pack_forget()
    ShowSales.pack_forget()
    NewsTransactionWindow.pack_forget()
    MainMenu.pack(fill="both", expand=True)

MainMenu = Frame(window)

Label1 = Label(MainMenu, text="This is the POS Machine Main Menu").grid(row=0, column=0)
SetPrice = Button(MainMenu, text="Set Price List", command=show_SetPriceList).grid(row=1, column=0)
ShowSales = Button(MainMenu, text="Show Sales Report", command=show_ShowSales).grid(row=2, column=0)
NewsTransaction = Button(MainMenu, text="Make news transaction", command=show_NewsTransactionWindow).grid(row=3, column=0)
ClosePOSMachine = Button(MainMenu, text="Exit", command=show_ClosePOS).grid(row=4, column=0)





MainMenu.pack(fill="both", expand=True)

SetPriceList = Frame(window)
Label2 = Label(SetPriceList, text="SetPriceList").pack(side=LEFT)
contents = ScrolledText(SetPriceList)
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
SetPrice = Button(SetPriceList, text="Pick File").pack(side=LEFT)
BacktoMenu1 = Button(SetPriceList, text="Back to main Menu", command=show_mainmenu).pack(side=LEFT)



ShowSales = Frame(window)
LabelSaes = Label(ShowSales, text="show Sales report").pack(side=TOP)
BacktoMenu2 = Button(ShowSales, text="Back to main Menu", command=show_mainmenu).pack(side=LEFT)


NewsTransactionWindow = Frame(window)
Label4 = Label(NewsTransactionWindow, text="Make Transaction").pack(side=TOP)
BacktoMenu3 = Button(NewsTransactionWindow, text="Back to main Menu", command=show_mainmenu).pack(side=LEFT)


ClosePOS = Frame(window)
LabelPOS = Label(ClosePOS, text="Close").pack(side=TOP)
Yes = Button(ClosePOS, text="Yes", command=window.destroy).pack(side=LEFT)
No = Button(ClosePOS, text="No", command=show_mainmenu).pack(side=LEFT)




window.mainloop()