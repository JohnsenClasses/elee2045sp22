people = {"Kyle":{"height_in":75,"address":"117 Boyd"},"Andrew":{}}
print(list(people.keys()))
print(list(people.values()))


people = {}
people_file = open("people.txt")
people_list = [x.strip() for x in people_file.readlines()]

for line in people_list:
    sections = line.split(":") #turns the colon separated string into a list
    name = sections[0]
    height = int(sections[1])
    address = sections[2]
    if name not in people.keys():
        people[name] = {"height":height,"address":address}
print(people)

for person,info in people.items():
    print(person,info)



