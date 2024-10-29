from utilities.print_with_color import *
import managements.car_management as car_management 
import managements.customer_management as customer_management
import managements.rent_management as rent_management

def car_menu():
    print("\n\nCar Management")
    print("[1] Add Car")
    print("[2] Remove Car")
    print("[3] Search Car")
    print("[4] Show All Cars")
    print("[0] Back To Previous\n")
    
    chosenMenu = int(input('Masukan Pilihan: '))
    print('\n')
    
    if chosenMenu == 1:
        car_management.add_car()
        car_menu()
    elif chosenMenu == 2:
        car_management.remove_car()
        car_menu()
    elif chosenMenu == 3:
        car_management.search()
        car_menu()
    elif chosenMenu == 4:
        car_management.show_all_cars()
        car_menu()
    elif chosenMenu == 0:
        main_menu()
    else:
        print_error("Choose the correct number!")
        
def customer_menu():
    print("\n\nCustomer Management")
    print("[1] Add Customer")
    print("[2] Remove Customer")
    print("[3] Search Customer")
    print("[4] Show All Customers")
    print("[0] Back To Previous\n")
    
    chosenMenu = int(input('Masukan Pilihan: '))
    print('\n')
    
    if chosenMenu == 1:
        customer_management.add_customer()
        customer_menu()
    elif chosenMenu == 2:
        customer_management.remove_customer()
        customer_menu()
    elif chosenMenu == 3:
        customer_management.search()
        customer_menu()
    elif chosenMenu == 4:
        customer_management.show_all_customer()
        customer_menu()
    elif chosenMenu == 0:
        main_menu()
    else:
        print_error("Choose the correct number!")
        
def rent_menu():
    print("\n\nRent Management")
    print("[1] Rent Transaction")
    print("[2] Return Transaction")
    print("[3] Search Transaction")
    print("[4] Show All Transactions")
    print("[0] Back To Previous\n")
    
    chosenMenu = int(input('Masukan Pilihan: '))
    print('\n')
    
    if chosenMenu == 1:
        rent_management.rent_transaction()
        rent_menu()
    elif chosenMenu == 2:
        rent_management.return_transaction()
        rent_menu()
    elif chosenMenu == 3:
        rent_management.search()
        rent_menu()
    elif chosenMenu == 4:
        rent_management.show_all_transactions()
        rent_menu()
    elif chosenMenu == 0:
        main_menu()
    else:
        print_error("Choose the correct number!")

def main_menu():
    print("\n\n\nWelcome to Car Rental")
    print("[1] Management Car")
    print("[2] Management Customer")
    print("[3] Management Rent")
    print("[0] Close The Program\n")
    
    chosenMenu = int(input('Masukan Pilihan: '))
    print('\n')
    
    
    if chosenMenu == 1:
        car_menu()
    elif chosenMenu == 2:
        customer_menu()
    elif chosenMenu == 3:
        rent_menu()
    elif chosenMenu == 0:
        close_program()
    else:
        print_error("Choose the correct number!")
        
def close_program():
    print("Do you really want to close the program?(y/n) ", end='')
    
    if input() == "y":
        exit(1)
    else:
        main_menu()