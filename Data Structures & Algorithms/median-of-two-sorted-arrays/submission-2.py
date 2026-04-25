class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx1 = 0
        idx2 = 0

        result = []

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                result.append(nums1[idx1])
                idx1 +=1

            else:
                result.append(nums2[idx2])
                idx2 += 1
        

        while idx1 < len(nums1):
            result.append(nums1[idx1])
            idx1 += 1

        while idx2 < len(nums2):
            result.append(nums2[idx2])
            idx2 += 1

        return result


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            merge and midpoint
        """

        total_len = len(nums1) + len(nums2)
        merged_list = self.merge(nums1,nums2)

        if (total_len % 2) == 1:
            return merged_list[total_len // 2]

        else:
            left = merged_list[total_len // 2 - 1]
            right = merged_list[(total_len // 2)]
            return (left + right) / 2


