package org.example.ArraryProblems;


/**
 * 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
 *  输入：nums = [-4,-1,0,3,10]
 *  输出：[0,1,9,16,100]
 *
 */

public class SquaresOfASortedArra {
    public static int[] sortedSquares(int[] nums){
        int left = 0;
        int right = nums.length - 1;

        while(left <= right){
            // 两边指针进行比较
            // 将大的放置到最后，并对其进行交换操作
            if(nums[left] * nums[left] > nums[right] * nums[right]){
              swap(nums, left, right);
            }
            nums[right] = nums[right] * nums[right];
            right -= 1;
        }
        return nums;
    }

    public static void swap(int[] nums, int left, int right){
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
    }

    // 版本1
    /*public static int[] sortedSquares(int[] nums) {

        int left = 0;
        int right = nums.length - 1;
        int[] tmpNum = new int[nums.length];
        int index = nums.length - 1;
        while(left <= right) {
            // 通过双指针进行两边的比较
            // 如果大的就将其放置到末位
            if (nums[left] * nums[left] > nums[right] * nums[right]) {
                tmpNum[index] = nums[left] * nums[left];
                // 左边的大
                left += 1;
            } else {
                tmpNum[index] = nums[right] * nums[right];
                // 右边的大
                right -= 1;
            }
            index -= 1;
        }
        return tmpNum;
    }*/
}
