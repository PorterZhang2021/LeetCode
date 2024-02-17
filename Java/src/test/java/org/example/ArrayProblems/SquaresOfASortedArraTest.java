package org.example.ArrayProblems;

import org.example.ArraryProblems.SquaresOfASortedArra;
import org.junit.Test;

public class SquaresOfASortedArraTest {
    @Test
    public void test1(){
        /**
         * 输入：nums = [-4,-1,0,3,10]
         * 输出：[0,1,9,16,100]
         */
        int[] nums = {-4, -1, 0, 3, 10};
        int[] squares = SquaresOfASortedArra.sortedSquares(nums);
        for (int square : squares) {
            System.out.println(square);
        }
    }

    @Test
    public void test2(){
        /**
         * 输入：nums = [-7,-3,2,3,11]
         * 输出：[4,9,9,49,121]
         */
        int[] nums = {-7, -3, 2, 3, 11};
        int[] squares = SquaresOfASortedArra.sortedSquares(nums);
        for (int square : squares) {
            System.out.println(square);
        }
    }
}
