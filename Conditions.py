temp = 30 
if temp > 35:
    print("الجو حر")
elif temp > 25:
    print("الجو دافي")
else:
    print("الجو بارد")
#-----------------------------------------------
x = 10 
result = "Even" if x % 2 == 0 else "Odd"
print(result)
#------------------OR---------------------------
print("Even") if x % 2 == 0 else print("Odd") 
#-----------------------------------------------
score = 84
grade = "A" if score >= 85 else "B" if score >= 75 else "C"
print(grade)
#-----------------------------------------------
a = 10
b = 20
if a == 10 and b == 20 : print(True)
if all([a == 10, b==20, x == 10, result.lower() == "even" ]) :
    print(True)
#------------------------------------------------
language = "Python"
match language :
    case "Python":
        print("You choose python")
    case _:
        print("You don't choose python")
#------------------------------------------------
