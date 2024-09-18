
# BMS(BANK MANAGEMENT SYSTEM)
# SP = Sign Up
# LN = Log In

class BMS:
    # Initiallize the BMS
    def __init__(self, accounts, balance):
        self.accounts = accounts
        self.balance = balance
    
    # Made a function for getting the signed up username of the user
    def getSPUsername(self):
        SPUsername = input("Enter your desired username: ")
        return SPUsername
    
    def getSPPassword(self):
        SPPassword = input("Enter a password: ")
        SPPasswordConfirmation = input("Confirm your password: ")

        return SPPassword, SPPasswordConfirmation

    def SPUsernameisValid(self, SPusername):
        if len(SPusername) >= 6:
            return True
        return False


def main():
    # Created a temporary instance for the BMS
    bms = BMS(accounts=True, balance=True)

    # Declared the getSPUsername function inside the class
    SPUsername = bms.getSPUsername()

    if bms.SPUsernameisValid(SPUsername):
        print("The password is valid")
    else:
        print("Invalid Password. Password should have atleast 6 characters")

if __name__ == "__main__":
    main()