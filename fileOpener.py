import os

f = open("planner.txt", "r")

f.close()
his=input("What is tonight's homework for History?: ")
hisd=input("when is it due?:")

csp=input("What is tonight's homework for AP Com Sci?: ")
cspd=input("when is it due?:")

rob=input("What is tonight's homework for Advanced Robotics?: ")
robd=input("when is it due?:")

pc=input("What is tonight's homework for Math?: ")
pcd=input("when is it due?:")

chem=input("What is tonight's homework for Chemistry?: ")
chemd=input("when is it due?:")

eng=input("What is tonight's homework for English?: ")
engd=input("when is it due?:")


g = open("planner2.html", "w")
print("file created")
l = ["<!DOCTYPE html>\n", "<html>\n", "<head>\n", "<style>\n", "table {\n", "  font-family: arial, sans-serif;\n",
     "  border-collapse: collapse;\n", "  width: 100%;\n", "}\n", "td, th {\n", "border: 1px solid #dddddd;\n",
     "text-align: left;\n", "padding: 8px;\n", "}\n", "tr:nth-child(even) {\n", "background-color: #e8effa;\n", "}\n",
     "</style>\n", "</head>\n", "<body>\n", "<table>\n", "<tr>\n", "<th>Class</th>\n",
     "<th>Assignment</th>\n", "<th>Assessments</th>\n", "</tr>\n", "<tr>\n", "<td>Contemporary World History</td>\n",
     "<td>Maria Anders</td>\n", "<td>Germany</td>\n", "</tr>\n", "<tr>\n", "<td>AP Computer Science Principles</td>\n",
     "<td>Francisco Chang</td>\n", "<td>Mexico</td>\n", "</tr>\n", "<tr>\n", "<td>Video Production</td>\n",
     "<td>Roland Mendel</td>\n", "<td>Austria</td>\n", "</tr>\n", "<tr>\n", "<td>PreCal Honors</td>\n",
     "<td>Helen Bennett</td>\n", "<td>UK</td>\n", "</tr>\n", "<tr>\n", "<td>Chemistry Honors</td>\n",
     "<td>Yoshi Tannamuri</td>\n", "<td>Canada</td>\n", "</tr>\n", "<tr>\n", "<td>English II</td>\n",
     "<td>Giovanni Rovelli</td>\n", "<td>Italy</td>\n", "</tr>\n", "<tr>\n", "<td>Arabic</td>\n",
     "<td>Giovanni Rovelli</td>\n", "<td>Italy</td>\n", "</tr>\n", "</table>\n", "</body>\n", "</html>"]
print("planner2.txt opened")
g.writelines(l)

g.close()
