import random


class PokerLineTrainClass(object):
    """
    排火车
    """
    list_cards = []
    list_cards_desktop = []

    def generate(self):
        """
        生成54张牌
        :return:
        """
        self.list_cards = [['大王', 16], ['小王', 15]]
        for num in range(2, 15):
            for des in ('黑桃', '红桃', '梅花', '方块'):
                self.list_cards.append([des, num])
        return self

    def shuffle(self):
        """
        洗牌
        :return:
        """
        length = len(self.list_cards)
        for i in range(0, length-1):
            r = random.randint(i, length-1)
            self.list_cards[i], self.list_cards[r] = self.list_cards[r], self.list_cards[i]
        return self

    def deal(self, n) -> tuple:
        """
        发牌
        :return:
        """
        length = len(self.list_cards)
        n = length//n
        list_deal = []
        for i in range(0, length, n):
            list_deal.append(self.list_cards[i:i+n])
        return tuple(list_deal)

    def play(self, list_poker: list, user):
        """
        出牌
        :param list_poker:
        :param user:
        :return:
        """
        result = False
        index = -1
        value = list_poker.pop()
        # print(user + "出牌：", value)
        # print("桌面牌：", self.list_cards_desktop)

        # 判断是否大小王
        if value == ["大王", 16] or value == ["小王", 15]:
            list_poker[:0] = self.list_cards_desktop
            self.list_cards_desktop = []
            return
        # 判断牌的数字是否存在桌面上
        for v in self.list_cards_desktop:
            index = index + 1
            if value[1] == v[1]:
                result = True
                break
        if result:
            list_pull = self.list_cards_desktop[index:]
            self.list_cards_desktop[index:] = []
            # print(user + "获得火车牌：", list_pull)
            list_poker[:0] = list_pull + [value]
        else:
            self.list_cards_desktop.append(value)
        # print("新桌面牌：", self.list_cards_desktop)


PLT = PokerLineTrainClass()
PLT.generate()
PLT.shuffle()
A, B = PLT.deal(2)
print("甲的牌：", A)
print("乙的牌：", B)
count = 0
while len(A) > 0 and len(B) > 0:
    count = count + 1
    PLT.play(A, '甲')
    PLT.play(B, '乙')
    print(f"\r甲手牌数：{len(A)}, 乙手牌数：{len(B)}", end='')
print()
if len(A) > len(B):
    print("共打了",  count, "轮后，甲赢了！")
elif len(A) < len(B):
    print("共打了 ",  count, " 轮后，乙赢了")
