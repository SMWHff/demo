import random


class GoldenFlowerClass(object):
    """
    炸金花
    """
    _list_cards = []
    _dict_user = {}
    _dict_card_val = {}

    def generate(self):
        """
        生成 54 张牌
        :return:
        """
        self._list_cards = []
        for num in range(2, 15):
            for des in ('黑桃', '红桃', '梅花', '方块'):
                self._list_cards.append([des, num])
        return self

    def shuffle(self):
        """
        洗牌
        :return:
        """
        length = len(self._list_cards)
        for i in range(0, length-1):
            r = random.randint(i, length-1)
            self._list_cards[i], self._list_cards[r] = self._list_cards[r], self._list_cards[i]
        return self

    def deal(self, user):
        """
        发牌
        :return:
        """
        for i in range(3):
            card = self._list_cards.pop()
            self._dict_user[user] = self._dict_user.get(user, []) + [card]
        return self._dict_user[user]

    def get_card_value(self, user):
        """
        获取牌值
        :return:
        """
        list_comp = {'特殊': -1, '散牌': 0, '对子': 2, '顺子': 4, '金花': 8, '同花顺': 16, '豹子': 32}
        card_value = 0
        card_type = '散牌'
        card_num = 0
        card: list = self._dict_user[user]
        card.sort(key=lambda x: x[1])
        k1, k2, k3 = card[0][0], card[1][0], card[2][0]
        v1, v2, v3 = card[0][1], card[1][1], card[2][1]
        if v1 == v2 == v3:
            card_num = v3
            card_type = '豹子'
            card_value = list_comp.get(card_type)
        elif v1+2 == v2+1 == v3:
            card_num = v3
            if k1 == k2 == k3:
                card_type = '同花顺'
            else:
                card_type = '顺子'
            card_value = list_comp.get(card_type)
        elif k1 == k2 == k3:
            card_num = v3+v2/100+v1/10000
            card_type = '金花'
            card_value = card_value + list_comp.get(card_type)
        elif v1 == v2:
            card_num = v1+v3/100
            card_type = '对子'
            card_value = list_comp.get(card_type)
        elif v1 == v3:
            card_num = v1+v2/100
            card_type = '对子'
            card_value = list_comp.get(card_type)
        elif v2 == v3:
            card_num = v3+v1/100
            card_type = '对子'
            card_value = list_comp.get(card_type)
        else:
            card_num = v3+v2/100+v1/10000
            if v1 == 2 and v2 == 3 and v3 == 5:
                if k1 != k2 and k1 != k3 and k2 != k3:
                    card_num = 0
                    card_type = '特殊'
                    card_value = -1
        self._dict_card_val[user] = (card_value, card_type, card_num)
        return self._dict_card_val[user]

    def comp(self, value1, value2):
        """
        比较牌值
        :param value1:
        :param value2:
        :return:
        """
        if value1[1] == '特殊' and value2[1] == '豹子':
            return 1
        elif value1[1] == '豹子' and value2[1] == '特殊':
            return -1
        elif value1[0] > value2[0]:
            return 1
        elif value1[0] < value2[0]:
            return -1
        else:
            if value1[2] > value2[2]:
                return 1
            elif value1[2] < value2[2]:
                return -1
            else:
                return 0


GF = GoldenFlowerClass()
GF.generate()
GF.shuffle()
print(GF.deal('甲'))
print(GF.deal('乙'))
print(GF.deal('丙'))
val1 = GF.get_card_value('甲')
val2 = GF.get_card_value('乙')
val3 = GF.get_card_value('丙')
result1 = GF.comp(val1, val2)
result2 = GF.comp(val1, val3)
result3 = GF.comp(val2, val3)
print("甲：", val1)
print("乙：", val2)
print("丙：", val3)
if result1 > 0:
    if result2 > 0:
        print("甲赢了")
    elif result2 < 0:
        print("丙赢了")
    else:
        print("甲丙赢了")
elif result1 < 0:
    if result3 > 0:
        print("乙赢了")
    elif result3 < 0:
        print("丙赢了")
    else:
        print("乙丙赢了")
else:
    if result2 > 0:
        print("甲乙赢了")
    elif result2 < 0:
        print("丙赢了")
    else:
        print("平局")