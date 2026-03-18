from time import time

def somemath(thing1, thing2):
    print(f"Doing some math with {thing1} and {thing2}")
    if time() % 2 == 0:
        return thing1 + thing2
    return thing1 - thing2