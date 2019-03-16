class CarRentService():
    def __init__(self):
        self.storage_all ={}
        self.free_cars = {}
        self.cash_base = []
        self.client_base = {}
        self.car_hisory = {}
        self.earnings_by_clients = {}

    def add_car(self,RentCar):
        self.storage_all[RentCar.model] = RentCar.rent_price
        self.free_cars[RentCar.model] = RentCar.rent_price

    def rent_car(self, RentCar, Client):
        if RentCar.model in self.free_cars:
            del self.free_cars[RentCar.model]
            if Client.name in self.client_base:
                self.client_base[Client.name].append(RentCar.model)
            else:
                self.client_base.update({Client.name:[RentCar.model]})
        elif RentCar.model in self.storage_all and RentCar.model not in self.free_cars:
            print ("Модель", RentCar.model, "арендуется")
        else:
            print ("Модель", RentCar.model, "не найдена")

    def get_total_earnings(self):
        return "Выручка сервиса: " + str(sum(self.cash_base)) + " $"

    def get_client_history(self,Client):
        if Client.name in self.client_base:
            print(Client.name, "у нас арендовывал :",self.client_base[Client.name])
        else:
            print("Клиент "+str(Client.name)+" пока у нас не арендовывал авто")

    def return_car(self, RentCar, Client, hours):
        if hours > 0:
            if RentCar.model in self.storage_all and RentCar.model not in self.free_cars:
                cash = int(self.storage_all.get(RentCar.model))*int(hours)
                self.free_cars.update({RentCar.model:self.storage_all.get(RentCar.model)})
                self.cash_base.append(cash)
                if RentCar.model in self.car_hisory:
                    self.car_hisory[RentCar.model].append(cash)
                else:
                    self.car_hisory.update({RentCar.model:[cash]})
                if  Client.name in self.earnings_by_clients:
                    self.earnings_by_clients[Client.name].append(cash)
                else:
                    self.earnings_by_clients.update({Client.name:[cash]})
            else:
                print(RentCar.model, " - Вы возвращаете не ту машину, которую арендовали!")

    def get_rent_history(self,RentCar):
        if RentCar.model in self.car_hisory:
            print("Автомобиль арендовался:", len(self.car_hisory[RentCar.model]), "раз")
            print("Автомобиль принес доход:", sum(self.car_hisory[RentCar.model]), "$")
        else:
            print("Автомобиль еще не арендовался")

    def get_earnings_by_client(self,Client):
        if Client.name in self.earnings_by_clients:
            print("Клиент принес доход:", sum(self.earnings_by_clients[Client.name]), "$")
        else:
            print("Клиент не найден")


class Car():
    def __init__(self,model):
        self.model = model

class RentCar(Car):
    def __init__(self,model,rent_price):
        super().__init__(model)
        self.rent_price = rent_price

class Client():
    def __init__(self,name):
        self.name = name
