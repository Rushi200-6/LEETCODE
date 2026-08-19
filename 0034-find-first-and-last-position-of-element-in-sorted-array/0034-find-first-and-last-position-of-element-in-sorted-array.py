class Solution(object):

    def searchRange(self, nums, target):

        def lower_bound(nums, target):
            n = len(nums)
            lb = -1
            l, r = 0, n - 1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] >= target:
                    lb = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return lb

        def upper_bound(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            ub = n

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] > target:
                    ub = mid
                    r = mid - 1
                else:
                    l = mid + 1

            return ub

        lb = lower_bound(nums, target)
        ub = upper_bound(nums, target)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]

        # use of upper bound and lower bound with binary search