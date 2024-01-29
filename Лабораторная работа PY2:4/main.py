class Animal:
    def __init__(self, species: str, age: int) -> None:
        """
        Initialize an Animal object.

        Args:
            species (str): The species of the animal.
            age (int): The age of the animal.

        Note:
            The age parameter is indicated as private to encapsulate the age attribute.

        """
        self.species = species
        self._age = age  # Let's make the _age attribute private for encapsulation
        # age let's make _age to prevent direct modification of the animal's age

    def __str__(self) -> str:
        """
        Return a string representation of the Animal object.

        Returns:
            str: A string representing the animal's species and age.

        """
        return f"This is a {self.species} aged {self._age}."

    def __repr__(self) -> str:
        """
        Return a string representation of the Animal object for debugging.

        Returns:
            str: A string representing the animal's species and age.

        """
        return f"Animal('{self.species}', {self._age})"

    def make_sound(self) -> str:
        """
        Return a generic animal sound.

        Note:
            This method is intended for internal use and should not be accessed directly from outside the class.

        Returns:
            str: A string representing a generic animal sound.

        """
        return "Some generic animal sound"


class Cat(Animal):
    def __init__(self, name: str, species: str, age: int) -> None:
        """
        Initialize a Cat object.

        Args:
            name (str): The name of the cat.
            species (str): The species of the cat.
            age (int): The age of the cat.

        """
        super().__init__(species, age)
        self.name = name

    def __str__(self) -> str:
        """
        Return a string representation of the Cat object.

        Returns:
            str: A string representing the cat's name, species, and age.

        """
        return f"This is {self.name}, a {self.species} aged {self._age}."

    def __repr__(self) -> str:
        """
        Return a string representation of the Cat object for debugging.

        Returns:
            str: A string representing the cat's name, species, and age.

        """
        return f"Cat('{self.name}', '{self.species}', {self._age})"

    def _make_sound(self) -> str:
        """
        Return the sound of a Cat.

        Note:
            Cats typically make a 'meow' sound. Overriding the generic make_sound method to provide a specific sound for cats.

        Returns:
            str: A string representing the sound of a cat.

        """
        return "Meow"


if __name__ == "__main__":
    # Usage example:
    animal = Animal("Dog", 3)
    print(animal)  # Will display: This is a Dog aged 3.
    print(repr(animal))  # Will display: Animal('Dog', 3)
    print(animal.make_sound())  # Will display: Some generic animal sound

    cat = Cat("Whiskers", "Cat", 5)
    print(cat)  # Will display: This is Whiskers, a Cat aged 5.
    print(repr(cat))  # Will display: Cat('Whiskers', 'Cat', 5)
    print(cat._make_sound())  # Will display: Meow