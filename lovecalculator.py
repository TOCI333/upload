
print("love calculator")
print("love accuaracy")

name=input("enter your name: ")
name2=input("enter the second name: ")

name3=name.lower()
name4=name2.lower()

#for true love

fort=name3.count("t")
forr=name3.count("r")
foru=name3.count("u")
fore=name3.count("e")

for_love_l=name3.count("l")
for_love_o=name3.count("o")
for_love_v=name3.count("v")
for_love_e=name3.count("e")

#for second name

fort1=name4.count("t")
forr1=name4.count("r")
foru1=name4.count("u")
fore1=name4.count("e")

for_love_l1=name4.count("l")
for_love_o1=name4.count("o")
for_love_v1=name4.count("v")
for_love_e1=name4.count("e")

#lasuma
t=fort+fort1
r=forr+forr1
u=foru+foru1
e=fore+fore1

l=for_love_l+for_love_l1
o=for_love_o+for_love_o1
v=for_love_v+for_love_v1
e1=for_love_e+for_love_e1

true=t+r+u+e
love=l+o+v+e1

#a string
true1=str(true)
love1=str(love)
total=true1+love1


print(f"your score is {total}%")

var1=int(total)

if var1<=10 and var1>=90:
    print("YOU GO TOGETHER LIKE COKE AND MENTOS =()")
elif var1>=40 and var1<=50:
    print("YOU ARE ALRIGHT TOGETHER =)")

print(f"T occurs {t}")
print(f"r occurs {r}")
print(f"u occurs {u}")
print(f"e occurs {e}")
print(f"total {t+r+u+e} ")

print(f"l occurs {l}")
print(f"o occurs {o}")
print(f"v occurs {v}")
print(f"e occurs {e}")
print(f"total {l+o+v+e} ")

print("thanks for using, Created by Isaac Tolentino")
