"""
Logical Operator
(To Operate on 2 or more conditions)

and
condition1 condition2 result
f           f           f
f           t           f
t           f           f
t           t           t

or
c1 c2 result
f   f   f
f   t   t
t   f   t
t   t   t


Not
Reverses the Result


"""

# EX:1
# physics = 33
# chemistry = 33

# print(physics > 33 or chemistry >= 33)

# Ex:2
# physics = 33
# chemistry = 33

# print(not (physics > 33))


# Ex:3
# physics = 23
# chemistry = 21

# print(not physics > 33 and chemistry > 33)
# Not F and F
# Not of F is T and F
# Ans is  F

# Ex:5
physics = 23
chemistry = 21

print(not physics > 33 and not chemistry > 33)
print(not (physics > 33 and chemistry > 33))
