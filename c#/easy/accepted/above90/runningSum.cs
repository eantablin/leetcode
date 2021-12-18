// Runtime: 265 ms, faster than 5.18% of C# online submissions for Running Sum of 1d Array.
// Memory Usage: 39.3 MB, less than 96.71% of C# online submissions for Running Sum of 1d Array.

// If nums.Length isn't placed into an int it's considerably slower 

public int[] RunningSum(int[] nums) {
    int pHolder = 0;

    for(int i = 0; i < nums.Length; ++i)
    {
        pHolder += nums[i];

        nums[i] = pHolder;
    }

    return nums;
}

// Runtime: 120 ms, faster than 80.24% of C# online submissions for Running Sum of 1d Array.
// Memory Usage: 41.2 MB, less than 49.18% of C# online submissions for Running Sum of 1d Array.

class Program
{
    static void Main()
    {
        int[] nums = [1,2,3,4];

        Problem.RunningSum(nums);
    }
}

public class Problem
{
    public int[] RunningSum(int[] nums) {
            int numsLen = nums.Length;
            int pHolder = 0;

            for(int i = 0; i < numsLen; ++i)
            {
                pHolder += nums[i];

                nums[i] = pHolder;
            }

            return nums;
        }
}
