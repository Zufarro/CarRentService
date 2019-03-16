from module1 import CarRentService, Car, RentCar, Client

my_rent_service = CarRentService()

car1 = RentCar("kia", 50)
car2 = RentCar("bmw", 150)
my_rent_service.add_car(car1)
my_rent_service.add_car(car2)

print("Все машины сервиса: ", my_rent_service.storage_all)


client1 = Client("Bob")
my_rent_service.rent_car(car1, client1)

print("Своблодные машины сервиса: ", my_rent_service.free_cars)
print("История заказов: ", my_rent_service.client_base)


my_rent_service.return_car(car1, client1, 10)

print("Своблодные машины сервиса: ", my_rent_service.free_cars)

my_rent_service.get_total_earnings()

my_rent_service.get_rent_history(car1)


my_rent_service.get_client_history(client1)

my_rent_service.get_earnings_by_client(client1)

client2 = Client("Alex")
my_rent_service.rent_car(car2, client2)

my_rent_service.return_car(car2, client1, 120)

print("История заказов: ", my_rent_service.client_base)
my_rent_service.get_rent_history(car2)

f = open("base_car.txt", "w")
f.write(",".join(my_rent_service.free_cars))
f.close()
