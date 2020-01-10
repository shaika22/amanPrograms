import time
import webbrowser
# his = ''
# hisd = ''
# hc = ''
# csp = ''
# cspd = ''
# csc = ''
# rob = ''
# robd = ''
# rc = ''
# pc = ''
# pcd = ''
# pcc = ''
# chem = ''
# chemd = ''
# cc = ''
# eng = ''
# engd = ''
# ec = ''
# arab = ''
# arabd = ''
# ac = ''
# def allHomeWork():
#     historyHW()
#     comsciHW()
#     advrobHW()
#     pcalHW()
#     chemHW()
#     engHW()
#     arabHW()

# def historyHW():
his = input("What is tonight's homework for History?: ")
hisd = input("when is it due?:")
hc = input("Is it completed?:")

# def comsciHW():
csp = input("What is tonight's homework for AP Com Sci?: ")
cspd = input("when is it due?:")
csc = input("Is it completed?:")
#
#
# def advrobHW():
rob = input("What is tonight's homework for Advanced Robotics?: ")
robd = input("when is it due?:")
rc = input("Is it completed?:")

#
# def pcalHW():
pc = input("What is tonight's homework for Math?: ")
pcd = input("when is it due?:")
pcc = input("Is it completed?:")

# def chemHW():
chem = input("What is tonight's homework for Chemistry?: ")
chemd = input("when is it due?:")
cc = input("Is it completed?:")

# def engHW():
eng = input("What is tonight's homework for English?: ")
engd = input("when is it due?:")
ec = input("Is it completed?:")

# def arabHW():
arab = input("What is tonight's homework for Arabic?: ")
arabd = input("when is it due?:")
ac = input("Is it completed?:")

# option = input("Hello Aman, what do you want me to input(subject)(all):")
# if option == "all":
#     allHomeWork()
# if option=="history":
#     historyHW()
# if option=="comsci":
#     comsciHW()
# if option=="robotics":
#     advrobHW()
# if option=="arabic":
#     arabHW()
# if option=="english":
#     engHW()
# if option=="chemistry":
#     chemHW()

g = open("planner2.html", "w")
print("file created")
l = ["<html>\n", "<head>\n", "<style>\n", "table {\n", "  font-family: arial, sans-serif;\n",
     "  border-collapse: collapse;\n", "  width: 100%;\n", "}\n", "td, th {\n", "border: 1px solid #dddddd;\n",
     "text-align: left;\n", "padding: 8px;\n", "}\n", "tr:nth-child(even) {\n", "background-color: #e8effa;\n", "}\n",
     "</style>\n", "</head>\n", "<body>\n", "<table>\n", "<tr>\n", "<th>Class</th>\n",
     "<th>Assignment</th>\n", "<th>Assessments</th>\n","<th>Completion</th>\n" "</tr>\n", "<tr>\n", "<td>Contemporary World History</td>\n",
     "<td>" + his + "</td>\n", "<td>" + hisd + "</td>\n", "<td>" + hc + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>AP Computer Science Principles</td>\n",
     "<td>" + csp + "</td>\n", "<td>" + cspd + "</td>\n", "<td>" + csc + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>Video Production</td>\n",
     "<td>" + rob + "</td>\n", "<td>" + robd + "</td>\n", "<td>" + rc + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>PreCal Honors</td>\n",
     "<td>" + pc + "</td>\n", "<td>" + pcd + "</td>\n", "<td>" + pcc + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>Chemistry Honors</td>\n",
     "<td>" + chem + "</td>\n", "<td>" + chemd + "</td>\n", "<td>" + cc + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>English II</td>\n",
     "<td>" + eng + "</td>\n", "<td>" + engd + "</td>\n", "<td>" + ec + "</td>\n", "</tr>\n", "<tr>\n",
     "<td>Arabic</td>\n",
     "<td>" + arab + "</td>\n", "<td>" + arabd + "</td>\n", "<td>" + ac + "</td>\n", "</tr>\n", "</table>\n",
     "</body>\n", "</html>"]

def openchart():
    print("opening chart in 3 seconds...")
    time.sleep(1)
    print("2 seconds")
    time.sleep(1)
    print("1 second")
    time.sleep(1)
    print("opening...")
    webbrowser.open("file:///C:/Users/Aman%20Shaik/PycharmProjects/aman's%20programs/planner2.html")
print("planner2.txt opened")
g.writelines(l)
g.close()
openchart()
print("Planner updated")