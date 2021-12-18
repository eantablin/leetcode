// Runtime: 72 ms, faster than 99.01% of C# online submissions for Richest Customer Wealth.
// Memory Usage: 38.5 MB, less than 24.34% of C# online submissions for Richest Customer Wealth.

public int MaximumWealth(int[][] accounts) {
    int accountsLen = accounts.Length;
    int maxWealth = 0;
    
    for(int i = 0; i < accountsLen; ++i)
    {   
        int curValWealth = 0;
        int currLen = accounts[i].Length;
        
        for(int j = 0; j < currLen; ++j)
        {
            curValWealth += accounts[i][j];
            
            if (curValWealth >= maxWealth) { maxWealth = curValWealth; }
        }
    }
    
    return maxWealth;
}