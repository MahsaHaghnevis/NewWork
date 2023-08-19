#
##  aug 19
### created by yseeva
## Time manager
#


def subtract_time(t1,t2):
    time={}
    time["h"]=t2["h"]-t1["h"]
    time["mi"]=t2["mi"]-t1["mi"]
    time["se"]=t2["se"]-t1["se"]
    if time["se"]<0:
        time["mi"]-=1
        time["se"]+=60
        
    if time["mi"]<0:
        time["h"]-=1
        time["se"]+=60
        
    if time["h"]<0:
        print("inputs were wrong!")
        time={"h":0 , "mi":0 , "se":0}
        
    return time

def add_time(t1,t2):
    time={}
    time["h"]=t1["h"]+t2["h"]
    time["mi"]=t1["mi"]+t2["mi"]
    time["se"]=t1["se"]+t2["se"]
    if time["se"]>=60:
        time["mi"]+=1
        time["se"]-=60
        
    if time["mi"]>=60:
        time["h"]+=1
        time["se"]-=60
        
    if time["h"]>=24:
        print("it has passed more than a day!")
        time={"h":0 , "mi":0 , "se":0}
    return time

def show(inp):
    print(f"the result is :{inp['h']}: {inp['mi']}: {inp['se']}")
    
def menu():
    print("enter ur enter and exit time in a 24-hour format : ")
    num1=int(input("hour of enter -> "))
    num2=int(input("minute of enter-> "))
    num3=int(input("second of enetr -> "))
    num4=int(input("hour of exit->"))
    num5=int(input("minute of exit->"))
    num6=int(input("second of exit->"))
    print(f"so your enter time was = {num1}:{num2}:{num3} and the exit time is= {num4}:{num5}:{num6}")
    tim1={"h":num1 , "mi":num2 , "se":num3}
    tim2={"h":num4 , "mi":num5 , "se":num6}
    print("you want to add or suntract time ? 1-add 2-suntract")
    opt=int(input())
    if opt==1:
        show(add_time(tim1,tim2))
    elif opt==2:
        show(subtract_time(tim1,tim2))
    else:
        print("wrong input")

    
    

menu()