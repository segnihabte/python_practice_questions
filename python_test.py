import random
print("hello, welcome to guess the number")
print("please Tell us Your Name")
name = input()
surr = ""
Gender = input("Enter M for a male and F for a Female")
if Gender == "M":
        surr="Mr"
elif Gender == "F":
        surr ="Mrs"
secretNum = random.randint(1,20)
print("Well, now guess the number between 1 and 20")
#the player will guess only 5 times 
def GuessTheNumber():
        for i in range(1,9):
                print("take a guess")
                guess = int(input())
                if guess>secretNum:
                        print("your guess is too high," +surr +" " +name)
                elif guess<secretNum:
                        print("your guess is too low," +surr +" " +name)
                else:
                        print("CONGRATS ON YOUR GUESS !!!🎉🎉🎉🎉🎉, THE CORRECT NUMBER IS ", secretNum ,surr+" " +name )
                        break
print('this is also a python code')
GuessTheNumber()