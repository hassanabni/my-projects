faculty = ["Uzair", "Ali", "Samad", "Usman", "Saifullah"]
cofounder = faculty[3:5]
print(cofounder)

new_faculty = faculty[0:3]
print(new_faculty)

recent_faculty = new_faculty.pop(1)
print(recent_faculty)

new_faculty.insert(1, "umair")
print(new_faculty)

