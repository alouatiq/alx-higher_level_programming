#!/usr/bin/python3
"""Module that contains a function to convert a
class instance to JSON-compatible dictionary."""


def class_to_json(obj):
    """Returns the dictionary description for
    JSON serialization of an object."""
    return obj.__dict__
