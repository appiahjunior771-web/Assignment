#task1
s="LESSON"
def to_lowercase(s):
    s.lower()
    return 
#task 2
    def swap_case(s):
        s.swapcase()
    return 
#task 
    def remove_uppercase(s):
     join(c for cin in s if not c.isupper())
     return
#task 4   
def count_case(s):
    upper=sum(1 for c in s if c.isupper())
    lower=sum(1 for c in s if c.islower())
    return f"uppercase:{upper},lowercase:{lower}"
    
#task 5
def remove_non_letters(s):
    join(c for c in s if c.isaplha())

    return
#task 6
import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
#task 7
def format_names(names):
    for name in names:
        print(name.center(20,""))

#task 8
import string
def clean_string(s):
    s=s.strip()
    s="".join(c for c in s if c not in string.punctuation)
    s=s.replace("","")
    return s