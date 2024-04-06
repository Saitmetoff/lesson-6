"""1"""

# def average_of_missing_numbers(list1, list2):
#     numbers1 = set(list1)
#     numbers2 = set(list2)
#     missing_numbers = [num for num in numbers1.symmetric_difference(numbers2) if isinstance(num, int)]
#     if missing_numbers:
#         return sum(missing_numbers) / len(missing_numbers)
#     else:
#         return None
#
# list1 = [1, 1, 3, 4, 4, 5, 6, 7]
# list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
#
# result = average_of_missing_numbers(list1, list2)
# print(result)


"""2"""

# def add_prefix_to_list(lst, prefix):
#     return [prefix + str(item) for item in lst]
#
# lst = [1, 4, 3, 9]
# prefix = "RM"
#
# result = add_prefix_to_list(lst, prefix)
# print(result)


"""3"""

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_sum_list = max(lists, key=sum)
# print(max_sum_list)


"""4"""

# def count_integers(lst):
#     return sum(isinstance(x, int) for x in lst)
#
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
#
# result = count_integers(lst)
# print(result)


"""5"""

# def most_common_element(lst):
#     counts = {}
#     for item in lst:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
#     max_count = max(counts.values())
#     most_common = [key for key, value in counts.items() if value == max_count][0]
#     return most_common, max_count
#
# lst = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
#
# element, count = most_common_element(lst)
# print(f"{element} -> {count} marta")


"""6"""

# def increment_last_digit(lst):
#     num = int(''.join(map(str, lst)))
#     num += 1
#     return [int(x) for x in str(num)]
#
# input1 = [1, 2, 3]
# input2 = [9]
# input3 = [9, 9, 9, 9]
#
# print(increment_last_digit(input1))
# print(increment_last_digit(input2))
# print(increment_last_digit(input3))


"""7"""
# def square_of_elements():
#     n = int(input("Enter the number of elements: "))
#     lst = [int(input()) for _ in range(n)]
#     return [x**2 for x in lst]
#
# result = square_of_elements()
# print(result)


"""8"""

# def add_number_to_elements(lst_numbers, lst_strings):
#     return [str(lst_strings[i]) + str(lst_numbers[i]) for i in range(min(len(lst_numbers), len(lst_strings)))]
#
# numbers = [1, 4, 3, 9]
# strings = ['chelsea', 'real', 'barca', 'MU']
#
# result = add_number_to_elements(numbers, strings)
# print(result)


"""9"""

# def max_of_common_elements(lst1, lst2):
#     common_elements = set(lst1) & set(lst2)
#     if common_elements:
#         return max(common_elements)
#     else:
#         return None
#
# list1 = [1, 4, 3, 9]
# list2 = [5, 4, 9, 7]
#
# result = max_of_common_elements(list1, list2)
# print(result)


"""10"""

# def fibonacci(n):
#     fib_list = [1, 2]
#     while fib_list[-1] <= n:
#         fib_list.append(fib_list[-1] + fib_list[-2])
#     return fib_list[:-1]
#
# n = int(input("Enter a number: "))
# fib_numbers = fibonacci(n)
# print(fib_numbers)