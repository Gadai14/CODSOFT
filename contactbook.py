from beautifultable import BeautifulTable

class Contact_Book:
    def __init__(self):
        self.__data = {}
    
    def addContact(self, name=None, address=None, phone_number=None, email=None):
        if name and address and phone_number and email:
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, address, phone_number, email]
                print("Added successfully")
            else:
                print("Phone number already exists")
        else:
            print("Please enter all the values")

    def deleteContact(self, phone_number=None):
        if phone_number:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Phone number does not exist in the database")
        else:
            print("Please enter a phone number")

    def editContact(self, phone_number=None, name=None, address=None, email=None):
        if phone_number and phone_number in self.__data:
            if name:
                self.__data[phone_number][0] = name
            if address:
                self.__data[phone_number][1] = address
            if email:
                self.__data[phone_number][3] = email
            print("Contact updated successfully")
        else:
            print("Phone number does not exist in the database")

    def searchContact(self, query=None, sort_field=None):
        if query:
            search_results = []
            for key, val in self.__data.items():
                if query.lower() in " ".join(val).lower():
                    search_results.append(val)
            
            if sort_field:
                try:
                    sort_index = {"name": 0, "address": 1, "phone_number": 2, "email": 3}[sort_field]
                    search_results.sort(key=lambda x: x[sort_index])
                except KeyError:
                    print("Invalid sort field. Sorting by name by default.")
                    search_results.sort(key=lambda x: x[0])
            
            self.viewContact(search_results)
        else:
            print("Please enter a valid query")

    def viewContact(self, data):
        table = BeautifulTable()
        table.columns.header = ["Name", "Address", "Phone Number", "Email"]
        
        for index, contact in enumerate(data, start=1):
            table.rows.append(contact)
        
        print(table)

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    self.addContact(name, address, phone_number, email)
                
                elif choice == 2:
                    phone_number = input("Phone Number: ")
                    self.deleteContact(phone_number)
                
                elif choice == 3:
                    phone_number = input("Phone Number: ")
                    name = input("Name (leave blank to skip): ")
                    address = input("Address (leave blank to skip): ")
                    email = input("Email (leave blank to skip): ")
                    self.editContact(phone_number, name, address, email)
                
                elif choice == 4:
                    query = input("Search query: ")
                    sort_by = input("Sort by (name/address/phone_number/email, leave blank for default): ")
                    self.searchContact(query, sort_by)
                
                elif choice == 5:
                    self.viewContact(self.__data.values())
                
                elif choice == 6:
                    break
                
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            
            except ValueError:
                print("Invalid input. Please enter a number.")

            except Exception as e:
                print(f"An error occurred: {e}")

# Running the contact book console
if __name__ == "__main__":
    contact_book = Contact_Book()
    contact_book.console()
