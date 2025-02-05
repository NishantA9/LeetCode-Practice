class MyCustomClass:
    pass

for item in MyCustomClass():  # Raises TypeError: 'MyCustomClass' object is not iterable
    print(item)
