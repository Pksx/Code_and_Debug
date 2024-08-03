# Spread/Splat
# *args always in tuple


# Ex:1
def add(n1, n2, *n3):
    print(f"n1->{n1}")
    print(f"n2->{n2}")
    print(f"n3->{n3}")


add(10, 20, 30, 40, 50, 60)
# Output
# n1=10
# n2=20
# n3=(30, 40, 50, 60)
add(10, 20)
# Output
# n1=10
# n2=20
# n3=()


# *args
# Ex:2
def add(n1, n2, *args):
    print(f"n1->{n1}")
    print(f"n2->{n2}")
    print(f"n3->{args}")


add(10, 20, 30, 40, 50, 60)
# Output:
# n1->10
# n2->20
# n3->(30, 40, 50, 60)


# EX:3
def add(*args):
    print(f"num ->{args}")


add(10, 20, 30, 40)  # Output -> num ->(10, 20, 30, 40)


# Ex:4
# Toget ssum using tuple
def add(n1, n2, *args):
    print(f"n1->{n1}")
    print(f"n2->{n2}")
    print(f"n3->{sum(args)}")


add(10, 20, 30, 40, 50, 60)
# Output
# n1->10
# n2->20
# n3->180


# Ex:4
def add(n1, n2, *args):
    print(f"n1->{n1}")
    print(f"n2->{n2}")
    print(f"n3->{args}")


add(10, 20, 30, "John", 44.55)
# Output:
# n1->10
# n2->20
# n3->(30, 'John', 44.55)
