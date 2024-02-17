package org.example.ArrayProblems;


import org.example.ArraryProblems.RemoveElementFinsh;
import org.junit.Test;

public class RemoveElementFinshTest {
    @Test
    public void testRemoveElement1(){
        /*
        * 输入：nums = [3,2,2,3], val = 3
        *  输出：2, nums = [2,2]
        * */
        int[] nums = {3,2,2,3};
        int val = 3;
        int index = RemoveElementFinsh.removeElement(nums, val);
        for (int i = 0; i < index; i++) {
            System.out.println(nums[i]);
        }
    }

    @Test
    public void testRemoveElement2(){
        /*
        * nums = [0,1,2,2,3,0,4,2], val = 2
        *  5, nums = [0,1,3,0,4]
        * */
        int[] nums = {0,1,2,2,3,0,4,2};
        int val = 2;
        int index = RemoveElementFinsh.removeElement(nums, val);
        for (int i = 0; i < index; i++) {
            System.out.println(nums[i]);
        }
    }
}
