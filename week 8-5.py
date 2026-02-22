student = {
    "name": "Charansai",
    "age": 20,
    "Department": "Cse"
}
value = "Cse"
print("Reverse Look up for Key")
for key, val in student.items():
    if val == value:
        print("Key for value", value, "is:", key)
