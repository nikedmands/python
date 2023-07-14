from classes import User

Nik = User("Nik Edmands", "13051990")
print(Nik.name)
print(Nik.first_name)
print(Nik.last_name)
print(Nik.birthday)

# get a helpful overview of the class details with the call in the next line
# help(User)

print(Nik.age())