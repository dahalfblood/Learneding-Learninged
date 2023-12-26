# def print_fever_check(temperature):
#       NORMAL_TEMP = 98.6
#       CUTOFF_TEMP = 95
#       degrees_of_fever = 0
#       if (temperature > NORMAL_TEMP):
#            degrees_of_fever = temperature - NORMAL_TEMP
#            print(f'You have {degrees_of_fever:f} degrees of fever.') 
#       elif (temperature < CUTOFF_TEMP):
#            degrees_of_fever = CUTOFF_TEMP - temperature
#            print(f'Your temperature is {degrees_of_fever:f} below 95.') 


# body_temperature = 96.0
# print('Checking for fever...')
# print_fever_check(body_temperature)

# my_poem = 'Roses are red; Violets are blue'
# new_separator = '.'
# new_poem = my_poem.split(';')
# print(new_separator.join(new_poem))

# my_string = 'What is your name?'
# print(my_string.split('?'))

# objects = {}
# objects['a'] = 'Chair'
# objects['b'] = 'Table'
# objects['c'] = 'Sofa'
# objects.clear()
# print(objects)

# new_list = [['hello', 'word'], 'good morning', 'have a nice day']
# print(new_list[0:2])

# class Company():
#         def __init__(self,employees):
#                self._employees = employees
#         def __len__(self):
#             return len(self._employees)

# members = Company(['manager','team lead','mentor'])
# print(len(members))

# class Factorial:
#        def __init__(self, num1 = 5):
#              self.num1= num1
#        def calculate_fact(self):
#              fact = 1 
#              for i in range(1, self.num1 + 1):
#                     fact *= i 
#              print(fact)

# fact1 = Factorial(2)
# fact1.calculate_fact()

# def odd_even(a):
#       if isinstance(a, int):
#            if a % 2 == 0:
#                   return 'even'
#            else:
#                   return 'odd'
#       else:
#            raise TypeError('Invalid Variable Type!') 

# try:
#      n = '3'
#      print(odd_even(n))
# except TypeError as expt:
#      print(expt)
# except:
#      print('Error!')
# finally:
#      print('Value entered:', n)


# def calculate_pay(hourly_rate, hours_worked):
#     regular_hours = min(8, hours_worked)
#     overtime_hours = max(0, min(4, hours_worked - 8))
#     double_overtime_hours = max(0, hours_worked - 12)

#     regular_pay = regular_hours * hourly_rate
#     overtime_pay = overtime_hours * 1.5 * hourly_rate
#     double_overtime_pay = double_overtime_hours * 2.0 * hourly_rate

#     total_pay = regular_pay + overtime_pay + double_overtime_pay

#     return total_pay

# # Example usage:
# hourly_rate = 10.0
# hours_worked = 14
# total_pay = calculate_pay(hourly_rate, hours_worked)
# print(f'Total pay: ${total_pay:.2f}')

def encode_string(input_string):
    # Slicing the original string into two parts
    first_part = input_string[:3]
    second_part = input_string[3:]

    # Changing the first variable to "Title Case"
    first_part = first_part.title()

    # Adding 200 to the integer value of the second variable
    second_part = str(min(int(second_part) + 200, 1000))

    # Joining the two variables
    encoded_string = first_part + second_part

    return encoded_string

# Taking input from the user
user_input = input("Please input your abc123: ")

# Encoding the string and displaying the result
encoded_result = encode_string(user_input)
print(f'Your Encoded String is: {encoded_result}')

