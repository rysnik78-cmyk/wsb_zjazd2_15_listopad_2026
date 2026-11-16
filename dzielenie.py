def podziel(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b



print(podziel(4,5))
print(podziel(4,4))