'''
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
示例 1:输入: 5输出: True解释:5的二进制数是: 101
示例 2:输入: 7输出: False解释:7的二进制数是: 111
示例 3:输入: 11输出: False解释:11的二进制数是: 1011
示例 4:输入: 10输出: True解释:10的二进制数是: 1010
'''
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 二进制由0和1组成,已知相邻的两个位数永不相等,得到00和11不存在bin(n)中
        return '00' not in bin(n) and '11' not in bin(n)
print(Solution().hasAlternatingBits(n=4))