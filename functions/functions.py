def myFun():
    print("hello world")

def computeRectArea(width,height=3):
    area = width*height
    return area

def get_width_and_height_from_user():
    w = int(input("Enter a width: "))
    h = int(input("Enter a height: "))
    return (w,h)

def process_list(b_list):
    b_list[0] = -5