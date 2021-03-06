
"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：

输入：[5,5,10]
输出：true
示例 3：

输入：[10,10]
输出：false
示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
提示：

0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20
"""

#思路:bills[i] - 5 = 0     当前帐单减5   changer[]

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changer = []
        for i in bills:
            changer.append(i)
            if i ==10:
                if 5 in changer:
                    changer.remove(5)
                else:

                    return False
                    break
            if i ==20:
                if 10 in changer and 5 in changer:
                    changer.remove(10)
                    changer.remove(5)
                elif changer.count(5) >=3:
                    changer.remove(5)
                    changer.remove(5)
                    changer.remove(5)
                else:
                    return False
                    break

        return True

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
Solution().lemonadeChange(bills)


#48ms
class Solution1:
    def lemonadeChange1(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        money5, money10, money20 = 0, 0, 0
        for bill in bills:
            if bill == 5:
                money5 += 1
            elif bill == 10:
                if money5 <= 0:
                    return False
                money10 += 1
                money5 -= 1
            else:
                if money10 >= 1 and money5 >= 1:
                    money10 -= 1
                    money5  -= 1
                elif money5 >= 3:
                    money5 -= 3
                else:
                    return False
                money20 += 1
        return True



"""
让我们尝试模拟给每个购买柠檬水的顾客进行找零的过程。最初，我们从没有 5 美元钞票也没有 10 美元钞票的情况开始。

如果顾客支付了 5 美元钞票，那么我们就得到 5 美元的钞票。

如果顾客支付了 10 美元钞票，我们必须找回一张 5 美元钞票。如果我们没有 5 美元的钞票，答案就是 false，因为我们无法正确找零。

如果顾客支付了 20 美元钞票，我们必须找回 15 美元。

如果我们有一张 10 美元和一张 5 美元，那么我们总会更愿意这样找零，这比用三张 5 美元进行找零更有利。

否则，如果我们有三张 5 美元的钞票，那么我们将这样找零。

否则，我们将无法给出总面值为 15 美元的零钱，答案是 false。

---------------------

本文来自 Anarkh_Lee 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/anarkh_lee/article/details/81026146?utm_source=copy 
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int bill: bills) {
            if (bill == 5)
                five++;
            else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else {
                if (five > 0 && ten > 0) {
                    five--;
                    ten--;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}

---------------------

本文来自 Anarkh_Lee 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/anarkh_lee/article/details/81026146?utm_source=copy 
"""