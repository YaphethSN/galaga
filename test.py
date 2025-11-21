some_value = 2

class my_class:
    private_value = some_value

my_first_class = my_class()

some_value = 10
my_second_class = my_class()

print(my_first_class.private_value)
print(my_second_class.private_value)