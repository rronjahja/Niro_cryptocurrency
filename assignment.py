# 1 Create two variables - one with your name and one with your age
# user_name='Rron'
# user_age=25
user_name = input('Enter your name: ')
user_age = input('Enter your age,too: ')


# 2 Create a function which prints your data as one string
def print_user_data():
    print(user_name + ' - ' + user_age)


print_user_data()


# 3 Create a function which prints ANY data (two arguments) as one string
def print_concatenated_data(el1, el2):
    print(el1 + el2)


print_concatenated_data(user_name, user_age)


# 4 Create a function which calculates and returns the number of decades you already lived (e.g. 23=2 decades)
def calculate_decades(age):
    decades_lived = age // 10
    return decades_lived


decades = calculate_decades(int(user_age))
print(decades)
