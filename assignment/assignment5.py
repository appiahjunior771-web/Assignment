name=input("please enter your name:");
num=input("please enter a number:")
if int(num)% 2==0:
    result="even"
else:
    result="odd"
    print(f"Hello,{name}!,The number{num}is {result}.")
