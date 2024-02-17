package org.example.ArraryProblems;

public class RemoveElementFinsh {
    /*
     * 输入：nums = [3,2,2,3], val = 3
     *  输出：2, nums = [2,2]
     * */
    public static int removeElement(int[] nums, int val) {
        // 遍历整个数组，所有为3的移除
        // 这里可以对数组的元素进行添加
        // 这里我们返回的是数组的长度
        int index = 0;
        for (int num : nums) {
            if (num != val) {
                nums[index] = num;
                index +=1;
            }
        }
        return index;
    }

}
