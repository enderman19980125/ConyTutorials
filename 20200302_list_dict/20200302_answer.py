# 今天也是想念小兔的一天呢！


# ---------------------------------------------------------
# 这是检验答案是否正确的函数，兔兔不用在意它
# ---------------------------------------------------------
def compare_answer(cony_answer: object, std_answer: object):
    global C
    C += 1
    print(f"[Problem {C}]")
    print("Cony: " + str(cony_answer))
    print("Std:  " + str(std_answer))
    correct = cony_answer == std_answer and cony_answer is not std_answer
    print("\033[32mCorrect\033[0m" if correct else "\033[31mWrong\033[0m")
    print()


C = 0

# ---------------------------------------------------------
# 一、列表推导式
# ---------------------------------------------------------

# [Problem 1] 产生一个包含 9 到 27 中所有 3 的倍数的列表
cony = [i for i in range(9, 28) if i % 3 == 0]
std = [9, 12, 15, 18, 21, 24, 27]
compare_answer(cony, std)

# [Problem 2] 产生一个格点列表，横坐标都是 x = 1，纵坐标 y 从 1 到 10，列表中每个元素都是一个元组 (x, y)
cony = [(1, y) for y in range(1, 11)]
std = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]
compare_answer(cony, std)

# [Problem 3] 产生一个列表，其每个元素都是一个列表，且第 k 个列表是十位为 k 的那十个整数，即将 100 以内的整数按十位分成 10 组
cony = [[10 * a + b for b in range(10)] for a in range(10)]
std = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
]
compare_answer(cony, std)

# ---------------------------------------------------------
# 二、遍历列表
# ---------------------------------------------------------

brown = ["Brown", 175, 77.7, "hamburger", "Cony"]

# [Problem 4] 使用 in 遍历 brown 列表，并依次将每个元素添加到 brown_copy 列表中，最终效果 brown == brown_copy
brown_copy = []
for element in brown:
    brown_copy.append(element)
compare_answer(brown_copy, brown)

# [Problem 5] 使用 enumerate 遍历 brown 列表，并依次将每个元素的索引和值作为一个列表 [index, element] 添加到 brown_copy 列表中
brown_copy = []
for index, element in enumerate(brown):
    brown_copy.append([index, element])
compare_answer(brown_copy, [[0, "Brown"], [1, 175], [2, 77.7], [3, "hamburger"], [4, "Cony"]])

# ---------------------------------------------------------
# 三、遍历字典
# ---------------------------------------------------------

brown = {"Name": "Brown", "Height": 175, "Weight": 77.7, "Eat": "hamburger", "Love": "Cony"}

# [Problem 6] 使用 keys() 遍历 brown 字典，并依次将每个元素添加到 brown_copy 字典中，最终效果 brown == brown_copy
brown_copy = {}
for key in brown.keys():
    brown_copy[key] = brown[key]
compare_answer(brown_copy, brown)

# [Problem 7] 使用 items() 遍历 brown 字典，并依次将每个元素添加到 brown_copy 字典中，最终效果 brown == brown_copy
brown_copy = {}
for key, value in brown.items():
    brown_copy[key] = value
compare_answer(brown_copy, brown)
