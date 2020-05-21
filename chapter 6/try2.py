squares = [x * x for x in range(10)]

# values = [expression for item in collection]
# ============================================
# values = []
# for item in collection:
#     values.append(expression)

even_squares = [x * x for x in range(10) if x % 2 == 0]

# values = [expression for item in collection if condition]
# =========================================================
# values = []
# for item in collection:
#     if condition:
#         values.append(expression)

my_set = { x * x for x in range(-9, 10) }
my_dict = { x: x * x for x in range(5) }