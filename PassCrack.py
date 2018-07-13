class Passcrack:

    #Creates password lists
    with open("C:/Users/admin/Documents/GitHub/PassCrack/librarys/500_passwords.txt") as f:
        shortList = f.read().splitlines()
    with open("C:/Users/admin/Documents/GitHub/PassCrack/librarys/10_million_password_list_top_1000000.txt") as pl:
        passList = pl.read().splitlines()
    with open("C:/Users/admin/Documents/GitHub/PassCrack/librarys/english.txt") as ed:
        english = ed.read().splitlines()


    
    #Creates class instance
    def __init__(self,password):
        #password must be string
        self.password = password
        self.count = 0
        self.pass_found = False
        self.correct_pass = 'Pass not Found'

        
    #compares guess to password    
    def checkPass (self,entered):
        if self.password == entered:
            print('PASSWORD SOLVED!!!')
            return True
    #checks each list item against the password
    def runList (self,passList):
        for guess in passList:
            if self.checkPass(guess)== True:
                self.correct_pass = guess
                self.pass_found = True
                return self.correct_pass
            else:
                self.count += 1

    #creates a new password list with a specified number at the end
    def plusNum(self,num, passList):
        new_list = [password + str(num) for password in passList]
        return new_list

    
    def run(self):
        self.runList(Passcrack.passList)
        self.runList(Passcrack.english)
        self.runList(self.plusNum(1, Passcrack.english))
        print("ran " + str(self.count) + " guesses")
        print('Password: ' + self.correct_pass)
        
    def runNum(self, num_range):
        while self.pass_found == False:
            for i in range(num_range):
                self.runList(self.plusNum(i, Passcrack.english))
                print( "attempt " + str(i))
        print("ran " + str(self.count) + " guesses")
        print('Password: ' + self.correct_pass)

    def clear(self):
        self.count = 0
        self.pass_found = False
        self.correct_pass = 'Pass not Found'

#Runs program
def main():
    run = True
    print("PassCrack")
    print("   by Riley Mulvihill")
    print("")
    print("How Strong is your Password?")
    print("PassCrack compares your password")
    print("with millions of commonly used passwords")
    print("")
    print("")
    while(run):
        print("")
        password = str(input("Please enter a Password to Test):"))
        try:
            password = str(password)
        except:
            print("invalid input")
            print("Password must be convetible to a string")
            return

        instance = Passcrack(password)
        instance.run()
        run_boolean = input("Run Again? (y/n):")
        if run_boolean == "y":
            run = True
        elif run_boolean == "n":
            run = False
        else:
            print("Invalid input")

main()
print("")
print("Thank you for using PassCrack")
print("Hit 'Enter' to close")
input()
