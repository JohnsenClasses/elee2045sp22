file_handle = open("data/data.txt") #results in a file object
file_contents = file_handle.read()
print(file_contents)
file_handle.close() #allows the file to be opened again later

#another way is to consume the file as a list of lines

file_handle = open("data/data.txt") #results in a file object
file_lines = file_handle.readlines()
file_numbers = [int(line)**2 for line in file_lines if int(line) > 5] #convert the list of strings to a list of integers
print(file_numbers)
file_handle.close() #allows the file to be opened again later

#repeating the above using a for loop

file_handle = open("data/data.txt") #results in a file object
file_lines = file_handle.readlines()
file_numbers = []
for line in file_lines:
    num = int(line)
    if num > 5:
        file_numbers.append(num**2)
print(file_numbers)
file_handle.close() #allows the file to be opened again later


#repeating the above, this time reading line by line

file_handle = open("data/data.txt") #results in a file object
file_numbers = []
while True:
    line = file_handle.readline()
    if line == '': break
    num = int(line)
    if num > 5:
        file_numbers.append(num**2)
print(file_numbers)
file_handle.close() #allows the file to be opened again later