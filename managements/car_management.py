import operations.car_operation as car_operation
from utilities.print_with_color import print_error, print_warning, print_success

def add_car():
    id = int(input("Input ID: "))
    car_number = int(input("Input Car Number: "))
    brand = str(input("Input Brand: "))
    model = str(input("Input Model: "))
    year = int(input("Input Year: "))
    status = int(input("Status Available?(0/1): "))
    
    is_found = car_operation.get_car_with_car_number(int(car_number))
    if is_found:
        print_error("Car Number is already exist")
    else:
        car_operation.create_one(id, car_number, brand, model, year, status)
        show_all_cars()
    
def remove_car():
    car_number = input("Input Car Number: ")
    searched_car = car_operation.get_car_with_car_number(int(car_number))
    if not searched_car:
        print_warning("Not Found")
    else:
        if input("Do you really want to remove? (y/n): ") == "y":
            car_operation.delete_one_with_car_number(int(car_number))
            print_success("Successfuly Removed Data")
        else:
            print_error("Failed Removed Data")
    
def search():
    search_by = str(input("Input Search By (car_number/brand/model): "))
    
    if search_by.lower() == "car_number":
        car_number = int(input("Input Car Number: "))
        search_result = car_operation.get_car_with_car_number(int(car_number))
        
        print("\n\n\n")
        print("="*10+"Search Result"+"="*10)
        
        if search_result:
            search_result = search_result ['data']
            print(f"ID: {search_result['car_id']}")
            print(f"Car Number: {search_result['car_number']}")
            print(f"Brand: {search_result['brand']}")
            print(f"Model: {search_result ['model']}")
            print(f"Year: {search_result ['year']}")
            print(f"Status: {search_result ['status']}")
        else:
            print_warning("No Data")
    
    elif search_by.lower() == "brand":
        brand = str(input("Input Brand: "))
        search_result = car_operation.get_car_with_brand(brand)
        
        print("\n\n\n")
        print("="*10+"Search Result"+"="*10)
        
        if len(search_result) > 0:
            for car in search_result:
                print(f"ID: {car ['data']['car_id']}")
                print(f"Car Number: {car ['data']['car_number']}")
                print(f"Brand: {car ['data']['brand']}")
                print(f"Model: {car ['data'] ['model']}")
                print(f"Year: {car ['data'] ['year']}")
                print(f"Status: {car ['data'] ['status']}")
                
                print("="*25)
        else:
            print_warning("No Data")
            
    elif search_by.lower() == "model":
        model = str(input("Input Model: "))
        search_result = car_operation.get_car_with_model(model)
        
        print("\n\n\n")
        print("="*10+"Search Result"+"="*10)
        
        if len(search_result) > 0:
            for car in search_result:
                print(f"ID: {car ['data']['car_id']}")
                print(f"Car Number: {car ['data']['car_number']}")
                print(f"Brand: {car ['data']['brand']}")
                print(f"Model: {car ['data'] ['model']}")
                print(f"Year: {car ['data'] ['year']}")
                print(f"Status: {car ['data'] ['status']}")
                
                print("="*25)
        else:
            print_warning("No Data")
            
    else:
        print_error("Input Invalid!")
  
def show_all_cars():
    cars = car_operation.read_many()
    
    if cars:
        print("\n\n\n")
        print("List of Cars")
        for car in cars:
            print("="*25)
            print(f"ID: {car['car_id']}")
            print(f"Car Number: {car['car_number']}")
            print(f"Brand: {car['brand']}")
            print(f"Model: {car ['model']}")
            print(f"Year: {car ['year']}")
            print(f"Status: {car ['status']}")
    else:
        print_warning("No Data")