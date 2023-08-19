#
## aug 19
### creatd by yseeva
## fractions
#
#the code provides a simple way to perform arithmetic operations on fractions.
result={}
def add_fraction(fr1,fr2):
    result["s"]=(fr1["s"]*fr2["m"])+(fr2["s"]*fr1["m"])
    result["m"]=fr1["m"]*fr2["m"]
    return result

def subtract_fraction(fr1 , fr2):
    result["s"]=(fr1["s"]*fr2["m"])-(fr2["s"]*fr1["m"])
    result["m"]=fr1["m"]*fr2["m"]
    return result

def multiple_fraction(fr1,fr2):
    result["s"]=fr1["s"]*fr2["s"]
    result["m"]=fr1["m"]*fr2["m"]
    return result

def divide_fraction(fr1,fr2):
    result["s"]=fr1["s"]*fr2["m"]
    result["m"]=fr1["m"]*fr2["s"]
    return result

def Show(sth):
    print(f"result is = {sth['s']}/{sth['m']}")
    

def menu():
    while 1:
        num1=float(input("enter head of ur fraction 1 : "))
        num2=float(input("enter down of ur fraction 1 : "))
        if num2==0.0:
            print("it can't be zero!")
            while 1:
                num2=float(input("enter down of ur fraction 1 : "))
                if num2!=0:
                    break
        num3=float(input("enter head of ur fraction 2 : "))
        num4=float(input("enter down of ur fraction 2 : "))
        if num4==0.0:
            print("it can't be zero!")
            while 1:
                num4=float(input("enter down of ur fraction 2 : "))
                if num4!=0:
                    break
                
        print(f"so ur fractions are :\n --> {num1}/{num2} and --> {num3}/{num4} right? enter yes or no")
        ans=input()
        if ans=="yes" or ans=="Yes" or ans=="YES" or ans=="YEs" or ans=="yES" or ans=="yeS":
            break
        else:
            print("okay lets try again") 
    d1={"s":num1 , "m":num2}
    d2={"s":num3 , "m":num4}
    print("what u wanna do?\n -> 1-add ->2-subtract ->3-multiply  ->4-divide")
    option=int(input())
    if option==1:
        Show(add_fraction(d1,d2))
    elif option==2:
        Show(subtract_fraction(d1,d2))
    elif option==3:
        Show(multiple_fraction(d1,d2))
    elif option==4:
        Show(divide_fraction(d1,d2))
    else:
        print("invalid input")


menu()