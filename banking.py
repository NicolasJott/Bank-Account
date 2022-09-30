import random
import os
import pathlib
import time
import shutil
import re
from accountClass import bank_account
from datetime import date
import pandas as pd 
               
def createAccount(): #funcion to create a new user account
                account = ""
                f_name = input("Client First Name : ") # collect client information
                l_name = input("Client Last Name : ")
                social = input("Client Social Security Number (###-##-####) : ")
                dob = input("Client Date of Birth (M/D/YYYY) : ")            
                existing_accounts = [] #empty to check if the new account number exsist
                j_existing_accounts = []
                file = open("existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                file = open("j_existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        j_existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                while True:
                    account_number = random.randint(100000000, 999999999) # generate account number
                    if account_number in existing_accounts or account_number in j_existing_accounts:
                        break
                    else:
                       
                        existing_accounts.append(account_number)
                        file = open("existing_accounts.txt", "a")
                        file.write(str(account_number))
                        file.write(",")
                        file.close()
                        break
                account_directory = (str(account_number)) #Create account directory
                os.mkdir(account_directory)
                deposit = int(input("What is the initial deposit?: "))
                file = open(str(account_directory) + "/balance.txt","w")
                file.write(str(deposit))
                file.close()
                file = open(str(account_directory) + "/history.txt","a")
                file.write(str(time.asctime()) + "___Initial Deposit: "+"$"+str(deposit))
                file.close()
                file = open(str(account_directory)+"/information.txt","w")
                file.write("Account Number: "+ str(account_number) + "\n" + "First Name: "+f_name+"\n"+"Last Name: "+l_name+"\n"+"Social Security Number: "+social+"\n"+"Date of Birth: "+ dob)
                file.close()
                Account = bank_account(f_name, l_name, social, dob, deposit, account_number)
                all_accounts = existing_accounts + j_existing_accounts
                file = open("accounts.csv","a") #appends data to a csv file
                index = all_accounts.index(account_number) + 1
                file.write(str(index) + "," + str(account_number) + "," + str(l_name) + "," + str(f_name) + "," + str(social) + "," + str(dob) + "," + str(deposit) + "," + "Savings" + "\n")
                print("***************")
                print("This accounts number is:",str(account_number))
                print("***************") 
                main(0,account_number,existing_accounts,j_existing_accounts) #calls main function



def createJoint(account_number): #function to create a new joint account
                j_account = ""
                f_name = input("Client First Name : ") # collect client information
                l_name = input("Client Last Name : ")
                social = input("Client Social Security Number (###-##-####) : ")
                dob = input("Client Date of Birth (MM/DD/YYYY) : ")
                existing_accounts = [] #empty to check if the new account number exsist
                j_existing_accounts = []
                file = open("existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        existing_accounts.append(j_account)
                        j_account = ""
                    else:
                        j_account = j_account + i
                file.close()
                file = open("j_existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        j_existing_accounts.append(j_account)
                        j_account = ""
                    else:
                        j_account = j_account + i
                file.close()
                while True:
                    j_account_number = random.randint(100000000, 999999999) # generate account number
                    if j_account_number in existing_accounts or j_account_number in j_existing_accounts:
                        break
                    else:
                        j_existing_accounts.append(j_account_number)
                        file = open("j_existing_accounts.txt", "a")
                        file.write(str(j_account_number))
                        file.write(",")
                        file.close()
                        break
                j_account_directory = (str(j_account_number)) #creates a directory with the random generated account number
                os.mkdir(j_account_directory)
                deposit = int(input("What is the initial deposit?: "))
                file = open(str(j_account_directory) + "/balance.txt","w") #creates file containing balance
                file.write(str(deposit))
                file.close()
                file = open(str(j_account_directory) + "/history.txt","a") #creates file containing account history
                file.write(str(time.asctime()) + "___Initial Deposit: "+"$"+str(deposit))
                file.close()
                file = open(str(j_account_directory)+"/information.txt","w") #creates file containg user information
                file.write("Parent Account Number: " + str(account_number)+ "\n" + "Account Number: " +str(j_account_number) +"\n" + "First Name: "+f_name+"\n"+"Last Name: "+l_name+"\n"+"Social Security Number: "+social+"\n"+"Date of Birth: "+dob)
                file.close()
                Account = bank_account(f_name, l_name, social, dob, deposit, account_number)
                all_accounts = existing_accounts + j_existing_accounts #combines the two main lists together 
                file = open("accounts.csv","a") #writes user data to a csv file
                index = all_accounts.index(j_account_number) + 1 #row numbers based off index
                file.write(str(index) + "," + str(account_number) + "," + str(l_name) + "," + str(f_name) + "," + str(social) + "," + str(dob) + "," + str(deposit) + "," + "Joint" + "\n")
                print("***************")
                print("This accounts number is:",str(j_account_number))
                print("***************")
                account_number = j_account_number
                jointMain(account_number,existing_accounts,j_existing_accounts) #calls main function to bring ui for a joint user up front 

def readExisting(num2): #this function creates an updated list of all the account numbers
            if num2 == 1:
                account = ""
                existing_accounts = [] 
                file = open("existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                return existing_accounts
                
            elif num2 == 2:
                file = open("j_existing_accounts.txt", "r")
                j_account = ""
                j_existing_accounts = []
                data = file.read()
                for i in data:
                    if i == ",":
                        j_existing_accounts.append(j_account)
                        j_account = ""
                    else:
                        j_account = j_account + i
                file.close()
                return j_existing_accounts
            print(j_existing_accounts)
            print(existing_accounts)
def validate():
    #code to check the existing accounts file
                account_number = input("Enter the account number: ")
                account = ""
                existing_accounts = []
                j_existing_accounts = []
                file = open("existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                file = open("j_existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        j_existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                if account_number in existing_accounts: #checks if the account number is in this list
                        pass
                        old_number = account_number #stores account number in this variable for later use
                        main(old_number,account_number, existing_accounts, j_existing_accounts) #if account number is in this list, its an individual account so it will call the regular ui funciton
                elif account_number in j_existing_accounts:
                        pass 
                        print(account_number) 
                        jointMain(account_number, existing_accounts, j_existing_accounts) #if account number is in the joint accounts list, will call the joint ui funcion. 
                else:
                        print("The inputted account number does not match any of our previous records.")
                        create = input("Would you like to create an account? (Y/N): ").upper()
                        if create == "Y":
                                createAccount()
                        else:
                                pass

def removeAccount(num,account_number): #function to remove any given account           
                if num == 1:    #for individual account
                    existing_accounts = readExisting(1)               
                    confirm = input("Are you sure you wish to delete this account? (Y/N): ").upper()
                    if confirm == "Y":
                            shutil.rmtree(str(account_number)) #removes directory and everything inside of it               
                            existing_accounts.remove(str(account_number))
                            string = ",".join(existing_accounts)
                            file = open("existing_accounts.txt","w")
                            file.write(string)
                            file.close()                           
                            print("***************")
                            print("This account has been succesfully closed")
                            print("***************")
                            loginScreen()
                    elif confirm == "N":
                            pass
                    else:
                            print("Invalid Choice")
                elif num == 2:  #for joint account
                    print(account_number)
                    j_existing_accounts = readExisting(2)              
                    confirm = input("Are you sure you wish to delete this account? (Y/N): ").upper()
                    if confirm == "Y":
                            removing_j_history = (str(account_number) + "/history.txt") #This code essentially does the same thing as the code above but I kept this code to show you can achieve the same thing with less code. 
                            removing_j_balance = (str(account_number) + "/balance.txt")
                            removing_j_information = (str(account_number) + "/information.txt")
                            os.remove(removing_j_history)
                            os.remove(removing_j_balance)
                            os.remove(removing_j_information)
                            os.removedirs(str(account_number))
                            j_existing_accounts.remove(str(account_number))
                            string = ",".join(j_existing_accounts)
                            file = open("j_existing_accounts.txt","w")
                            file.write(string)                       
                            file.close()
                            print("***************")
                            print("This account has been succesfully closed")
                            print("***************")
                            pass
                    elif confirm == "N":
                            pass
                    else:
                            print("Invalid Choice")
def depositAndWithdraw(account_number,num,deposit,existing_accounts,j_existing_accounts): #Handles depositing and withdrawing in any account. 
    all_accounts = existing_accounts + j_existing_accounts
    index = all_accounts.index(account_number) #variable for the index of the account number in the all_accounts list
    file = open(str(account_number)+"/balance.txt","r")
    deposit = file.read()
    file.close()
    file = open(str(account_number)+"/balance.txt","w")
    file2 = open(str(account_number)+"/history.txt","a")
    df = pd.read_csv("accounts.csv")
    if num == 1: #deposit
        print("***************")
        print("Your current account balance is", "$"+str(deposit)) #displays current balance before deposit
        amount = float(input("Enter the amount to deposit: ")) #asks user what to deposit
        newdeposit = float(deposit) + amount # balance plus the deposit
        newBalance = "{:.2f}".format(newdeposit)
        file.write(str(newBalance)) # writes the new balance to the balance.txt file
        file2.write("\n"+str(time.asctime())+"___Deposited: "+ "$"+str(amount)) #updates the history.txt file with the amount deposited
        print("You have succesfully deposited","$"+str(amount)+"!")
        print("***************")
        print("Your current account balance is","$"+str(newBalance))
        df.loc[index, 'Balance'] = str(newBalance) #updates csv file with the new balance 
        df.to_csv("accounts.csv", index=False)
        file.close()
        file2.close()
        input()

    elif num == 2: #withdraw
        while True: #while loop to prevent user from withdrawing more than what is in the account
            print("***************")
            print("Your current account balance is", "$"+str(deposit))
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= float(deposit): #checks if amount requested to withdraw is less than the balance
                newdeposit =  float(deposit) - amount #subtracts withdraw from the balance
                newBalance = "{:.2f}".format(newdeposit)
                file.write(str(newBalance)) #writes to balance file
                file2.write("\n"+str(time.asctime())+"___Withdrew: "+"$"+str(amount)) #updates history file
                print("You have succesfully deposited","$"+str(amount)+"!")
                print("***************")
                print("Your current account balance is","$"+str(newBalance))
                df.loc[index, 'Balance'] = str(newBalance)
                df.to_csv("accounts.csv", index=False) #updates csv file with the new balance
                file.close()
                file2.close()
                input()
                break
            else:
                print("You cannot withdraw more than the account balance.")

def displayBalance(account_number): #method to simply display the user's balance
    file = open(str(account_number)+"/balance.txt","r")
    print("***************")
    print("This account's balance is "+"$"+file.read()) #reads from the balance.txt file and displays the value.
    input()
    file.close()

def savings(): #Function to incorporate interest
                account = ""
                existing_accounts = [] 
                file = open("existing_accounts.txt", "r")
                data = file.read()
                for i in data:
                    if i == ",":
                        existing_accounts.append(account)
                        account = ""
                    else:
                        account = account + i
                file.close()
                print(existing_accounts)
                file = open("j_existing_accounts.txt", "r")
                j_account = ""
                j_existing_accounts = []
                data = file.read()
                for i in data:
                    if i == ",":
                        j_existing_accounts.append(j_account)
                        j_account = ""
                    else:
                        j_account = j_account + i
                file.close()
                all_accounts = existing_accounts + j_existing_accounts
                from math import e
                for x in all_accounts:
                    index = all_accounts.index(x)
                    df = pd.read_csv("accounts.csv")
                    file = open(str(x)+"/balance.txt","r")
                    balance = file.read()
                    file.close()
                    file = open(str(x)+"/balance.txt","w")
                    interest = float(balance) * (e**.017*1) #Takes balance from each account and applies 1.7% interest on their current balances compunded monthly
                    format_interest = "{:.2f}".format(interest)
                    file.write(str(format_interest))
                    file.close()
                    file = open(str(x)+"/history.txt","a") #updates history file to show this added interest
                    file.write("\n"+str(time.asctime())+"___Interest: "+"$"+str(format_interest))
                    df.loc[index, 'Balance'] = str(format_interest)
                    df.to_csv("accounts.csv", index=False)
                    file.close()
def intro(): #Prints out an intro screen
        print("\t\t\t\t***************")
        print("\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t***************")
        print("\t\t\t\tBrought To You By:")
        print("\t\t\t\tNicolas Ott")
        input()
        loginScreen()

def loginScreen(): #main login screen where user can either login to a individual account, joint account, or create an account
    ch=""
    num=0
    while ch != 3:
        print("\t1. LOG IN")
        print("\t2. Create ACCOUNT")
        print("\t3. EXIT")
        print("\tSelect Your Option (1-3): ")
        ch = input() 
        if ch == '1':
            validate()
            break
        elif ch == '2':
            createAccount()
            break
        elif ch == '3':
            print("\tThanks for using bank management system.")
            break
        else:
            print("Invalid Choice")
            pass
def jointMain(account_number,existing_accounts,j_existing_accounts): #main ui for joint accounts
    ch = ""
    deposit = 0
    while ch != 5:
            print("\tMAIN MENU")
            print("\t1. DEPOSIT AMOUNT")
            print("\t2. WITHDRAW AMOUNT")
            print("\t3. ACCOUNT BALANCE")
            print("\t4. CLOSE ACCOUNT")
            print("\t5. EXIT")
            print("\tSelect Your Option (1-5): ")
            ch = input()
            if ch == '1':
                    depositAndWithdraw(account_number,1, deposit,existing_accounts,j_existing_accounts)
                    
            elif ch == '2':
                    depositAndWithdraw(account_number,2, deposit,existing_accounts,j_existing_accounts)
            elif ch == '3':
                    displayBalance(account_number)
            elif ch == '4':
                    removeAccount(2,account_number)
                    break
            elif ch == '5':
                print("\tThanks for using bank management system.")
                break        
            else:
                    print("Invalid Choice")
                    pass
def getAccountNumber(old_number): #this function is used when logging into a joint account through an individual account. The individual account number is stored in this function until the individual ui is brought back to the front. 
    account_number = old_number

def main(old_number,account_number,existing_accounts,j_existing_accounts): #main ui for individual accounts
    getAccountNumber(old_number) #calls function to assign account number to a stored variable. 
    all_accounts = existing_accounts + j_existing_accounts
    ch = ""
    deposit = 0
    while ch != 8:
            print("\tMAIN MENU")
            print("\t1. NEW ACCOUNT")
            print("\t2. DEPOSIT AMOUNT")
            print("\t3. WITHDRAW AMOUNT")
            print("\t4. ACCOUNT BALANCE")
            print("\t5. ADD JOINT ACCOUNT")
            print("\t6. CLOSE ACCOUNT")
            print("\t7. ACCESS JOINT")
            print("\t8. EXIT")
            print("\tSelect Your Option (1-8): ")
            ch = input()
            if ch == '1':
                    createAccount()
                    break
            elif ch == '2':
                    depositAndWithdraw(account_number,1, deposit,existing_accounts,j_existing_accounts)
            elif ch == '3':
                    depositAndWithdraw(account_number,2, deposit,existing_accounts,j_existing_accounts)
            elif ch == '4':
                    displayBalance(account_number)
            elif ch == '5':
                    createJoint(account_number)
            elif ch == '6':    
                    removeAccount(1,account_number)
                    break
            elif ch == '7':
                    validate()                   
            elif ch == '8':
                    print("\tThanks for using bank management system.")
                    break
            else:
                    print("Invalid Choice")
                    pass
if date.today().day != 1: #if the day of any given month is not 1, it will pass the function
            pass
else:   #if the day of any given month is 1, it will execute the function
            savings() #calls interest method

intro() #beginning of program



