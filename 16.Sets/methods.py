# Mutable
set1 = {88, 46, 22, 47, 96, 32, 12, 54, 54, 54, 54}
print(set1)

set1.add(100)
print(set1)  # {96, 32, 12, 46, 47, 22, 54, 88}

set1.remove(32)
print(set1)  # {96, 100, 12, 46, 47, 22, 54, 88}

# set1.clear()
# print(set1)  # set()

# set2 = set1
# set2.add(199)
# print(set2)  # {96, 100, 199, 12, 46, 47, 22, 54, 88}
# print(set1)  # {96, 100, 199, 12, 46, 47, 22, 54, 88}

set2 = set1.copy()
set2.add(199)
print(set2)  # {96, 100, 199, 12, 46, 47, 22, 54, 88}
print(set1)  # {96, 100, 12, 46, 47, 22, 54, 88}
