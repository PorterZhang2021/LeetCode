package org.example.ArraryProblems;

public class BinarySearchFinsh {
    public static int search(int[] nums, int target) {
        // 利用二分查找法完成此任务
        // 左边界
        int left = 0;
        // 右边界
        int right = nums.length - 1;
        // 如果左边界<=右边界 可以继续
        while (left <= right) {
            // 找到中间
            int mid = (left + right) / 2;
            // 如果此时中间<target 那么更新左边界
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                // 否则更新右边界
                right = mid - 1;
            } else {
                // 返回下标
                return mid;
            }

        }
        // 没有找到返回-1
        return -1;
    }

    public static void main(String[] args) {
        /*
        * 示例 1:
            输入: nums = [-1,0,3,5,9,12], target = 9
            输出: 4
            解释: 9 出现在 nums 中并且下标为 4
            示例 2:

            输入: nums = [-1,0,3,5,9,12], target = 2
            输出: -1
            解释: 2 不存在 nums 中因此返回 -1
        * */
        int[] nums1 = {-1, 0, 3, 5, 9, 12};
        int target1 = 9;
        // 返回结果为下标4
        System.out.println(BinarySearchFinsh.search(nums1, target1));

        int[] nums2 = {-1, 0, 3, 5, 9, 12};
        int target2 = 2;
        // 返回结果为-1
        System.out.println(BinarySearchFinsh.search(nums2, target2));
    }
}
