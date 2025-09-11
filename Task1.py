key = {
    "Viraj" : 93,
    "Manoj" : 85,
    "Ballu" : 78,
    "vivek" : 81,
}

name = input("Enter your student's name: ")
if name in key:
    print(f"{name}'s marks: {key[name]}")
else:
    print("Student not found.")
