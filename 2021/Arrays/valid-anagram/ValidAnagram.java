/**
 * @Author: Araika Singh <NonZeroExitCode>
 * @Date:   2021-03-20T00:25:44+05:30
 * @Email:  roseymods@gmail.com
 * @Last modified by:   NonZeroExitCode
 * @Last modified time: 2021-03-20T01:28:43+05:30
 * @Link to question: https://leetcode.com/problems/valid-anagram/
 */

 class ValidAnagram {

   // If two strings have same letters in same number exactly in same
   // or different order then the two strings are anagrams
   public boolean isAnagram(String s, String t) {
     int sLen = s.length(), tLen = t.length();

     // If the length of both strings are different then they
     // can't be anagrams
     if(sLen != tLen) {
       return false;
     }

     // Keeping a hashmap to keep track of letters
     // The intuition used here would be say there are two words
     // aka "araika" and "raakia", now when we count the letters in
     // string and subtract them, we should get an overrall answer as
     // zero, i.e, string "araika"--> 3 a's, 1 r, 1 i and 1 k
     // minus string "raakia"--> 3 a's, 1 r, 1 i and 1 k is equal to
     // 0 a, 0 r, 0 i and 0 k

     HashMap<Character, Integer> map = new HashMap<>();

     // Since the length of both strings, it doesn't matter what string size
     // is to be taken
     for(int i = 0; i < sLen; i++){
       char ch = s.charAt(i), ch2 = t.charAt(i);

       // If the map doesn't contain the letter in string s then add
       // it to list and update the corresponding value as 1
       if(!map.containsKey(ch)){
         map.put(ch, 1);
       }else{
         // If the letter in string s is already present then the value is
         // incremented by 1
         map.put(ch, map.get(ch)+1);
       }

       // If the map doesn't contain the letter in string t then add
       // it to list and update the corresponding value as -1
       if(!map.containsKey(ch2)){
         map.put(ch2, -1);
       }else{
         // If the letter in string s is already present then the value is
         // decremented by 1
         map.put(ch2, map.get(ch2)-1);
       }
     }

     // Checking if the values of any letter is not zero, that means there is an
     // extra letter/character in either of the given strings
     for(int val : map.values()){

       // If the value is not zero then return false
       if(val != 0){
         return false;
       }
     }

     // No value was found in map that wasn't zero that means the strings s and t
     // are anagrams
     return true;
   }
}
