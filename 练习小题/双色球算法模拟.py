# 9、双色球算法模拟
# 红色球号码区由1~33范围数字
# 蓝色球号码区由1-16范围数字
# 投注时选择6个红色球号码和1个蓝色球号码组成一注
import random


class TwoColorBallClass(object):
    """
    双色球
    """

    def lottery_machine(self):
        """
        机选彩票
        :return:
        """
        list_red = [i for i in range(1, 34)]
        list_blue = [i for i in range(1, 17)]
        for i in range(6):
            n = random.randint(i, 32)
            list_red[i], list_red[n] = list_red[n], list_red[i]
        for i in range(1):
            n = random.randint(i, 15)
            list_blue[i], list_blue[n] = list_blue[n], list_blue[i]
        list_red = list_red[:6]
        list_blue = list_blue[:1]
        return list_red, list_blue

    def result(self, nums: tuple, sys_nums: tuple):
        set_red = set(nums[0])
        prize_reds = len(set_red.intersection(set(sys_nums[0])))
        prize_blues = 1 if nums[1][0] == sys_nums[1][0] else 0
        list_prize = {
            (6, 1): "一等奖",
            (6, 0): "二等奖",
            (5, 1): "三等奖",
            (5, 0): "四等奖",
            (4, 1): "四等奖",
            (4, 0): "五等奖",
            (3, 1): "五等奖",
            (2, 1): "六等奖",
            (1, 1): "六等奖",
            (0, 1): "六等奖",
            (3, 0): "未中奖",
            (2, 0): "未中奖",
            (1, 0): "未中奖",
            (0, 0): "未中奖"
        }
        return list_prize[(prize_reds, prize_blues)]


buy = int(input("1：机选\n2：自选\n请选择机选还是自选："))
TCB = TwoColorBallClass()
if buy == 1:
    payno = TCB.lottery_machine()
else:
    rno = input("请输入6个红色球（1~33,空格隔开）：")
    bno = input("请输入1个蓝色球（1~16）：")
    rno = [int(i) for i in rno.split()]
    bno = [int(bno)]
    payno = (rno, bno)
print("购买号码：", payno)

n=0
ret=''
while ret != '一等奖':
    n=n+1
    # print("正在生成开奖号码。。。")
    prize = TCB.lottery_machine()
    # print("开奖号码：", prize)
    ret = TCB.result(payno, prize)
print("开奖号码：", prize)
print(ret, n)