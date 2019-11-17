# import datetime
import time
# currentDT = datetime.datetime.now()
# functions
import webbrowser
name = input("Hello, Please input your name: ")
bonus = 3
gradehonors = 13.5
def Honors():
    honorsgrade = input("Tell me your grade in Honors: ")
    if honorsgrade == "A+" or honorsgrade == "a+":
        gradeh = 13.5
    elif honorsgrade == "A" or honorsgrade == "a":
        gradeh = 12.5
    elif honorsgrade == "A-" or honorsgrade == "a-":
        gradeh = 11.5
    elif honorsgrade == "B+" or honorsgrade == "b+":
        gradeh = 10.5
    elif honorsgrade == "B" or honorsgrade == "b":
        gradeh = 9.5
    elif honorsgrade == "B-" or honorsgrade == "b-":
        gradeh = 8.5
    elif honorsgrade == "C+" or honorsgrade == "c+":
        gradeh = 7.5
    elif honorsgrade == "C" or honorsgrade == "c":
        gradeh = 6.5
    elif honorsgrade == "C-" or honorsgrade == "c-":
        gradeh = 5.5
    elif honorsgrade == "D+" or honorsgrade == "d+":
        gradeh = 4.5
    else:
        print("That was not a valid answer please try again.")
        Honors()
    return gradeh
def apcalc():
    ap = input("What is your grade in ap class? ")
    if ap == "A+" or ap == "a+":
        gradea = 15
    elif ap == "A" or ap == "a":
        gradea = 14
    elif ap == "A-" or ap == "a-":
        gradea = 13
    elif ap == "B+" or ap == "b+":
        gradea = 12
    elif ap == "B" or ap == "b":
        gradea = 11
    elif ap == "B-" or ap == "b-":
        gradea = 10
    elif ap == "C+" or ap == "c+":
        gradea = 9
    elif ap == "C" or ap == "c":
        gradea = 8
    elif ap == "C-" or ap == "c-":
        gradea = 7
    elif ap == "D+" or ap == "d+":
        gradea = 6
    else:
        print("That was not a valid answer please try again")
        apcalc()
    return gradea

def standard():
    st = input("What is your standard grade?: ")
    if st == "A+" or st == ("a+"):
        grades = 12
    elif st == "A" or st == ("a"):
        grades = 11
    elif st == "A-" or st == ("a-"):
        grades = 10
    elif st == "B+" or st == ("b+"):
        grades = 9
    elif st == "B" or st == ("b"):
        grades = 8
    elif st == "B-" or st == ("b-"):
        grades = 7
    elif st == "C+" or st == ("c+"):
        grades = 6
    elif st == "C" or st == ("c"):
        grades = 5
    elif st == "C-" or st == ("c-"):
        grades = 4
    elif st == "D+" or st == ("d+"):
        grades = 3
    else:
        print("That was not a valid answer please try again.")
        standard()
    return grades
def intro():
    print("Hello", name, ", my name is Genie. I am a gpa calculator created by Aman Shaik")
    print("Help me out with some basic information first.")
def questions():
    ap = int(input(" How many ap classes do you take?:  "))
    h = int(input(" How many Honors classes do you take?:  "))
    st = int(input(" How many Standard classes do you take?:  "))
    numclasses = h + ap + st
    if numclasses > 5:
        bonus = 3
    else:
        bonus = 0
    print("You take ", numclasses, "classes")
    htotal = 0
    aptotal = 0
    sttotal = 0
    for honors in range(h):
        grade = Honors()
        htotal = htotal + grade
    for ap in range(ap):
        grade = apcalc()
        aptotal = aptotal + grade
    for stan in range(st):
        classs = standard()
        sttotal = sttotal + classs
    total = htotal + aptotal + sttotal + bonus
    print("total:", total)
    print(htotal, ":hon")
    print(aptotal, ":ap")
    print(sttotal, ":standard")
    twelvepointgpa = (total / numclasses)
    fourpointgpa = twelvepointgpa / 2.62663185
    goalgpa = float(input("What is your desired GPA?: "))
    pointsaway=(goalgpa-fourpointgpa)
    print("you are ",pointsaway,"from your desired GPA")
    print("I will now calculate your grade.")
    print("calculating.....")
    print(".........")

    print(name, ", your twelve point gpa is :", (twelvepointgpa))
    print("Opening File......")
    openchart()
    print(name, "your four point gpa is approximately ", fourpointgpa)
    again = input("Hope This was successful would you like to run again?")
    if again == "yes":
        intro()
        questions()
    else:
        print("hope to see you next time! :)")


def openchart():
    print("opening chart in 3 seconds...")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 second")
    time.sleep(1)
    print("opening...")
    webbrowser.open("http://www.triton.k12.in.us/Downloads/12%20Point%20Grade%20Scale%20Value.pdf")


intro()
questions()
