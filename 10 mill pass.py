class Passcrack:
    with open("500_passwords.txt") as f:
        shortList = f.read().splitlines()
    with open("10_million_password_list_top_1000000.txt") as pl:
        passList = pl.read().splitlines()
    with open("english.txt") as ed:
        english = ed.read().splitlines()


    

    def __init__(self,password):
        self.password = password
        self.count = 0
        self.pass_found = False
        self.correct_pass = 'Pass not Found'
        
    def checkPass (self,entered):
        if self.password == entered:
            print('PASSWORD SOLVED!!!')
            return True

    def runList (self,passList):
        for guess in passList:
            if self.checkPass(guess)== True:
                self.correct_pass = guess
                self.pass_found = True
                return self.correct_pass
            else:
                self.count += 1


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
