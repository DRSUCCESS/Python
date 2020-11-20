# # ...COMPREHENSION using list
# # double prize money weekend bonanza
# prizes = [5, 10, 50, 100, 1000]


# dbl_prizes = [ ]
# for prize in prizes:
#     dbl_prizes.append(prize*2)
# # print(dbl_prizes)


# # comprehension metthod
# dbl_prizes = [ prize*2 for prize in prizes ]
# # print(dbl_prizes)


# # squaring numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
# square_even_nums = [ ]

# for num in nums:
#     if(num **2) % 2 == 0:
#         square_even_nums.append(num ** 2)
#         # print(square_even_nums)

# # comprehension metthod
# square_even_nums = [num ** 2 for num in nums if (num ** 2 )% 2 ==0 ]
# # print(square_even_nums)



# # ...MAP FUNCTION

# from random import shuffle

# def jumble(word):
#     anagram = list(word)
#     shuffle(anagram)
#     return ''.join(anagram)

# words = ['bestroot', 'carrot', 'potatoes']
# anagrams = [ ]

# # print(list(map(jumble, words))) # using map function

# # print([jumble(word) for word in words])  # comprehension

# # for word in words: # for loop
# #     anagrams.append(jumble(word))
# # print(anagrams)



# # ...FILTER
# grades = ['A', 'B', 'C', 'F', 'A', 'C']

# def remove_fails(grade):
#     return grade != 'F'
# # print(list(filter(filtered_grades, grades))) #map


# # filtered_grades = [] # function
# # for grade in grades:
# #     if grade != 'F':
# #         filtered_grades.append(grade)
# # print(filtered_grades)

# # print([grade for grade in grades if grade != 'F' ]) # comprehension


# ...LAMBDA FUNCTION
nums = [1,2,3,4,5,6]

def square(n):
    return n*n


# print(list(map(square, nums)))  # map
print(list(map(lambda n:n*n, nums)))  # lamda
