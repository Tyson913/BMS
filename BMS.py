
# BMS(BANK MANAGEMENT SYSTEM)
# SP = Sign Up
# LN = Log In

import json

class BMS: # Bank Management System Object
    # Initiallize the BMS
    def __init__(self, accounts, balance):
        self.accounts = accounts
        self.balance = balance
    
    # Made a function for getting the chosen user auth of the user (Log In and Sign Up)
    def getUserAuth(self):
        print("1. Sign Up\n2. Log In")
        chosenUserAuth = int(input("Enter a number: "))

        return chosenUserAuth

    # Made a function for getting the signed up username of the user
    def getSPUsername(self):
        SPUsername = input("Enter your desired username: ")
        return SPUsername
    
    # Made a function for getting the created password of the user
    def getSPPassword(self):
        SPPassword = input("Enter a password: ")
        SPPasswordConfirmation = input("Confirm your password: ")

        return SPPassword, SPPasswordConfirmation

    # Function for the validation of Signed Up Username of the user
    def SPUsernameisValid(self, SPusername):
        if len(SPusername) >= 6:
            return True
        return False
    
    # Function for the validation of Signed Up password of the user
    def SPPasswordisValid(self, SPPassword, SPPasswordConfirmation):
        if len(SPPassword) and len(SPPasswordConfirmation) >= 6 and SPPasswordConfirmation == SPPassword:
            return True
        return False
    
    # Function to print out the offered services
    def Services(self):
        Services = '''
            ======================================
            ||             Services             ||
            ======================================
            ||            1. Deposit            ||
            ||            2. Transfer           ||
            ||            3. Withdraw           ||
            ||      4. Transaction History      ||
            ======================================

        '''
        print(Services)
        return None
    
    def addAcc(self, SPUsername, SPPassword):
        self.accounts = []
        account = {
            "username": SPUsername,
            "password": SPPassword
        }

        self.accounts.append(account)

        with open('BMS.json', 'w') as file:
            json.dump(self.accounts,file)



def main():
    print(" ")
    # Created a temporary instance for the BMS
    bms = BMS(accounts=True, balance=True)

    # Collected the username of the user inside the getSPUsername function inside the class
    while bms.getUserAuth() != 1 and bms.getUserAuth() != 2:
        print("Please enter a valid number.")
        bms.getUserAuth()
    while True:
        if bms.getUserAuth() == 1:
            SPUsername = bms.getSPUsername() # if the chosen user auth is 1 then perform the username validation
            if bms.SPUsernameisValid(SPUsername): # if the SPUsername is valid, the getSPPassword will be executed
                SPPassword, SPPasswordConfirmation = bms.getSPPassword() # Get the values of the variables SPPassword and SPPasswordConfirmation
                if bms.SPPasswordisValid(SPPassword, SPPasswordConfirmation): # if the password created by the user is valid, then the function Services will be executed
                    bms.addAcc(SPUsername, SPPassword)
                    bms.Services()
                    break
                
            break
        elif bms.getUserAuth() == 2:


            # Code for the log In user auth here
            break # Temporary code to avoid error


if __name__ == "__main__":
    main()