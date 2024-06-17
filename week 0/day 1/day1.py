from datetime import datetime

n = 13
s = 9
print(f"multiplication: {n*s}")


number = 987
if number % 2 == 0:
    print("even")
else:
    print("odd")


why = "daddy is a stupid ass uhh 10 words"

# okay = why[:3]
# print(okay)
# okay = why[-3:]
# print(okay)

# okay = why[3:13]
# print(okay)

# words = why.split(" ")
# why = words[::-1]
# okay = " ".join(why)
# print(okay)

# okay = why[::-1]
# print(okay)

# why2 = "and more shit"
# okay = why + " " + why2
# print(okay)

# okay2 = f"{why2} {why}"
# print(okay2)

# okay = why.replace("daddy", "bob")
# # print(okay)

# okay = why.replace("daddy","")
# print(okay)

# bday = datetime(year = 2008,  month = 2, day = 21)
# time = datetime.now()
# old = time - bday
# age = old.days/365.25
# print(f"age {round(age, 1)}")

bday = datetime(year = 2008,  month = 2, day = 21)
time = datetime(year = 2049,  month = 6, day = 3)
old = time - bday
age = old.days/365.25
print(f"age {round(age, 0)}")

