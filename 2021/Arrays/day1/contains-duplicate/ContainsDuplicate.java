/**
 * @Author: Araika Singh <NonZeroExitCode>
 * @Date:   2021-03-19T22:02:05+05:30
 * @Email:  roseymods@gmail.com
 * @Last modified by:   NonZeroExitCode
 * @Last modified time: 2021-03-20T01:26:04+05:30
 * @Link to question: https://leetcode.com/problems/contains-duplicate/
 */

class ContainsDuplicate{

  public boolean containsDuplicate(int[] nums) {

    // Keep a set that keeps track of distict elements in nums array
    HashSet<Integer> set = new HashSet<>();

    // Traversing the nums array
    for(int i = 0; i < nums.length; i++){

      // In case the set already contains the number then return true
      if(set.contains(nums[i])) {
        return true;
      }else{
        // If the set doesn't contain the nums[i] then add it to set
        set.add(nums[i]);
      }
    }

    // In case no element was found again the set, hence no duplicate present
    return false;
  }
 }
