def test_greeting():
    """
    Write a program that displays a greeting.
    """
    name = "Anna"
    age = 25
    # TODO Form the required string
    output = f"Hello, {name}! You are {age} years old."

    # Check the result
    assert output == "Hello, Anna! You are 25 years old."

def test_rectangle():
    """
    Write a program that takes the length and width of a rectangle
    and calculates its perimeter and area.
    """
    a = 10
    b = 20
    # TODO calculate the perimeter
    perimeter = 2 * (a + b)

    assert perimeter == 60

    # TODO calculate the area
    area = a * b

    assert area == 200

import math

def test_circle():
    """
    Write a program that takes the radius of a circle
    and calculates its area and circumference.
    Use the PI constant.
    """
    r = 23
    # TODO calculate the area
    area = math.pi * r ** 2
    assert area == 1661.9025137490005
    # TODO calculate the circumference
    length = 2 * math.pi * r
    assert length == 144.51326206513048

import random

def test_random_list():
    """
    Create a list of 10 random numbers from 1 to 100 (inclusive) and sort it in ascending order.
    """
    # TODO create the list
    l = sorted([random.randint(1, 100) for _ in range(10)])
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))

def test_unique_elements():
    """
    Remove all duplicate elements from the list.
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO remove duplicate elements
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    """
    Create a dictionary from two lists.
    Use the first list as keys and the second as values.
    Hint: use the built-in zip function.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO create the dictionary
    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
