contactBook=[]
#function to add contact
def adding_contact():
  name=input("Enter the name:")
  email=input("Enter the Email:")
  mobile=input("Enter the mobile number:")
  contactBook.append({"Name" : name,"Email" : email,"Mobile" : mobile})
  print(f"Contact of {name} is added successfully")

#function to view contact
def view_contact():
  if  len(contactBook)==0:
    print("There are no contacts")
  else:
    print("Contacts :")
   
    for contact in contactBook:
     print(contact)
#function to search contact
def search_contact():
  name=input("Enter the name of contact")
  found = False
  for contact in contactBook:
      if contact["Name"].lower() == name.lower():
          found = True
          print(contact)
      if not found:
          print(f"contact of {name} is not found")
#save contacts to text file        
def saveto_file():
    with open("contactBook.txt", "w") as file:
        for contact in contactBook:
            file.write(f"{contact['Name']},{contact['Mobile']},{contact['Email']}\n")
    print("Contacts saved to file")
        
#Loading contacts from file
def loadingFrom_file():
    try:
        with open("contactBook.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, mobile, email = parts
                    contactBook.append({"Name": name, "Mobile": mobile, "Email": email})
                else:
                    print(f"Skipping invalid line: {line.strip()}")
        print("Contacts loaded from contactBook.txt")
    except FileNotFoundError:
        print("No contacts file found.")
#main program
while True:
  print("Contact Book Menu:")
  print("1.Add a contact")
  print("2.View a contact")
  print("3.Search for a contact")
  print("4.To load from file")
  print("5.Exit")

  choice = input("Enter your choice 1/2/3/4")
  if choice=="1":
    adding_contact()
    saveto_file()
  elif choice=="2":
    view_contact()
  elif choice=="3":
    search_contact()
  elif choice=='4':
    loadingFrom_file()
  elif choice=="5":
    print("Contact book has exited successfully")
    break
    

  else:
    print("Invalid choice ")