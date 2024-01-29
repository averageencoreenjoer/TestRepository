## Final task

1. Let's create a base class `Animal` and a child class `Cat`.

In the base `Animal` class we implement the `__init__` constructor, as well as the `__str__` and `__repr__` magic methods. These methods allow you to represent objects as strings and in program code, respectively.

The `Cat` child class will inherit these methods, but can also extend or overload them if necessary.

1. Now we have the ability to inherit and overload methods in the `Cat` child class.

Let's first implement inheritance of one method from the `Animal` base class. Let's say we want to extend the `make_sound()` method, which will return the sound made by an animal.

We can also overload the method to return a cat-specific sound and justify this choice in the method documentation.

1. We can now make some attributes and methods non-public to ensure encapsulation. This will improve security and help hide implementation details from the outside world.

Let's make the age attribute in the `Animal` class and the `make_sound()` method in the `Cat` class private.

The age field in the `Animal` class can be made private to prevent direct modification of the animal's age, and justify this decision in a comment. The `make_sound` method in the `Cat` class can also be made private with justification in the method documentation.

1. Let's add type annotations for all arguments and outputs of methods in the `Animal` and `Cat` classes.

Prior to this, Python 3.5 and later added support for type annotations, which allow you to specify the argument and return types of methods. Although the Python interpreter does not strictly check these annotations, they can still be useful for documentation and static code analysis tools.

## Conclusion

We have created a program that defines two classes: `Animal` and `Cat`. The `Animal` class represents a general description of an animal, storing its species and age, and allowing the creation of general animal sounds. The `Cat` class inherits these attributes and methods from the `Animal` class, adding the ability to make a cat-like sound.

We've also made improvements to the program by adding type annotations for method arguments and output, detailed comments and documentation for classes and methods, and using encapsulation for certain attributes.

This program can be used as a basis for modeling various types of animals. For example, it can serve as the basis for creating an extensive model of a zoo or veterinary information system that requires storing information about different types of animals, their ages, and special characteristics such as typical sounds or the specific features of certain species.

Additionally, the program can be used for educational purposes to demonstrate object-oriented programming principles such as inheritance, encapsulation, and polymorphism.

Thus, the created program is an example of an object-oriented animal model that can be used for various practical or educational purposes.

Kishko Roman, Saint-Petersburg Politech University, 2024