// Runtime: 202 ms, faster than 11.33% of C# online submissions for Concatenation of Array.
// Memory Usage: 43.8 MB, less than 13.71% of C# online submissions for Concatenation of Array.

public int[] GetConcatenation(int[] nums) {
    int numLen = nums.Length;
    int[] ans = new int[numLen*2];
    nums.CopyTo(ans, 0);
    nums.CopyTo(ans, numLen);
    
    
    return ans;
}