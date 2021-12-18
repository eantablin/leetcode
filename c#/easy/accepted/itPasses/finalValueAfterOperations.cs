Runtime: 92 ms, faster than 49.11% of C# online submissions for Final Value of Variable After Performing Operations.
Memory Usage: 39.5 MB, less than 40.74% of C# online submissions for Final Value of Variable After Performing Operations.

public int FinalValueAfterOperations(string[] operations) {
    int x = 0;
    int opLen = operations.Length;
    
    for (int i = 0; i < opLen; ++i) {
        
        string pHolder = operations[i];
        
        if (pHolder.Contains('-')) {
            x--;
        }
        else if (pHolder.Contains('+')) {
            x++;
        }
    

    }
    
    return x;
}