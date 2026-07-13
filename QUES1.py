# Student Roll Number Search
# A teacher has stored the roll numbers of students in a list in the order they registered. The list is not sorted. Write a program to check whether a given roll number exists in the list. If found, display its position; otherwise, print "Student Not Found."

Studentroll = [11,12,13,14,15,16,17,20]
search = int(input("enter num: "))
if search in Studentroll:
    print("Student found roll num :", search)
else:
    print("Student not found")