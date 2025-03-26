class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #O(nlogn)
        for i,n in enumerate(nums2):
            nums1[m + i] = n

        nums1.sort()
