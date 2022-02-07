
test_list = [3,2,1,3,4,5,7]

# this code prints each element in the test_list on subsequent lines
for element in test_list:
    print(element)

#this is another way, but I'll comment it for now

# for index in range(0,len(test_list)):
#     print(test_list[index])

print(test_list)
print(test_list[3:]) # this is better
print(test_list[3:6]) # this is the same (For this list)
print(test_list[3:len(test_list)]) #also the same, but much worse
print(test_list[:3]) #first 3 items of the list

print(test_list[len(test_list)-1]) #this is bad, but it will work
print(test_list[-1]) #this is much better, to refer to the end of the list
print(test_list[::-1]) #reverse string
print(list(reversed(test_list))) #much better 

another_list = test_list.copy() #need to make a copy (shallow copy) to edit without changing the original list
another_list[3] = 18
print(test_list)

a_third_list = another_list

print(id(another_list),id(a_third_list))

print(list(sorted(test_list)))

another_list.sort(reverse=True)
another_list.reverse()

print(another_list) #another way to sort (really the preferred way)

numbers = []
for i in range(0,11):
    numbers.append(i)

print(numbers)

# for i in range(0,11):
#     numbers[i] = numbers[i]**2

numbers = [x**2 for x in range(0,11)] # a better way to square the numbers

print(numbers)
