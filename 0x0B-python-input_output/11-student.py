#!/usr/bin/python3
"""Module that defines a Student class
with serialization and deserialization."""


class Student:
    """Represents a student with first
    name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with
        the provided attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary
        representation of a Student instance.
        If attrs is a list of strings
        only those attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {
                key: value for key,
                value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of
        the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
