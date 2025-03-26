def get_person_details():
    """
    Function to read a person's detrails from the keyboard.
    """
    name=input("enter your name:")
    address=input("enter youyr address:")
    email=input("enter your email:")
    phone=input("enter your phone number:")
    return name,adress, email,phone

def print_person_details(name,address,email,phone):
    """
    function to print a person's details.
    """
    print("\n--Personal Details--")
    print(f"Name:{name}")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"Phone Number:{phone}")
#get details from the user
name,address,email,phone=get_person_details()
#print the details
print_person_details(name,address,email,phone)
