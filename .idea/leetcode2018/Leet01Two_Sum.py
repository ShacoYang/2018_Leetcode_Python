'''
enumerate
loop over sth and have an automatic counter

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

for counter, value in enumerate(some_list):
    print(counter, value)
'''

class Solution:
    def twoSum(self, nums, target):
        '''
        :param nums: list[int]
        :param target: int
        :return: list[int]
        '''
        result = {}
        for i in num in enumerate(nums):
            if target - num in result:
                return [result[target - num], i]
            result[num] = 1
