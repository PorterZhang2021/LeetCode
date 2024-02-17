package ArrayProblems;

import org.junit.Test;

public class MSSubarraySumTest {
    /**
     * 输入：target = 7, nums = [2,3,1,2,4,3]
     * 输出：2
     * 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
     */
    @Test
    public void test1(){
        int target = 7;
        int[] nums = {2, 3, 1, 2, 4, 3};
        System.out.println(MSSubarraySum.minSubArrayLen(target, nums));
    }
}
