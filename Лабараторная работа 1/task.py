from abc import ABC, abstractmethod
import doctest

class MaterialObject(ABC):
    def __init__(self, weight: float, volume: float) -> None:
        """
        Создает материальный объект с указанным весом и объемом.

        :param weight: Вес объекта.
        :type weight: float
        :param volume: Объем объекта.
        :type volume: float

        :raises ValueError: если вес или объем отрицательны.
        >>> materialobject = MaterialObject(10.0, 5.0)
        """

        self._weight = self._validate_weight(weight)
        self._volume = self._validate_volume(volume)

    def _validate_weight(self, weight: float) -> float:
        """
        Производит валидацию веса объекта.

        :param weight: Вес объекта.
        :type weight: float

        :return: Вес объекта.
        :rtype: float
        >>> materialobject = MaterialObject(10.0, 5.0)
        >>> materialobject._validate_weight(10.0)
        10.0
        """
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number.")
        return weight
    # ... код валидации ...

    def _validate_volume(self, volume: float) -> float:
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("Volume must be a positive number.")
        return volume
     # ... код валидации ...

    @abstractmethod
    def get_weight(self) -> float:
        """
        Возвращает вес объекта.

        :return: Вес объекта.
        :rtype: float
        >>> materialobject = MaterialObject(10.0, 5.0)
        >>> materialobject.get_weight(10.0)
        10.0
        """
        pass

    @abstractmethod
    def get_volume(self) -> float:
        """Возвращает объем объекта."""
        pass

    @abstractmethod
    def move_to(self, destination: str) -> None:
        """
        Перемещает объект в указанное место.

        :param destination: Место, куда нужно переместить объект.
        :type destination: str
        """
        pass

    @abstractmethod
    def calculate_density(self) -> float:
        """Вычисляет плотность объекта."""
        pass

    @abstractmethod
    def change_state(self, new_state: str) -> None:
        """
        Изменяет состояние объекта.

        :param new_state: Новое состояние объекта.
        :type new_state: str
        """
        pass


class ImmaterialObject(ABC):
    def __init__(self, is_transparent: bool, is_phantom: bool) -> None:
        self._is_transparent = self._validate_transparency(is_transparent)
        self._is_phantom = self._validate_phantom(is_phantom)
        # ... проводится валидация ...

    def _validate_transparency(self, is_transparent: bool) -> bool:
        if not isinstance(is_transparent, bool):
            raise ValueError("Transparency must be a boolean value.")
        return is_transparent
        # ... код валидации ...

    def _validate_phantom(self, is_phantom: bool) -> bool:
        if not isinstance(is_phantom, bool):
            raise ValueError("Phantom property must be a boolean value.")
        return is_phantom
        # ... код валидации ...

    @abstractmethod
    def is_transparent(self) -> bool:
        """Определяет, является ли объект прозрачным."""
        pass

    @abstractmethod
    def is_phantom(self) -> bool:
        """Определяет, является ли объект фантомом."""
        pass

    @abstractmethod
    def change_opacity(self, new_opacity: int) -> None:
        """
        Изменяет прозрачность объекта.

        :param new_opacity: Новый уровень прозрачности.
        :type new_opacity: int
        """
        pass

    @abstractmethod
    def change_phantom_state(self, new_state: str) -> None:
        """
        Изменяет состояние объекта на фантомное или обратно.

        :param new_state: Новое состояние объекта.
        :type new_state: str
        """
        pass


class ObjectWithArbitraryProperties(ABC):
    def __init__(self, properties: dict) -> None:
        self._properties = self._validate_properties(properties)
    # ... проводится валидация ...

    def _validate_properties(self, properties: dict) -> dict:
        if not isinstance(properties, dict):
            raise ValueError("Properties must be a dictionary.")
        return properties
        # ... код валидации ...

    @abstractmethod
    def get_properties(self) -> dict:
        """Получает свойства объекта."""
        pass

    @abstractmethod
    def update_property(self, key: str, value: str) -> None:
        """
        Обновляет указанное свойство новым значением.

        :param key: Ключ для обновления.
        :type key: str
        :param value: Новое значение свойства.
        :type value: str
        """
        pass

    @abstractmethod
    def delete_property(self, key: str) -> None:
        """
        Удаляет указанное свойство.

        :param key: Ключ для удаления.
        :type key: str
        """
        pass

    @abstractmethod
    def analyze(self) -> str:
        """Анализирует объект и генерирует отчет об анализе."""
        pass


if __name__ == "__main__":
    doctest.testmod()
