cars = []
status_type = ["Unavailable", "Available"]

def create_one(car_id: int, car_number: int, brand: str, model: str, year: int, status: str):
    car = {}
    car['car_id'] = car_id
    car['car_number'] = car_number
    car['brand'] = brand
    car ['model'] = model
    car ['year'] = year
    if status.lower() == 'true':
        car['status'] = "Available"
    else:
        car['status'] = "Unavailable"
    
    cars.append(car)
    
    return car
    
def get_car_with_car_number(car_number: int): 
    for index, car in enumerate(cars):
        if car['car_number'] == car_number:
            return {
                "index": index,
                "data": car
            }
    return False

def get_car_with_brand(brand: str): 
    result = []
    for index, car in enumerate(cars):
        if car['brand'] == brand:
            result.append({
                "index": index,
                "data": car
            })
    return result

def get_car_with_model(model: str): 
    result = []
    for index, car in enumerate(cars):
        if car ['model'] == model:
            result.append({
                "index": index,
                "data": car
            })
    return result

def delete_one_with_car_number(car_number: int):
    car = get_car_with_car_number(car_number)
    if car: 
        cars.pop(car["index"])
        return True
    return False

def update_status_car(car_number: int, status: bool):
    car_searched = get_car_with_car_number(car_number)
    if car_searched:
        index = car_searched["index"]
        car = car_searched ['data']
        
        car ['status'] = status_type[status]
        cars[index] = car
        
        return True
    return False
    
def read_many():
    return cars