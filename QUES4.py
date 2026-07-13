# Rank Participants
# A sports academy has recorded the timings (in seconds) of participants in a race. Write a program to arrange the timings from the fastest to the slowest so that the winners can be announce

n = int(input("Enter number of participants: "))
time = []
for i in range(n):
    time.append(float(input("Enter timing: ")))
time.sort()
print("Fastest to Slowest:", time)
