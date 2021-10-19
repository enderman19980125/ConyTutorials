from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc = dict()
        for i, n in enumerate(nums):
            if target - n in loc.keys():
                return [loc[target - n], i]
            else:
                loc[n] = i
        return []


if __name__ == '__main__':
    solution = Solution()
    answer = solution.twoSum([2, 11, 15, 7], 9)
    print(answer)
