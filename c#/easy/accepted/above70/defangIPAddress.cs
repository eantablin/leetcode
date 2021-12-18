// Runtime: 134 ms, faster than 10.53% of C# online submissions for Defanging an IP Address.
// Memory Usage: 34.9 MB, less than 78.02% of C# online submissions for Defanging an IP Address.

string Address = "1.1.1.1"

public string DefangIPaddr(string address) {
    string validIP = address.Replace(".", "[.]");
    return validIP;
}
