Contacts = 3

contactDict = {}

for i in range(Contacts):
    name = input("Enter Name " )
    number1 = input("Enter number1 " )
    number2 = input("Enter number2 " )
    email = input("Enter email " )

    contactDict[name] = {
    "name":name,
    "number1":number1,
    "number2":number2,
    "email":email,
    }


print(contactDict.get("Name"))