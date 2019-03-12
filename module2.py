from module1 import CarRentService, Car, RentCar, Client

my_rent_service = CarRentService()

car1 = RentCar("kia", 50)
car2 = RentCar("bmw", 150)
my_rent_service.add_car(car1.model, car1.rent_price)
my_rent_service.add_car(car2.model, car2.rent_price)

print("Все машины сервиса: ", my_rent_service.storage_all)

client1 = Client("Bob")
my_rent_service.rent_car(car1.model, client1.name)

print("Своблодные машины сервиса: ", my_rent_service.free_cars)
print("История заказов: ", my_rent_service.client_base)

my_rent_service.return_car(car1.model, client1.name, 10)

print("Своблодные машины сервиса: ", my_rent_service.free_cars)
my_rent_service.get_total_earnings()

my_rent_service.get_rent_history(car1.model)

my_rent_service.get_client_history(client1.name)

my_rent_service.get_earnings_by_client(client1.name)

client2 = Client("Alex")
my_rent_service.rent_car(car2.model, client2.name)

my_rent_service.return_car(car2.model, client1.name, 120)

print("История заказов: ", my_rent_service.client_base)
my_rent_service.get_rent_history(car2.model)

f = open("base_car.txt", "w")
f.write(",".join(my_rent_service.free_cars))
f.close()
