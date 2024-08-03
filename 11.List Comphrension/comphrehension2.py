my_list = [i for i in range(1, 11) if i % 2 == 0]
print(my_list)  # [2, 4, 6, 8, 10]

"For Prime Numbers"
my_list = [i for i in range(1, 11) if is_prime_number(i)]
print(my_list)  # [1,2,3,5,7]
