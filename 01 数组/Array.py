class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        nums_k_right = nums[-k:]
        nums_k_left = nums[:-k]
        nums_rotated = nums_k_right + nums_k_left
        nums = nums_rotated
        print(nums)

class Solution1:
    def rotate(self, nums, k: int) -> None:
        n = len(nums) # 获取列表nums的长度
        k = k % n     # 对k取n的模运算，确保k处于有效范围内。3 % 7 是余 3的。如果k是10，其实也相当于3，因为操作7次就会回到原位。
        self.reverse(nums, 0, n-1) # 调用类的内部方法reverse
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
    def reverse(self, nums, left: int, right: int) -> None:
        # left和right分别指向左边界的指针和右边界的指针
        while left < right :
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
S = Solution1()
S.rotate([1, 2, 3, 4, 5, 6, 7], 3)
