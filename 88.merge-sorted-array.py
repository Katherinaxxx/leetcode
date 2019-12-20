class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0, 0
        new = []
        while i <m :
            while j <n and nums1[i]>=nums2[j]:
                new.append(nums2[j])
                j = j+1
            new.append(nums1[i])
            i = i+1
        if i==m:
            while j<n:
                new.append(nums2[j])
                j = j + 1
        nums1[:] = new