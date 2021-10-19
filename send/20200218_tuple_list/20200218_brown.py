# 兔兔知道怎么运行吗？
# 按 Alt + Shift + F9，然后选择文件名对应的配置就能运行了。
# 第一次运行成功后，以后按 Shift + F9 就能直接运行了。


# 所有带有 None 的地方是需要兔兔填的哦！！！


# ---------------------------------------------------------
# 这是检验答案是否正确的函数，兔兔不用在意它
# ---------------------------------------------------------
def compare_answer(cony_answer: object, std_answer: object):
    global C
    C += 1
    print(f"[Problem {C}]")
    print("Cony: " + str(cony_answer))
    print("Std:  " + str(std_answer))
    print("\033[32mCorrect\033[0m" if cony_answer == std_answer else "\033[31mWrong\033[0m")
    print()


C = 0

# ---------------------------------------------------------
# 一、列表的切片
# ---------------------------------------------------------

# 给定一个列表 a，仅用列表的切片完成以下操作
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# [Problem 1] 例：选取第零个元素
ans = a[0]
compare_answer(ans, 0)

# [Problem 2] 选取最后一个元素
ans = a[-1]
compare_answer(ans, 19)

# [Problem 3] 选取前两个元素
# TODO: 从列表开头选取可省略 0
# TODO: ans = a[:2]
ans = a[0:2]
compare_answer(ans, [0, 1])

# [Problem 4] 选取后两个元素
# TODO: 注意区分下面几种情况
# TODO: a[-1:-2]=[]   a[-2:-1]=[18]   a[-2:]=[18,19]
ans = a[-1:-2]
compare_answer(ans, [18, 19])

# [Problem 5] 选取从值为 2 到值为 4 的共三个元素
ans = a[2:5]
compare_answer(ans, [2, 3, 4])

# [Problem 6] 选取从值为 15 到值为 17 的共三个元素
ans = a[15:18]
compare_answer(ans, [15, 16, 17])

# [Problem 7] 选取所有值为奇数的元素
ans = a[1::2]
compare_answer(ans, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# [Problem 8] 选取所有值为 3 的倍数的元素，且不选择 0
ans = a[3::3]
compare_answer(ans, [3, 6, 9, 12, 15, 18])

# [Problem 9] 选取值为 2, 3, 4, 15, 16, 17 的共六个元素
ans = a[2:5] + a[15:18]
compare_answer(ans, [2, 3, 4, 15, 16, 17])

# [Problem 10] 倒序选取所有值为 6 的倍数的元素，且不选择 0
ans = a[-2::-6]
compare_answer(ans, [18, 12, 6])

# [Problem 11] 选取所有值为 7 的倍数的元素，并重复 3 遍
ans = a[0::7] * 3
compare_answer(ans, [0, 7, 14, 0, 7, 14, 0, 7, 14])

# [Problem 12] 选取值最小的元素，使用 min 函数
ans = min(a)
compare_answer(ans, 0)

# [Problem 13] 选取值最大的元素，使用 max 函数
ans = max(a)
compare_answer(ans, 19)

# [Problem 14] 获取列表的长度，使用 len 函数
ans = len(a)
compare_answer(ans, 20)

# [Problem 15] 删除列表 a 中的前十一个元素，即保留从值为 11 开始的所有元素
# TODO: a=a[11:] 或 a[:11]=[]
a[0:12] = []
compare_answer(a, [11, 12, 13, 14, 15, 16, 17, 18, 19])

# [Problem 16] 在值为 14 和 15 的元素之间插入一个值 520
# TODO: a[4:4]=[520] 或 a.insert(4,520)
# TODO: a.insert = [] 不能这样调用，应该这样调用 a.insert(position,value)
a.insert = [4, 520]
compare_answer(a, [11, 12, 13, 14, 520, 15, 16, 17, 18, 19])

# [Problem 17] 在值为 17 和 18 的元素之间插入三个值 1，2，3
# TODO: a[-2:-2]=[1,2,3] 或 a.insert(-2,1) a.insert(-2,2) a.insert(-2,3)
a.insert = [8, 1]
a.insert = [9, 2]
a.insert = [10, 3]
compare_answer(a, [11, 12, 13, 14, 520, 15, 16, 17, 1, 2, 3, 18, 19])

# [Problem 18] 将值为 11 和 12 的两个元素替换为三个值 -1，-2，-3
# TODO: a[:2]=[-1,-2,-3]
a[11] = -1
a[12] = -2
a.insert = [2, -3]
compare_answer(a, [-1, -2, -3, 13, 14, 520, 15, 16, 17, 1, 2, 3, 18, 19])

# ---------------------------------------------------------
# 二、元组
# ---------------------------------------------------------

t1 = (0, 1, 2)
t2 = (3, 4, 5)

# 以下哪几行语句能正确执行，为什么？所以元组(tuple)和列表(list)的区别是什么？

# TODO: 只有 t1[:1] = (8, 9) 有错误，因为元组 (tuple) 是不可变对象
# t3 = t1 + t2
# t4 = t1 * 3
# t5 = t1[:2] + t1[-2:]
# t6 = t1[:2] * 3
# t1[:1] = (8, 9)
# t2 = t2[:2]
