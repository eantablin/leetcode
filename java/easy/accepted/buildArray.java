// Runtime: 1 ms, faster than 99.84% of Java online submissions for Build Array from Permutation.
// Memory Usage: 39.7 MB, less than 61.37% of Java online submissions for Build Array from Permutation.

class Solution {
    public int[] buildArray(int[] nums) {
        int[] pHolder = new int[nums.length];
        
        for(int i = 0; i < nums.length; ++i)
        {
            pHolder[i] = nums[nums[i]];
        }
        
        return pHolder;
    }
}