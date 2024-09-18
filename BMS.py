
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
        signedUpUsername = input("Enter your desired username: ")
        return signedUpUsername

    def SPUsernameisValid(self, signedUpUsername):
        if len(signedUpUsername) >= 6:
            return True
        return False
    
def main():
    # Created a temporary instance for the BMS
    bms = BMS(accounts=True, balance=True)

    # Declared the getSPUsername function inside the class
    signedUpUsername = bms.getSPUsername()

    if bms.SPUsernameisValid(signedUpUsername):
        print("The password is valid")
    else:
        print("Invalid Password. Password should have atleast 6 characters")





if __name__ == "__main__":
    main()