
print("Enter Marks Obtained in this three Subject. English, Math, Data: ")
English = int(input())
Math = int(input())
Data = int(input())
total = English+Math+Data
Score = total/3
if Score>=69 and Score<=100:
    print("A")
elif Score>=59 and Score<70:
    print("B")
elif Score>=49 and Score<60:
    print("C")
elif Score>=39 and Score<50:
    print("D")
elif Score>=29 and Score<40:
    print("E")
elif Score>=0 and Score<30:
    print("F")
else:
    print("not allowed!")