/**
 * @Author: Araika Singh <NonZeroExitCode>
 * @Date:   2021-03-19T19:27:34+05:30
 * @Email:  roseymods@gmail.com
 * @Last modified by:   NonZeroExitCode
 * @Last modified time: 2021-03-19T20:20:49+05:30
 * @Link to question: https://leetcode.com/problems/two-sum/
 */

import java.io.*;
import java.util.*;

public class TwoSumJava{

  //Main logic here
  public int[] twoSum(int[] nums, int target) {
    //Creating a HashMap to keep track of numbers and their indices
    HashMap<Integer, Integer> map = new HashMap<>();

    //Traversing through the array
    /*Say for testcase array = {0, 1, -1, 2} if required sum is 0.
    *Then the present element should have a number (target - present element)
    *Like for n = 2, the list should have (0 - 2) = -2 to have a sum = 0
    */

    for(int i = 0; i < nums.length; i++){
      /*if the map contains (target - present element) then we got our pair and
      *hence the required indices is to be returned
      */
      if(map.containsKey(target-nums[i])){
        return new int[]{map.get(target-nums[i]), i};
      }else{
        /*According to the testcase {0, 1, -1, 2} we don't have (target - present element)
        *for first two elements yet and hence we just add 0 and 1 to the HashMap
        */
        map.put(nums[i], i);
        }
      }

      //In case, there is no pair then empty array is returned
      return new int[]{};
  }

  //Driver Codes. Not relevant for leetcode
  public static void main(String[] args) throws java.lang.Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    print("Enter the number of elements in array: ");
    StringTokenizer st = st(br);
    int n = ip(st.nextToken().trim());

    int[] arr = new int[n];
    println("\nEnter the array elements: ");
    st = st(br);
    for(int i = 0; i < arr.length; i++){
      arr[i] = ip(st.nextToken().trim());
    }

    println("Enter the target sum: ");
    st = st(br);
    int target = ip(st.nextToken().trim());

    TwoSumJava obj = new TwoSumJava();
    int[] res = obj.twoSum(arr, target);
    println("The indices for two sum are " + res[0] + ", " + res[1]);
  }

  public static void println(String s){
    System.out.println(s);
  }

  public static void print(String s){
    System.out.print(s);
  }

  public static int ip(String s){
    return Integer.parseInt(s);
  }

  public static long lp(String s){
    return Long.parseLong(s);
  }

  public static float fp(String s){
    return Float.parseFloat(s);
  }

  public static double dp(String s){
    return Double.parseDouble(s);
  }

   public static double log(long x, int base)
   {
     return (Math.log10(x) / Math.log10(base) + 1e-10);
   }

  public static StringTokenizer st(BufferedReader br) throws java.lang.Exception{
    return new StringTokenizer(br.readLine());
  }
}
