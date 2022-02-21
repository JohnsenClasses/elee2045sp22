from eleemath import Vector3

a_vector3 = Vector3(3,4,5)

print(a_vector3)
print(a_vector3 + a_vector3)
print(a_vector3.add(a_vector3))
print(a_vector3.__add__(a_vector3))
print(a_vector3 + 7)
print(a_vector3[0])
print(f"{len(a_vector3)}")
print(f"{a_vector3.length():.2f}")

print(a_vector3.scale(7)) #this is going to modify a_vector3
print(a_vector3)
print(a_vector3.dot(a_vector3))