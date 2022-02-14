import functions as functions
#from functions import myFun

# def myFun():
#     print("hello kyle")

# functions.myFun()

# myFun()

if __name__=="__main__":
    functions.myFun()
    w = int(input("Enter a width: "))
    h = int(input("Enter a height: "))
    area = functions.computeRectArea(height=h,width=w)
    print(area)