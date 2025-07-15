name = "  Ab ,:CD,\tMuSTAfa, mohAmed"
#____________________________
print(name.upper()) #--> بيكبر كله
print(name.lower()) #--> بيصغر كله 
print(name.capitalize()) #--> (بيكبر اول خانة (هنا هو كبر المسافة اللي ف الأول خدبالك
print(name.title()) #--> هنا بيكبر اول حرف فعلي من كل كلمة في الجملة
print(name.swapcase()) #--> بيعكس الحروف 
#________________________________________________________________________________________
print(name.strip())
print(name.lstrip())
print(name.rstrip())
#____________________
print(name.split(",",2)) #--> بيقسم من الشمال لليمين  
print(name.rsplit(",",2))#--> من اليمين للشمال
l = ["mohamed","Khaled"]
print(" ".join(l))
#______________________________________________________
print(name.find("MuSTAfa"))#--> بيقولك الموقع (قبلها كام ديجيت) ولو ملقاش -1
print(name.index("MuSTAfa"))#--> بيقولك الموقع (قبلها كام ديجيت) ولو ملقاش يدي ايرور
print(name.count("m")) #--> case sensetive
#________________________________________________________________________________________
print(name.replace("m",""))
#__________________________
print(name.startswith("  A"))#--> المسافات بتفرق
print(name.endswith("med"))#--> المسافات بتفرق

print(name.isdigit())
print(name.isdecimal())
print(name.isnumeric())

print(name.isalpha())
print(name.isascii())
print(name.isprintable())
print(name.isspace())
print(name.isalnum())

print(name.islower())
print(name.isupper())
print(name.istitle())

print(name.isidentifier())
#____________________________________________________
print(name.encode("utf-8"))#--> utf-8 is deafult
print(type(name.encode())) 
a=b'Rashwan'
print(a.decode())
print(type(a.decode()))
#________________________________________________
b="7"
print(b.zfill(4))#--> بيبقا الطول كله 4
print(name.zfill(50))
print(b.center(7,"-"))
print(name.partition(":"))
print(name.expandtabs(1))#--> بتنحكم في المسافات اللي هتديهالك التاب
#______________________________________________________________________
job = "Engineer"
age = 21
print("I'm an {}, and I'm {}".format(job,age))
print(f"I'm an {job}, and I'm {age}")
