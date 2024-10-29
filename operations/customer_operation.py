customers = []

def create_one(customer_id: int, name: str, address: str, phone_number: str):
    customer = {}
    customer['customer_id'] = int(customer_id)
    customer['name'] = str(name)
    customer['address'] = str(address)
    customer['phone_number'] = str(phone_number)
    
    customers.append(customer)
    
    return customer

def get_customer_with_id(customer_id: int):
    for index, customer in enumerate(customers):
        if customer['customer_id'] == customer_id:
            return {
                "index": index,
                "data": customer
            }
    return False

def delete_one_with_customer_id(customer_id: int):
    customer = get_customer_with_id(int(customer_id))
    if customer: 
        customers.pop(customer["index"])
        return True
    return False

def read_many():
    return customers