from random import *
from engi1020.arduino import *
from time import*

QMath = ["What is 12*13?","What is sin(π)?","What is cos(0)?", 
         "What is the antiderrivative of 1?", 
         "How many degrees does a triangle have?", 
         "What is tan(π/3)?Answer in exponent form?", 
         "What is 64** -1/2?Answer in fraction form?"]

AMath = ["156", "0", "1", "x", "180" , "3**1/2", "1/8"]

QHist =["What philosopher stated, 'Cogito, ergo sum'?", 
        "Who wrote the 95 theses?", 
        "Who defied segregation by sitting on the front of the bus?",
        "What is the main religion of the world?",
        "What is Harriet Tubman's nickname?",
        "What is the name of the Colombian novelist who won a Noble Prize in Literature?",
        "What is the name of the President of the United States who abolished slavery?"]

AHist = ["Rene Descartes", "Martin Luther", "Rosa Parks", "Christianity", "Moses", 
         "Gabriel Garcia Marquez", "Abraham Lincoln"]

QChem = ["What is this number known as 6.022 * 10^23?",
         "How many states of matter are there?", 
         "What is the name of a positevly charged ion?", 
         "What is the unite amount of substance?",
         "This bond occurs when two atoms share an electron?", 
         "273 K equals what value in Celsius?", 
         "What does entropy measure?One word?"]

AChem = ["Avogadro's Number", "4", "Cation","Mole", "Covalent Bond", "0", "Order"]


QPhys = ["What is the magnitude of gravity? Round to second decimal place",
         "What is the force that opposes movement?",
         "What is the force that opposes weight?",
         "Fill in the blank: Energy is not created or ____",
         "What is the equation of Newton's Second Law?",
         "Is gravity different in outter space? Yes or No", 
         "Fill in the blanck: Physics is the study of the __? One word"]

APhys = ["9.81","Friction", "Normal", "Destroyed", "F=m*a", "Yes", "Universe"]

"""
Description: 
Depending on the Rotary Dial(RDvalue) input value, a question of chemistry, physics, math, or history will be picked randomly from the pertaining list of the field of study for the user to answer. 
The type of question will then be outputted to the LCD screen and changing the screen to its corresponding colour. 
After, the question will be outputted to the console. 
Then the user will input the answer via the keyboard. 
If the user’s input matches the answer stored in the list, the user will receive 200 points, held in userpts. 
Users must follow the instructions stated at the beginning of the game for solutions to be correct. 
Else the user will receive 0 points. 
After, the LCD screen will be cleared and set to a white background. 
The function returns the user’s total points held in the variable userpts. 

Parameters:
    RDvlaue - integer, the value of the rotary dial that the user inputs.
        Limits are from 0 to 1023, with the 0 and 1023 included.
    userpts - integer, the user’s points
          
Returns:
    userpts - integer, value of points the user earned
"""


def Qtype(RDvalue, userpts):
    Qnumber = randint(0,6) 
    if RDvalue >= 0 and RDvalue <= 255:
        lcd_rgb(245,138,66) #orange colour
        lcd_print("Math question!")
        print(QMath[Qnumber])
        AMUser = str(input("Enter your answer please?"))
        if AMUser == AMath[Qnumber]:
            print("You are correct! You have earned 200 points!")
            userpts += 200
        else:
            print("A+ for trying! ")
    elif RDvalue > 255 and RDvalue <= 510:
        lcd_rgb(66,245,108) #green colour
        lcd_print("History question!")
        print(QHist[Qnumber])
        AHUser = str(input("Enter your answer please?"))
        if AHUser == AHist[Qnumber]:
            print("You are correct! You have earned 200 points!")
            userpts += 200
        else:
            print("A+ for trying! ")
    elif RDvalue > 510 and RDvalue <= 765:
        lcd_rgb(245,66,218) #pink colour
        lcd_print("Chemistry question!") 
        print(QChem[Qnumber])
        ACUser = str(input("Enter your answer please?"))
        if ACUser == AChem[Qnumber]:
            print("You are correct! You have earned 200 points!")
            userpts += 200
        else:
            print("A+ for trying! ")
    elif RDvalue > 765 and RDvalue <= 1023:
        lcd_rgb(66,242,245)# light blue colour
        lcd_print("Physics question!")
        print(QPhys[Qnumber])
        APUser = str(input("Enter your answer please?"))
        if APUser == APhys[Qnumber]:
            print("You are correct! You have earned 200 points!")
            userpts += 200
        else:
            print("A+ for trying! ")
            
    lcd_rgb(255,255,255)#white colour
    lcd_clear()    
    return userpts

usercontinue = "Yes"
while usercontinue == "Yes" or usercontinue == "yes": 
    print("Welcome to Trivia game!") 
    print("Instructions for the following questions: for multiplication symbol use '*', for exponent form '**' and for fraction '/. Follow grammatical conventions please.'")
    userpts = 0
    Loserdetector = 1 
    while userpts < 1000:
        print("Please move the rotary dial.")
        sleep(5)
        RDvalue = analog_read(0)
        Response= Qtype(RDvalue, userpts)
        Loserdetector = Response - userpts
        if Loserdetector == 0:
            break
        userpts = Response
        print("Your current points are:", Response)
    
    if Loserdetector == 0:
        print("You have lost. Better luck next time.")
        print("Your final score is:", Response)
    else:
        print("Congratulations you have won!") 
    usercontinue = input("Do you want to play again? Type Yes or No")
print("Game over. Thank you for playing!")