
# 🚗 OOP Revision Notes (Python)

This file is a compact reference for revising key Object-Oriented Programming (OOP) concepts in Python, using a car-themed example. All examples are taken from `oop_revision.py`.

---

## 📘 Topics Covered

### 1. Basic Class and Objects
**Example:**
```python
class Car():
    ...
my_first_car = Car("BMW","X5")
```

---

### 2. Class Method and `self`
- `self` refers to the instance of the class.
- Used to access attributes and methods.

**Example:**
```python
def getbrand(self):
    return self.__brand
```

---

### 3. Inheritance
- Allows a class to inherit attributes and methods from another.

**Example:**
```python
class ElectricCar(Car):
    ...
```

---

### 4. Encapsulation
- Restricting direct access to attributes using `__`.

**Example:**
```python
self.__brand = brand
def getbrand(self):
    return self.__brand
```

---

### 5. Polymorphism
- Method overriding in child classes.

**Example:**
```python
def get_fuletype(self): return "Petrol or Disel"  # in Car
def get_fuletype(self): return "Electric Charge"  # in ElectricCar
```

---

### 6. Class Variables
- Shared among all instances of the class.

**Example:**
```python
total_car = 0
Car.total_car += 1
```

---

### 7. Static Method
- Doesn't use `self` or `cls`.

**Example:**
```python
@staticmethod
def description():
    return "Baaj bno baaj, LaundiyaBaaj nhi"
```

---

### 8. Property Decorators
- Accessor for attributes as if they are public properties.

**Example:**
```python
@property
def getmodel(self):
    return self.__model
```

---

### 9. Class Inheritance and `isinstance()`
- To check if an object is an instance of a class or its subclass.

**Example:**
```python
print(isinstance(tesla, Car))
print(isinstance(tesla, ElectricCar))
```

---

### 10. Multiple Inheritance (Concept Only)
- When a class inherits from more than one class.

**Syntax:**
```python
class FlyingCar(Car, AirVehicle):
    ...
```
**Note:** This is not implemented in the code file, but good to know for completeness.

---

### 🔚 Quick Summary
- ✅ Real-life analogy with cars makes concepts easier.
- ✅ Covers encapsulation, inheritance, polymorphism, decorators, etc.
- ✅ Clean examples using simple class design.

---

Happy Revising! 💻✨
