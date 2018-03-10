class Passcrack:
    with open("500_passwords.txt") as f:
        shortList = f.read().splitlines()
    with open("10_million_password_list_top_1000000.txt") as pl:
        passList = pl.read().splitlines()
    with open("english.txt") as ed:
        english = ed.read().splitlines()
    with open("pet_names.txt") as pn:
        petList = pn.read().splitlines()


    

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


    def plus(self,added, passList):
        new_list = [password + str(added) for password in passList]
        return new_list

    def run(self):
        self.runList(Passcrack.passList)
        self.runList(Passcrack.english)
        self.runList(self.plus(1, Passcrack.english))
        print("ran " + str(self.count) + " guesses")
        print('Password: ' + self.correct_pass)
        
    def runNum(self, wordlist, num_range):
        count = 0;
        while count < num_range:
            for i in range(num_range):
                if self.pass_found == False:
                    self.runList(self.plus(i, wordlist))
                    print( "attempt " + str(i))
                    count += 1
                else:
                    print("ran " + str(self.count) + " guesses")
                    print('Password: ' + self.correct_pass)
                    return 
    def runPet(self):
        self.runList(self.plus('dog', Passcrack.petList))
        self.runList(self.plus('dog1', Passcrack.petList))
        self.runList(self.plus('cat', Passcrack.petList))
        self.runList(self.plus('cat1', Passcrack.petList))
        print("ran " + str(self.count) + " guesses")
        print('Password: ' + self.correct_pass)

    def checkDouble(self, passList):
        count = 0
        for first in passList:
            for second in passList:
                if count%1000000 == 0:
                    print(count)
                if self.checkPass(first + second)== True:
                    self.correct_pass = guess
                    self.pass_found = True
                    return self.correct_pass
                else:
                    self.count += 1
                    count += 1
    def runDouble(self):
        self.checkDouble(self.english)

    def runAll(self):
        self.run()
        self.runPet()
        self.runNum(self.passList,100)
        self.runNum(self.english,100)
    def clear(self):
        self.count = 0
        self.pass_found = False
        self.correct_pass = 'Pass not Found'
