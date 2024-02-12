class Automobile:
    """
    Базовый класс автомобилей.
    """

    def __init__(self, make: str, model: str):
        """
        Инициализация экземпляра класса.
        Example:
        >>> auto = Automobile("BMW", "x6")
        """
        self._make = make  # марка
        self._model = model  # модель

    def improve_characteristic(self):
        """
        Метод производит некоторые изменения в характеристике автомобиля.
        """
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None

    @property
    def make(self):
        """Возвращает марку автомобиля."""
        return self._make  # внутри класса обращаемся к защищенному атрибуту

    @property
    def model(self):
        """Возвращает модель автомобиля."""
        return self._model  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Автомобиль {self.make}. Марка {self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.make!r}, author={self.model!r})"


class PassengerCar(Automobile):
    """ Производный класс. Пассажирские автомобили. """

    def __init__(self, make: str, mark: str, kol_passengers: int):
        """
        Инициализация экземпляра класса.
        Example:
        >>> auto = Automobile("BMW", "x6", 5)
        """
        super().__init__(make, mark)
        self.kol_passengers = kol_passengers

    def improve_characteristic(self):
        """
        Метод повышает вместительность легковушки.(на 1-го человека)
        """
        print(f"Вызван метод класса {self.__class__.__name__}")
        self.kol_passengers = self.kol_passengers + 1
        return self.kol_passengers

    @property
    def kol_passengers(self):
        """Возвращает вместимость людей в автомобиле."""
        return self._kol_passengers  # внутри класса обращаемся к защищенному атрибуту

    @kol_passengers.setter
    def kol_passengers(self, new_kol_passengers: int) -> None:
        """Устанавливает вместимость людей в автомобиле."""
        if not isinstance(new_kol_passengers, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_kol_passengers <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._kol_passengers = new_kol_passengers

    def __str__(self):
        return f"Легковушка {self.make}. Модель {self.mark}. Вместимость по кол-ву человек {self.kol_passengers} "

    def __repr__(self):
        return f"{self.__class__.__name__}(make={self.make!r}, mark={self.mark!r}, kol_passengers={self.kol_passengers!r})"


class Truck(Automobile):
    """ Производный класс. Грузовые автомобили. """

    def __init__(self, make: str, mark: str, cargo_weight: int):
        """
        Инициализация экземпляра класса.
        Example:
        >>> auto = Automobile("KAMAZ", "65115", 14)
        """
        super().__init__(make, mark)
        self.cargo_weight = cargo_weight

    def improve_characteristic(self):
        """
        Метод повышает грузоподъемность грузовика (на 1 тонну).
        """
        print(f"Вызван метод класса {self.__class__.__name__}")
        self.cargo_weight = self.cargo_weight + 1
        return self.cargo_weight

    @property
    def cargo_weight(self):
        """Возвращает вместимость груза в тоннах."""
        return self._cargo_weight  # внутри класса обращаемся к защищенному атрибуту

    @cargo_weight.setter
    def cargo_weight(self, new_cargo_weight: int) -> None:
        """Устанавливает вместимость груза в тоннах."""
        if not isinstance(new_cargo_weight, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_cargo_weight <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._cargo_weight = new_cargo_weight

    def __str__(self):
        return f"Легковушка {self.make}. Модель {self.mark}. Вместимость груза в тоннах {self.cargo_weight} "

    def __repr__(self):
        return f"{self.__class__.__name__}(make={self.make!r}, mark={self.mark!r}, cargo_weight={self.cargo_weight!r})"


if __name__ == "__main__":
    pass