package ArrayProblems;

/**
 * 给定一个含有 n 个正整数的数组和一个正整数 target 。
 *
 * 找出该数组中满足其总和大于等于 target 的长度最小的连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
 * 并返回其长度。如果不存在符合条件的子数组，返回 0 。
 *
 * 此问题有一个起始位置, 有一个最小长度
 * 我们从起始位置开始对目标元素进行操作
 *  1. 判断目标元素是否==0
 *      1. 判断最小长度是否比现在的最小长度小, 进行更新操作
 *  2. 减去当前索引位置的值
 *  3. 索引值+1
 */
public class MSSubarraySum {
    public static int minSubArrayLen(int target, int[] nums){
        int minLength = Integer.MAX_VALUE;
        int curTarget;
        int curIndex;
        boolean isZero;
        for (int startIndex = 0; startIndex < nums.length; startIndex++) {
            // 用于进行目标的判断
            curTarget = target;
            curIndex = startIndex;
            isZero = false;
            // 遍历操作
            while(curTarget >= 0 && curIndex < nums.length){
                if(curTarget == 0){
                    isZero = true;
                    break;
                }
                curTarget -= nums[curIndex];
                curIndex += 1;
            }
            if(isZero){
                int tmpLength = curIndex - startIndex + 1;
                if (tmpLength < minLength) {
                    minLength = tmpLength;
                }
            }
        }
        if (minLength == Integer.MAX_VALUE){
            return 0;
        }
        return minLength;
    }
}
