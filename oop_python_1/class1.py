# 'объект - едница информации в памяти'
# 'экземпляр - конкретный объект какогото класса'
# 'класс - инструкция по созданию объектов определенного типа'
# 'метод - функции в классе для воздействия на объект'


class Purse:
    def __init__(self, valuta, name="Unknown"):
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print("Не достаточно средств")
            raise ValueError("Не достаточно средств")
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print("Кошелек удален")


x = Purse("USD")
y = Purse("EUR", "Bill")
y.top_up_balance(10)
x.top_up_balance(7)
x.info()
y.info()

