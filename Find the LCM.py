x=int(input("Enter the 1st number >> "))
y=int(input("Enter the 2nd number >> "))

if x>y:
    gerater=x
else:
    gerater=y

while(True):
    if gerater%x==0 and gerater%y==0:
        lcm=gerater
        break
    gerater +=1
print(f"LCM of {x} and {y} is ",gerater)
