from unittest import TestCase
from easy.two_sum import two_sum


class TestTwoSum(TestCase):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        nums2 = [3, 2, 4]
        target2 = 6
        nums3 = [3, 3]
        self.assertEqual([1, 0], two_sum(nums, target))
        self.assertEqual([2, 1], two_sum(nums2, target2))
        self.assertEqual([1, 0], two_sum(nums3, target2))


