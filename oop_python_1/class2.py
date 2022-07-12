from class3 import Verification


class V2(Verification):
    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open("users") as r:
            for i in r:
                if f"{self.login, self.password}" + "\n" == i:
                    raise ValueError("Такой есть")
        super().save()

    def show(self):
        return self.login, self.password


x = V2("Bob", "123456789", 25)
