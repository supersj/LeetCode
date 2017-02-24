# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
# Subscribe to see which companies asked this question
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a+b+c+d == len(s):
                            A = int(s[0:a])
                            B = int(s[a:a+b])
                            C = int(s[a+b:a+b+c])
                            D = int(s[a+b+c:a+b+c+d])
                            if A<=255 and B<=255 and C<= 255 and D<=255:
                                ans = str(A)+'.'+str(B)+'.'+str(C)+'.'+str(D)
                                if len(ans) == len(s) + 3:
                                    res.append(ans)
        return res





"""

public List<String> restoreIpAddresses(String s) {
    List<String> solutions = new ArrayList<String>();
    restoreIp(s, solutions, 0, "", 0);
    return solutions;
}

private void restoreIp(String ip, List<String> solutions, int idx, String restored, int count) {
    if (count > 4) return;
    if (count == 4 && idx == ip.length()) solutions.add(restored);

    for (int i=1; i<4; i++) {
        if (idx+i > ip.length()) break;
        String s = ip.substring(idx,idx+i);
        if ((s.startsWith("0") && s.length()>1) || (i==3 && Integer.parseInt(s) >= 256)) continue;
        restoreIp(ip, solutions, idx+i, restored+s+(count==3?"" : "."), count+1);
    }
}
"""
