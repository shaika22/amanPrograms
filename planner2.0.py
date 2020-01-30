import time
import webbrowser

hw = "What is tonight's homework"
due = "When is it due?:"
complete = "Is it completed?:"
assessments = "Do you have any upcoming Tests or Quizzes"
update = "planner updated"


def replaceline(fileName, lineNum, txt):
    lines = open("realplanner.html", "r").readlines()
    lines[lineNum] = txt + "\n"
    planner = open("realplanner.html", "w")
    planner.writelines(lines)
    planner.close()


option = input("Enter what subject to update planner or all: ")


def history():
    print("opened")
    hhw = input(hw)
    hdue = input(due)
    hcomplete = input(complete)
    hassessments = input(assessments)
    replaceline("realplanner.html", 28, "<td>" + hhw + "</td>")  # hw actual num 29
    print(update)
    replaceline("realplanner.html", 29, "<td>" + hdue + "</td>")  # due actual num 30
    print(update)
    replaceline("realplanner.html", 30, "<td>" + hcomplete + "</td>")  # due actual num 30
    print(update)
    replaceline("realplanner.html", 31, "<td>" + hassessments + "</td>")  # due actual num 30
def csp():
    print("opened")
    cshw = input(hw)
    csdue = input(due)
    cscomplete = input(complete)
    csassessments = input(assessments)
    replaceline("realplanner.html", 36, "<td>" + cshw + "</td>")  # hw actual num 37
    print(update)
    replaceline("realplanner.html", 37, "<td>" + csdue + "</td>")  # due actual num 38
    print(update)
    replaceline("realplanner.html", 38, "<td>" + cscomplete + "</td>")  # due actual num 39
    print(update)
    replaceline("realplanner.html", 39, "<td>" + csassessments + "</td>")  # due actual num 40


def advrob():
    print("opened")
    ahw = input(hw)
    adue = input(due)
    acomplete = input(complete)
    aassessments = input(assessments)
    replaceline("realplanner.html", 43, "<td>" + ahw + "</td>")  # hw actual num 44
    print(update)
    replaceline("realplanner.html", 44, "<td>" + adue + "</td>")  # due actual num 45
    print(update)
    replaceline("realplanner.html", 45, "<td>" + acomplete + "</td>")  # due actual num 46
    print(update)
    replaceline("realplanner.html", 46, "<td>" + aassessments + "</td>")  # due actual num 47


def pcal():
    print("opened")
    phw = input(hw)
    pdue = input(due)
    pcomplete = input(complete)
    passessments = input(assessments)
    replaceline("realplanner.html", 50, "<td>" + phw + "</td>")  # hw actual num 51
    print(update)
    replaceline("realplanner.html", 51, "<td>" + pdue + "</td>")  # due actual num 52
    print(update)
    replaceline("realplanner.html", 52, "<td>" + pcomplete + "</td>")  # due actual num 53
    print(update)
    replaceline("realplanner.html", 53, "<td>" + passessments + "</td>")  # due actual num 54


def chem():
    print("opened")
    chw = input(hw)
    cdue = input(due)
    ccomplete = input(complete)
    cassessments = input(assessments)
    replaceline("realplanner.html", 57, "<td>" + chw + "</td>")  # hw actual num 58
    print(update)
    replaceline("realplanner.html", 58, "<td>" + cdue + "</td>")  # due actual num 59
    print(update)
    replaceline("realplanner.html", 59, "<td>" + ccomplete + "</td>")  # due actual num 60
    print(update)
    replaceline("realplanner.html", 60, "<td>" + cassessments + "</td>")  # due actual num 61


def eng():
    print("opened")
    ehw = input(hw)
    edue = input(due)
    ecomplete = input(complete)
    eassessments = input(assessments)
    replaceline("realplanner.html", 64, "<td>" + ehw + "</td>")  # hw actual num 65
    print(update)
    replaceline("realplanner.html", 65, "<td>" + edue + "</td>")  # due actual num 66
    print(update)
    replaceline("realplanner.html", 66, "<td>" + ecomplete + "</td>")  # due actual num 67
    print(update)
    replaceline("realplanner.html", 67, "<td>" + eassessments + "</td>")  # due actual num 68


def arab():
    print("opened")
    ahw = input(hw)
    adue = input(due)
    acomplete = input(complete)
    aassessments = input(assessments)
    replaceline("realplanner.html", 71, "<td>" + ahw + "</td>")  # hw actual num 72
    print(update)
    replaceline("realplanner.html", 72, "<td>" + adue + "</td>")  # due actual num 73
    print(update)
    replaceline("realplanner.html", 73, "<td>" + acomplete + "</td>")  # due actual num 74
    print(update)
    replaceline("realplanner.html", 74, "<td>" + aassessments + "</td>")  # due actual num 75



if option == "history":
    history()
elif option == "comsci":
    csp()
elif option == "robotics":
    advrob()
elif option == "precal":
    pcal()
elif option == "chemistry":
    chem()
elif option == "english":
    eng()
elif option == "arabic":
    arab()
if option == "all":
    print("history: ")
    history()
    print("Computer Science Principles: ")
    csp()
    print("Advanced Robotics: ")
    advrob()
    print("Pre Calculus: ")
    pcal()
    print("Chemistry: ")
    chem()
    print("English: ")
    eng()
    print("Arabic: ")
    arab()
