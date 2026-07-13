# Employee Salary Report
# An HR department has employee salary records collected from two different branches. Write a program to combine both lists and display all salaries in ascending order

list1 =[]
list2 =[]

n1 = int(input("list1 employes: "))
for i in range(n1):
    list1.append(int(input("enter salary:")))
n2 = int(input("list2 employes: "))
for i in range(n2):
    list2.append(int(input("enter salary: ")))

list3 = list1 + list2
list3.sort()

print("employe's salary's:",list3)