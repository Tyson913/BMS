
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
        chosen_service = input("Enter the number of the service you'd like: ")
        return chosen_service

    
    def SPAccountisValid(self, SPUsername, SPPassword):
        with open('BMS.json', 'r') as file:
            data = json.load(file)

        return SPUsername != data["username"] and SPPassword != data["password"]

    def addAcc(self, SPUsername, SPPassword):
        self.accounts = []
        account = {
            "username": SPUsername,
            "password": SPPassword
        }

        self.accounts.append(account)

        with open('BMS.json', 'w') as file:
            json.dump(self.accounts,file)

    def getLN(self):
        LNusername = input("Username: ")
        LNpassword = input("Password: ")

        return LNusername, LNpassword
    
    def LNisValid(self,LNusername, LNpassword):
        with open('BMS.json', 'r') as file:
            data = json.load(file)

        for acc in data:
            if acc.get["username"] == LNusername and acc.get["password"] == LNpassword:
                return True
            return False

def main():
    print(" ")
    # Created a temporary instance for the BMS
    bms = BMS(accounts=True, balance=True)

    # Collected the username of the user inside the getSPUsername function inside the class
    chosenUserAuth = bms.getUserAuth()
   
    while chosenUserAuth != 1 and chosenUserAuth != 2:
        print("Invalid input. Please enter a valid number for user authentication.")
        bms.getUserAuth()
        print(' ')
    
    while True:
        match chosenUserAuth:
            case 1:
                SPUsername = bms.getSPUsername()
                if bms.SPUsernameisValid(SPUsername):
                    while True:
                        SPPassword, SPPasswordConfirmation = bms.getSPPassword()
                        if bms.SPPasswordisValid(SPPassword,SPPasswordConfirmation):
                            chosen_service = bms.Services()
                            match chosen_service:
                                case 1:
                                    print("You chose the deposit service")
                                case 2:
                                    print("You chose the transfer service")
                                case 3:
                                    print("You chose the withdraw service")
                                case 4:
                                    print("You chose to view your transaction history")
                        else:
                            continue
                else:
                    continue
            case 2:
                LNusername, LNpassword = bms.getLN()
                if bms.LNisValid(LNusername, LNpassword):
                    chosen_service = bms.Services()

                    match chosen_service:
                        case 1:
                            print("You chose the deposit service")
                        case 2:
                            print("You chose the transfer service")
                        case 3:
                            print("You chose the withdraw service")
                        case 4:
                            print("You chose to view your transaction history")
                else:
                    print("Account doesn't exist.")
                    continue
 
if __name__ == "__main__":
    main()