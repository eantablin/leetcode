// Runtime: 318 ms, faster than 5.42% of C# online submissions for Build Array from Permutation.
// Memory Usage: 43.9 MB, less than 77.57% of C# online submissions for Build Array from Permutation.

public int[] BuildArray(int[] nums) {
    int[] ans = new int[nums.Length];
    
    for(int i = 0; i < nums.Length; ++i)
    {
        ans[i] = nums[nums[i]];
    }
    
    return ans;
}