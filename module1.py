class CarRentService():
    def __init__(self):
        self.storage_all ={}
        self.free_cars = {}
        self.cash_base = []
        self.client_base = {}
        self.car_hisory = {}
        self.earnings_by_clients = {}

    def add_car(self,model,price):
        self.storage_all[model] = price
        self.free_cars[model] = price

    def rent_car(self, rent_model, client_name):
        if rent_model in self.free_cars:
            del self.free_cars[rent_model]
            if client_name in self.client_base:
                self.client_base[client_name].append(rent_model)
            else:
                self.client_base.update({client_name:[rent_model]})
        elif rent_model in self.storage_all and rent_model not in self.free_cars:
            print ("Модель", rent_model, "арендуется")
        else:
            print ("Модель", rent_model, "не найдена")

    def get_total_earnings(self):
        return "Выручка сервиса: " + str(sum(self.cash_base)) + " $"

    def get_client_history(self,find_client):
        if find_client in self.client_base:
            print(find_client, "у нас арендовывал :",self.client_base[find_client])
        else:
            print("С таким именем не было клиента")

    def return_car(self, return_model, client_name, hours):
        if hours > 0:
            if return_model in self.storage_all and return_model not in self.free_cars:
                cash = int(self.storage_all.get(return_model))*int(hours)
                self.free_cars.update({return_model:self.storage_all.get(return_model)})
                self.cash_base.append(cash)
                if return_model in self.car_hisory:
                    self.car_hisory[return_model].append(cash)
                else:
                    self.car_hisory.update({return_model:[cash]})
                if  client_name in self.earnings_by_clients:
                    self.earnings_by_clients[client_name].append(cash)
                else:
                    self.earnings_by_clients.update({client_name:[cash]})
            else:
                print(return_model, " - Вы возвращаете не ту машину, которую арендовали!")

    def get_rent_history(self,model):
        if model in self.car_hisory:
            print("Автомобиль арендовался:", len(self.car_hisory[model]), "раз")
            print("Автомобиль принес доход:", sum(self.car_hisory[model]), "$")
        else:
            print("Автомобиль еще не арендовался или отсутсвует в сервисе")

    def get_earnings_by_client(self,find_name):
        if find_name in self.earnings_by_clients:
            print("Клиент принес доход:", sum(self.earnings_by_clients[find_name]), "$")
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
