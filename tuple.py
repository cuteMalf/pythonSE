# tuple1 = (1, 2, 3, 4, 'a', 'abc', [1, 2, 3], 3.4, 3)
# print(tuple1[1])
# print(tuple1[6][0])
#
# print(tuple1.index('abc'))
#
# print(tuple1.count(3))
#
# print(len(tuple1))

# nums = []
# for i in range(1, 9):
#     nums.append(i)
#
# lucky = []
# lucky.append(nums[0])
#
# for x in lucky:
#     print(x)
import random

class1 = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for teacher in teachers:
    index = random.randint(0, 2)
    class1[index].append(teacher)

print(class1)
