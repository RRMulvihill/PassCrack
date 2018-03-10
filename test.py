import random

char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','_','+','!','@','#','$','%','^','&','*','(',')','_','+']
def getList(max_length):
    passList = []
    for i in range(10000000):
        password = ''
        length = random.randint(1,max_length)
        for j in range(length):
            password += str(char_list[random.randint(1,72)])
        passList.append(password)
    return passList


def checkPass (entered,password):
    if entered == password:
        return True

def runList (passList,password):
    pass_found = False
    correct_pass = 'Pass not Found'
    count = 0
    for guess in passList:
        if checkPass(guess,password)== True:
            correct_pass = guess
            pass_found = True
        else:
            count += 1
    print("ran " + str(count) + " guesses")
    print(correct_pass)    
            
    

def run():
    runList(getList(10),'agfd')

    

