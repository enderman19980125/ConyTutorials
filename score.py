import numpy as np

a = np.array([1, 2, 3])


class MyList:
    def __init__(self, in_list):
        self.list = in_list

    def __getitem__(self, item):
        yield self.list[item]

    def __len__(self):
        return len(self.list)

    def getAllow(self):
        return 1


lst = MyList([1, 2, 3])

for i in lst:
    print(i)
