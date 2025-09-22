import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # #Quick sort solution
        # def quicksort(l, r):
        #     #Base case: 0 or 1 item in interval
        #     if l >= r:
        #         return

        #     #Choose pivot (middle element)
        #     pivot = nums[(l + r)//2]
        #     i, j = l, r     #two pointers from both ends

        #     #partition loop
        #     while i <= j:
        #         #move i right until we find an element >= pivot
        #         while nums[i] < pivot:
        #             i += 1
        #         #move j left until we find an element <= pivot
        #         while nums[j] > pivot:
        #             j -= 1

        #         #if pointers haven't crossed, swap the out-of-place elements
        #         if i <= j:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j -= 1

        #     #now: j < i, and the array is partitioned into [l:j] and [i:r]
        #     quicksort(l, j)     #sort left partition
        #     quicksort(i, r)     #sort right partition

        # quicksort(0, len(nums) - 1)
        # return nums





        # # Merge Sort
        # def merge_sort(arr):
        #     if len(arr) <= 1:
        #         return arr      #base case: only one element - already solved

        #     mid = len(arr)//2
        #     l = merge_sort(arr[:mid])       #sort left half
        #     r = merge_sort(arr[mid:])       #sort right half

        #     return merge(l, r)

        # def merge(l, r):
        #     merged = []
        #     i, j = 0, 0

        #     #merge 2 sorted lists (loop through index and add lower val to merged return array)
        #     while i < len(l) and j < len(r):
        #         if l[i] < r[j]:
        #             merged.append(l[i])
        #             i += 1
        #         else:
        #             merged.append(r[j])
        #             j += 1

        #     #append any leftovers
        #     merged.extend(l[i:])
        #     merged.extend(r[j:])

        #     return merged

        # return merge_sort(nums)



        # # Heap Sort
        # n = len(nums)

        # def heapify(n, i):
        #     largest = i
        #     left = 2 * i + 1
        #     right = 2 * i + 2

        #     if left < n and nums[left] > nums[largest]:
        #         largest = left

        #     if right < n and nums[right] > nums[largest]:
        #         largest = right

        #     if largest != i:
        #         nums[i], nums[largest] = nums[largest], nums[i]
        #         heapify(n, largest)

        # for i in range(n//2 - 1, -1, -1):
        #     heapify(n, i)

        # for i in range(n - 1, 0, -1):
        #     nums[0], nums[i] = nums[i], nums[0]
        #     heapify(i,0)

        # return nums




        # Heap Sort (Built- in)
        heapq.heapify(nums)
        res = []

        while nums:
            res.append(heapq.heappop(nums))

        return res