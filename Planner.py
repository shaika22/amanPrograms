import time
import webbrowser

# list of variables to initialize
# his = ""
# hisd = ""
# hco = ""
# hc = ""
# ha = ""
# csp = ""
# cspd = ""
# cco = ""
# csc = ""
# ca = ""
# rob = ""
# robd = ""
# rco = ""
# rc = ""
# ra = ""
# pc = ""
# pcd = ""
# pco = ""
# pcc = ""
# pa = ""
# chem = ""
# chemd = ""
# ccolor = ""
# cc = ""
# cha = ""
# eng = ""
# engd = ""
# eco = ""
# ec = ""
# ea = ""
# arab = ""
# arabd = ""
# aco = ""
# ac = ""
# aa = ""

name = "Aman"
option = input("Hello " + name + ", Input HW by (subject)or(all)")
due = "When is it due?:"
complete = "Is it completed?:"
assessments = "Do you have any upcoming Tests or Quizzes"


def historyHW():
    his = input("What is tonight's homework for History?: ")
    hisd = input(due)
    hc = input(complete)
    if hc == "yes":
        hco = " bgcolor=MediumSeaGreen"
    else:
        hco = " bgcolor=Tomato"
    ha = input(assessments)
    g.writelines(lines)
    openchart()
    return his, hisd, hc, hco, ha


def comsciHW():
    csp = input("What is tonight's homework for AP Com Sci?: ")
    cspd = input(due)
    csc = input(complete)
    if csc == "yes":
        cco = " bgcolor=MediumSeaGreen"
    else:
        cco = " bgcolor=Tomato"
    ca = input(assessments)
    updateChart()
    openchart()


def advrobHW():
    rob = input("What is tonight's homework for Advanced Robotics?: ")
    robd = input(due)
    rc = input(complete)
    if rc == "yes":
        rco = " bgcolor=MediumSeaGreen"
    else:
        rco = " bgcolor=Tomato"
    ra = input(assessments)
    updateChart()
    openchart()


def pcalHW():
    pc = input("What is tonight's homework for Math?: ")
    pcd = input(due)
    pcc = input(complete)
    if pcc == "yes":
        pco = " bgcolor=MediumSeaGreen"
    else:
        pco = " bgcolor=Tomato"
    pa = input(assessments)
    updateChart()
    openchart()


def chemHW():
    chem = input("What is tonight's homework for Chemistry?: ")
    chemd = input(due)
    cc = input(complete)
    if cc == "yes":
        ccolor = " bgcolor=MediumSeaGreen"
    else:
        ccolor = " bgcolor=Tomato"
    cha = input(assessments)
    updateChart()
    openchart()


def engHW():
    eng = input("What is tonight's homework for English?: ")
    engd = input(due)
    ec = input(complete)
    if ec == "yes":
        eco = " bgcolor=MediumSeaGreen"
    else:
        eco = " bgcolor=Tomato"
    ea = input(assessments)
    updateChart()
    openchart()


def arabHW():
    arab = input("What is tonight's homework for Arabic?: ")
    arabd = input(due)
    ac = input(complete)
    if ac == "yes":
        aco = " bgcolor=MediumSeaGreen"
    else:
        aco = " bgcolor=Tomato"
    aa = input(assessments)
    updateChart()
    openchart()


def allHomeWork():
    historyHW()
    comsciHW()
    advrobHW()
    arabHW()
    engHW()
    chemHW()
    pcalHW()
    openchart()


def retry():
    if option == "all":
        allHomeWork()
    if option == "history":
        historyHW()
    if option == "comsci":
        comsciHW()
    if option == "robotics":
        advrobHW()
    if option == "arabic":
        arabHW()
    if option == "english":
        engHW()
    if option == "chemistry":
        chemHW()
    if option == "math":
        pcalHW()


g = open("realplanner.html", "w")
print("file created")


def openchart():
    print("opening chart in 3 seconds............................")
    time.sleep(1)
    print("2 seconds............................")
    time.sleep(1)
    print("1 second............................")
    time.sleep(1)
    print("opening............................")
    webbrowser.open("file:///C:/Users/Aman%20Shaik/PycharmProjects/aman's%20programs/realplanner.html")


def updateChart():
    g.writelines(lines)
    print("Chart Updated")


lines = ["<html>\n", "<head>\n", "<style>\n", "body {\n", "background-color: #e4f0f0;\n", "}\n", "table {\n",
         "  font-family: arial, sans-serif;\n",
         "  border-collapse: collapse;\n", "  width: 100%;\n", "}\n", "td, th {\n", "border: 1px solid #000000;\n",
         "text-align: left;\n", "padding: 8px;\n", "}\n", "}\n",
         "</style>\n", "</head>\n", "<body>\n", "<table>\n", "<tr>\n", "<th>Class</th>\n",
         "<th>Assignment</th>\n", "<th>DUE</th>\n", "<th>Completion</th>\n", "<th>Upcoming Assessments</th>\n",
         "</tr>\n", "<tr>\n",
         "<td>Contemporary World History</td>\n",
         "<td>" + his + "</td>\n", "<td>" + hisd + "</td>\n", "<td" + hco + ">" + hc + "</td>\n",
         "<td>" + ha + "</td>\n",
         "</tr>\n", "<tr>\n",
         "<td>AP Computer Science Principles</td>\n",
         "<td>" + csp + "</td>\n", "<td>" + cspd + "</td>\n", "<td" + cco + ">" + csc + "</td>\n",
         "<td>" + ca + "</td>\n""</tr>\n", "<tr>\n",
         "<td>Advanced Robotics</td>\n",
         "<td>" + rob + "</td>\n", "<td>" + robd + "</td>\n", "<td" + rco + ">" + rc + "</td>\n",
         "<td>" + ra + "</td>\n""</tr>\n",
         "<tr>\n",
         "<td>PreCal Honors</td>\n",
         "<td>" + pc + "</td>\n", "<td>" + pcd + "</td>\n", "<td" + pco + ">" + pcc + "</td>\n",
         "<td>" + pa + "</td>\n""</tr>\n",
         "<tr>\n",
         "<td>Chemistry Honors</td>\n",
         "<td>" + chem + "</td>\n", "<td>" + chemd + "</td>\n", "<td" + ccolor + ">" + cc + "</td>\n",
         "<td>" + cha + "</td>\n" "</tr>\n", "<tr>\n",
         "<td>English II</td>\n",
         "<td>" + eng + "</td>\n", "<td>" + engd + "</td>\n", "<td" + eco + ">" + ec + "</td>\n",
         "<td>" + ea + "</td>\n""</tr>\n",
         "<tr>\n",
         "<td>Arabic</td>\n",
         "<td>" + arab + "</td>\n", "<td>" + arabd + "</td>\n", "<td" + aco + ">" + ac + "</td>\n",
         "<td>" + aa + "</td>\n""</tr>\n", "</table>\n",
         "</body>\n", "</html>"]

if option == "all":
    allHomeWork()
elif option == "history":
    historyHW()
elif option == "comsci":
    comsciHW()
elif option == "robotics":
    advrobHW()
elif option == "arabic":
    arabHW()
elif option == "english":
    engHW()
elif option == "chemistry":
    chemHW()
elif option == "math":
    pcalHW()
else:
    print("not a valid answer, try again")
    retry()

g.close()
