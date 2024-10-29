transactions = []
status_type = ['rented', 'returned']

def create_one(customer_id: int, car_number: int, hasReturned: bool):
    transaction = {}
    transaction['customer_id'] = int(customer_id)
    transaction['car_number'] = int(car_number)
    transaction['status'] = str(status_type[hasReturned])
    
    transactions.append(transaction)
    
    return transaction

def get_transaction_with_customer_id(customer_id: int): 
    for index, transaction in enumerate(transactions):
        if transaction['customer_id'] == customer_id:
            return {
                'index': index,
                'data': transaction
            }
    return False

def get_transaction_with_car_number(car_number: int): 
    result = []
    for index, transaction in enumerate(transactions):
        if transaction['car_number'] == car_number:
            result.append({
                'index': index,
                'data': transaction
            })
    return result

def delete_one_with_transaction_id(transaction_id: int):
    transaction = get_transaction_with_customer_id(int(transaction_id))
    if transaction: 
        transactions.pop(transaction['index'])
        return True
    return False
    
def read_many():
    return transactions