import operations.rent_operation as rent_operation
import operations.car_operation as car_operation
import operations.customer_operation as customer_operation
from utilities.print_with_color import print_error, print_warning, print_success


def rent_transaction():
    customer_id = int(input("Input Customer ID: ")) 
    car_number = int(input("Input Car Number: "))
    
    customer = customer_operation.get_customer_with_id(customer_id)
    if not customer:
        print_error("Customer Not Found")
    else:
        car = car_operation.get_car_with_car_number(car_number)
        if not car:
            print_error("Car Not Found")
        elif car ['data'] ['status'] == "Unavailable":
            print_error("Car is not available")
        else:
            rent_operation.create_one(customer_id, car_number, False)
            car_operation.update_status_car(car_number, False)
            print_success("Successfuly Rented Car")
    
def return_transaction():
    car_number = int(input("Input Car Number: "))
    transactions = rent_operation.get_transaction_with_car_number(car_number)
    car = car_operation.get_car_with_car_number(car_number)
    
    if len(transactions) > 0:
        for transaction in transactions:
            if transaction ['data'] ['status'] == "rented":
                transaction ['data'] ['status'] = "returned"
                car_operation.cars[car['index']]['status'] = 'Available'
                print_success("Successfuly Returned Car")
    else:
        print_error("Car Number Not Found")
            
def search():
    car_number = int(input("Input Car Number: "))
    transactions = rent_operation.get_transaction_with_car_number(car_number)
    
    if transactions:
        print("\n\n\n")
        print("="*10+"Search Result"+"="*10)
        for transaction in transactions:
            print(f"Customer ID: {transaction ['data']['customer_id']}")
            print(f"Car Number: {transaction ['data']['car_number']}")
            print(f"Status: {transaction ['data'] ['status']}")
            
            print("="*25)
    else:
        print_warning("Not Found")
  
def show_all_transactions():
    transactions = rent_operation.read_many()
    
    if transactions:
        print("\n\n\n")
        print("List of Transaction")
        for transaction in transactions:
            print("="*25)
            print(f"Customer ID: {transaction['customer_id']}")
            print(f"Car Number: {transaction['car_number']}")
            print(f"Status: {transaction ['status']}")
    else:
        print_warning("No Data")