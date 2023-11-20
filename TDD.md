# Python Testing Examples with `pytest`

## Table of Contents

0. [Red, Green, Refactor](#0-red-green-refactor)
1. [Basic Value Assertions](#1-basic-value-assertions)
2. [Testing for Exceptions](#2-testing-for-exceptions)
3. [Collection Assertions](#3-collection-assertions)
4. [Floating Point Comparisons](#4-floating-point-comparisons)
5. [Object State and Behavior Testing](#5-object-state-and-behavior-testing)
6. [Class Instance Testing](#6-class-instance-testing)
7. [Testing Object Methods and Side Effects](#7-testing-object-methods-and-side-effects)

## 0. Red, Green, Refactor

Write the Smallest Possible Test Case: Start by writing a very small and specific test for a tiny piece of functionality. This test should initially fail because the functionality has not been implemented yet.

Write Just Enough Code to Pass the Test: Write only the amount of code necessary to make the test pass. The focus here is on simplicity and meeting the test requirements, not on writing comprehensive or final implementations.

Refactor the Code: Once the test passes, refactor the code. This includes cleaning up, removing duplication, and ensuring that the code adheres to good design principles. The key here is to make the code as clean and efficient as possible without altering its functionality.

Repeat the Process: After refactoring, write the next test, and continue the cycle of test, code, and refactor. This iterative process encourages building the software in small, manageable increments.

Focus on One Test at a Time: Work on one test and corresponding functionality at a time. Avoid the temptation to write multiple tests for different functionalities before making them pass.

Green-Red-Green Cycle: Remember the TDD mantra - "Red, Green, Refactor":

    Red: Write a test that fails (since the feature isn’t implemented yet).
    Green: Write just enough code to make the test pass.
    Refactor: Clean up the code while keeping the test green (passing).

## 1. Basic Value Assertions

### Expect True or False

```python
def is_even(number):
    return number % 2 == 0

def test_is_even():
    assert is_even(4)
    assert not is_even(5)
```

### Expect Equality

```python
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5
```

### Expect Greater or Less Than

```python
def subtract(a, b):
    return a - b

def test_greater_than():
    assert subtract(10, 5) > 0

def test_less_than():
    assert subtract(2, 5) < 0
```

## 2. Testing for Exceptions

### Expect an Exception

```python
def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

## 3. Collection Assertions

### Expect a List Contains a Value

```python
def test_contains_value():
    my_list = [1, 2, 3, 4, 5]
    assert 3 in my_list
```

## 4. Floating Point Comparisons

### Expect Approximate Equality

```python
def test_float_equality():
    assert (0.1 + 0.2) == pytest.approx(0.3)
```

## 5. Object State and Behavior Testing

### Expect an Object to Have Specific Attributes

```python
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_object_attributes():
    obj = MyClass("Test", 100)
    assert obj.name == "Test"
    assert obj.value == 100
```

## 6. Class Instance Testing

### Expect Object to Be an Instance of a Class

```python
def test_instance_of_class():
    obj = MyClass("Test", 100)
    assert isinstance(obj, MyClass)
```

## 7. Testing Object Methods and Side Effects

### Expect Methods to Return Correct Results

```python
class Calculator:
    def add(self, a, b):
        return a + b

def test_add_method():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
```

### Expect Changes to Object State

```python
class Counter:
    def __init__(self):
    self.count = 0

    def increment(self):
        self.count += 1

def test_counter_increment():
    counter = Counter()
    counter.increment()
    assert counter.count == 1
```

### Expect Side Effects

```python
class Logger:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

def test_logging():
    logger = Logger()
    logger.log("Test Message")
    assert "Test Message" in logger.messages
```
