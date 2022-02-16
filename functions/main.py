import functions as functions
#from functions import myFun

# def myFun():
#     print("hello kyle")

# functions.myFun()

# myFun()

if __name__=="__main__":
    functions.myFun()
    
    w,h = functions.get_width_and_height_from_user()
    area = functions.computeRectArea(w,h)
    print(area)

    width_and_height = functions.get_width_and_height_from_user()
    area = functions.computeRectArea(height=width_and_height[1],
                                     width=width_and_height[0])
    print(area)

    a_list = [2,3,4,1]
    functions.process_list(a_list.copy())
    print(a_list)
