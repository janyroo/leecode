'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
示例 1:

输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
示例 2:

输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
'''
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # i = 1
        # while i <= num:
        #     i = i << 1    # 比较少用的位移运算符(i自动转换成二进制数)
        # return (i - 1) ^ num     # 通过上述循环，确定了num的二进制数的位数。 通过减一操作，确定这个长度的全一序列进行异或操作。
        #                          # 二进制数和十进制数可以直接异或

        return  (2**(len(bin(num))-2)-1) ^ num # 将方法二的代码浓缩到一行（关键在于确定num的二进制数的长度）
print(Solution().findComplement(num=1))