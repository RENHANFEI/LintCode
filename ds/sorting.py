import random
from collections import deque

class Sorting(object):

    def __init__(self, nums=None):
        if nums:
            self.nums = nums
        else:
            self.nums = random.sample(range(-50, 50), 30)
        
    def bubble_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def selection_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        n = len(nums)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums 

    def insertion_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        n = len(nums)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    continue
        return nums

    def shell_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        gap = 0
        while gap <= len(nums):
            gap = gap * 3 + 1  # get initial gap (use dynamic gap)
        while gap > 0:
            for i in range(gap, len(nums)):
                num = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > num:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = num
            gap //= 3
        return nums

    def merge_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        return self.__merge(self.merge_sort(left), self.merge_sort(right))

    def __merge(self, left, right):
        result = []
        i, j = 0, 0
        n_left, n_right = len(left), len(right)
        while i < n_left and j < n_right:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < n_left:
            result.append(left[i])
            i += 1
        while j < n_right:
            result.append(right[j])
            j += 1
        return result

    def quick_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        self.__q_sort(nums, 0, len(nums) - 1)
        return nums

    def __q_sort(self, nums, left, right, cutoff=5):
        if left + cutoff < right:
            pivot = self.__median3(nums, left, right)
            i, j = left + 1, right - 2
            while 1:
                while nums[i] < pivot: i += 1
                while nums[j] > pivot: j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    break
            nums[i], nums[right - 1] = nums[right - 1], nums[i]
            self.__q_sort(nums, left, i - 1)
            self.__q_sort(nums, i + 1, right)
        else:
            nums[left:right + 1] = self.insertion_sort(nums[left:right + 1])

    def __median3(self, nums, left, right):
        mid = (left + right) // 2
        if nums[left] > nums[mid]: nums[left], nums[mid] = nums[mid], nums[left]
        if nums[left] > nums[right]: nums[left], nums[right] = nums[right], nums[left]
        if nums[mid] > nums[right]: nums[mid], nums[right] = nums[right], nums[mid]
        nums[mid], nums[right - 1] = nums[right - 1], nums[mid]  # hide pivot
        return nums[right - 1]

    def heap_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        # to save space, use max heap
        n = len(nums)
        for i in range(n // 2, -1, -1): self.__perc_down(nums, i, n)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.__perc_down(nums, 0, i)
        return nums

    def __perc_down(self, nums, i, n):
        temp = nums[i]
        child = self.__left_child(i)
        while child < n:
            if child != n - 1 and nums[child + 1] > nums[child]:
                child += 1
            if temp < nums[child]:
                nums[i] = nums[child]
            else:
                break
            i = child
            child = self.__left_child(i)
        nums[i] = temp

    def __left_child(self, i):
        return 2 * i + 1

    def counting_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        buckets = [0] * (max(nums) - min(nums) + 1)
        shift = -min(nums)
        for num in nums:
            buckets[num + shift] += 1
        result = []
        for i, bucket in enumerate(buckets):
            for _ in range(bucket):
                result.append(i - shift)
        return result

    def bucket_sort(self, nums=None, bucket_size=5):
        if not nums:
            nums = [num for num in self.nums]
        min_num, max_num = nums[0], nums[0]
        for num in nums[1:]:
            min_num = min(min_num, num)
            max_num = max(max_num, num)
        # get bucket num from difference between max and min
        bucket_num = (max_num - min_num) // bucket_size + 1
        buckets = [[] for _ in range(bucket_num)]
        # push nums into buckets
        for num in nums:
            buckets[(num - min_num) // bucket_size].append(num)
        # add up nums
        result = []
        for bucket in buckets:
            if bucket:
                result += self.insertion_sort(bucket)
        return result

    def radix_sort_nonnegative(self, nums=None):
        if not nums:
            nums = map(abs, self.nums)
        max_num = nums[0]
        for num in nums:
            max_num = max(max_num, num)
        max_digit = len(str(max_num))
        counters = [deque() for _ in range(10)]
        mod, dev = 10, 1
        for i in range(max_digit):
            for num in nums:
                counters[num % mod // dev].append(num)
            nums = []
            for counter in counters:
                while counter:
                    nums.append(counter.popleft())
            mod *= 10
            dev *= 10
        return nums

    def radix_sort(self, nums=None):
        if not nums:
            nums = [num for num in self.nums]
        negative = []
        nonnegative = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                nonnegative.append(num)
        return map(lambda x: -x, self.radix_sort_nonnegative(map(
            lambda x: -x, negative))[::-1]) + self.radix_sort_nonnegative(nonnegative)
    

sort = Sorting()
print("Original Array: {}".format(sort.nums))
print("Bubble Sort:    {}".format(sort.bubble_sort()))
print("Selection Sort: {}".format(sort.selection_sort()))
print("Insertion Sort: {}".format(sort.insertion_sort()))
print("Shell Sort:     {}".format(sort.shell_sort()))
print("Merge Sort:     {}".format(sort.merge_sort()))
print("Quick Sort:     {}".format(sort.quick_sort()))
print("Heap Sort:      {}".format(sort.heap_sort()))
print("Counting Sort:  {}".format(sort.counting_sort()))
print("Bucket Sort:    {}".format(sort.bucket_sort()))
print("Radix Sort:     {}".format(sort.radix_sort()))