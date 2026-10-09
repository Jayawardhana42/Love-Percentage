import time

print("birth day match eka check karamu")

b1 = input("your bday (yymmdd): ")
b2 = input("crush bday (yymmdd): ")

print("processing...")
time.sleep(1)

# podi logic ekak
n1 = sum([int(i) for i in b1 if i.isdigit()])
n2 = sum([int(i) for i in b2 if i.isdigit()])

score = (n1 + n2) % 100

print("match score:", score, "%")

if score > 75:
    print("sira match eka! goniye danna puluwan xD")
elif score > 40:
    print("podi try ekak dila balapan ithin")
else:
    print("epa ban wena kenek balaganin lol")
