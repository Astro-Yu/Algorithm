class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        new_list = list(set(arr))
        count = []

        for i in range(len(new_list)):
            new_count = arr.count(new_list[i])
            count.append(new_count)

        if len(list(set(count))) == len(count):
            return True
        else:
            return False

        