import operations.customer_operation as customer_operation
from utilities.print_with_color import print_error, print_warning, print_success

def add_customer():
    customer_id = int(input("Input Customer ID: "))
    name = str(input("Input Name: "))
    address = str(input("Input Address: "))
    phone_number = str(input("Input Phone Number: "))
    
    is_found = customer_operation.get_customer_with_id(int(customer_id))
    if is_found:
        print_error("Customer ID is already exist")
    else:
        customer_operation.create_one(customer_id, name, address, phone_number)
        show_all_customer()
    
def remove_customer():
    customer_id = input("Input Customer ID: ")
    searched_customer = customer_operation.get_customer_with_id(int(customer_id))
    if not searched_customer:
        print_warning("Not Found")
    else:
        if input("Do you really want to remove? (y/n): ") == "y":
            customer_operation.delete_one_with_customer_id(int(customer_id))
            print_success("Successfuly Removed Data")
        else:
            print_error("Failed Removed Data")
    
def search():
    customer_id = int(input("Input Customer ID: "))
    customer = customer_operation.get_customer_with_id(customer_id)
    
    if customer:
        customer = customer ['data']
        print("\n\n\n")
        print("="*10+"Search Result"+"="*10)
        print(f"ID: {customer['customer_id']}")
        print(f"Name: {customer['name']}")
        print(f"Address: {customer['address']}")
        print(f"Phone Number: {customer['phone_number']}")
    else:
        print_warning("Not Found")
  
def show_all_customer():
    customers = customer_operation.read_many()
    
    if customers:
        print("\n\n\n")
        print("List of Customers")
        for customer in customers:
            print("="*25)
            print(f"ID: {customer['customer_id']}")
            print(f"Name: {customer['name']}")
            print(f"Address: {customer['address']}")
            print(f"Phone Number: {customer['phone_number']}")
    else:
        print_warning("No Data")