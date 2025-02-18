from car import car
from account import account
from user import UberX
from user import user

if __name__ == "__main__":
    print("Inicializando las info de los carros")
    print("Car")
    car = car("AMS256", Acount("Andres Herrera", "ASD12365",
    "danielpenad0@gmail.com","2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    UberX = UberX("KLO365", Account("Marco Lois", "SGHJ1236",
    "danielpenad0@gmail.com","7856"), "Toyota", "Corolla")
    print(vars(UberX))
    print(vars(userX.driver))

    print("User")
    user = User("Mariana Valle", "SDFG125F", "danielpenad0@gmail.com",
    "7856")
    print(vars(user))