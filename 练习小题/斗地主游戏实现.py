import random


class PeasantsVsLandlordClass(object):
    """
    斗地主
    """
    _landlord_card: list = []
    _list_cards: list = []
    _list_names: list = []
    _dict_user: dict = {}
    _dict_card_val: dict = {}
    _dict_card_type: dict = {}
    _dict_card_desktop: dict = {'name': '', 'type': '', 'cards': []}
    _list_bridgemate: list = []
    _list_name_index = 0

    def generate(self):
        """
        生成54张牌
        :return:
        """
        self._list_cards = [['大王', 16.1], ['小王', 16]]
        for num in range(1, 14):
            for des in ('黑桃', '红桃', '梅花', '方块'):
                if num == 11:
                    des = des + "J"
                    n = 11
                elif num == 12:
                    des = des + "Q"
                    n = 12
                elif num == 13:
                    des = des + "K"
                    n = 13
                elif num == 1:
                    des = des + "A"
                    n = 14
                elif num == 2:
                    des = des + "2"
                    n = 15
                else:
                    des = des + str(num)
                    n = num
                self._list_cards.append([des, n])
        # print(self._list_cards)
        return self

    def shuffle(self):
        """
        洗牌
        :return:
        """
        self._landlord_card = []
        length = len(self._list_cards)
        for i in range(0, length-1):
            r = random.randint(i, length-1)
            self._list_cards[i], self._list_cards[r] = self._list_cards[r], self._list_cards[i]
        return self

    def deal(self, *list_user):
        """
        发牌
        :return:
        """
        # 抽出三张作为地主牌
        self._landlord_card = []
        for i in range(3):
            card = self._list_cards.pop()
            self._landlord_card.append(card)
        print("【三张地主牌】：", self._landlord_card)
        # 给所有玩家发牌
        self._list_names = list(list_user)
        while len(self._list_cards) > 0:
            for user in list_user:
                # 将一张牌放到玩家手中
                card = self._list_cards.pop()
                # 判断玩家是否在用户列表中
                if self._dict_user.get(user) is None:
                    self._dict_user[user] = {'title': '农民', 'hand': []}
                self._dict_user[user]['hand'] = self._dict_user[user].get('hand', []) + [card]
        # 对玩家手牌进行分析
        for user in list_user:
            # 排序
            self._dict_user[user]['hand'].sort(key=lambda x: x[1])
            # 牌型分组
            self._dict_card_type[user] = self._card_type(self._dict_user[user]['hand'])
        return self

    def rob_lord(self):
        """
        抢地主
        :return:
        """
        index = random.randint(0, len(self._list_names)-1)
        user = self._list_names[index]
        self._dict_user[user]['title'] = '地主'
        self._list_name_index = index
        self._dict_user[user]['hand'] += self._landlord_card
        self._landlord_card = []
        # 排序
        self._dict_user[user]['hand'].sort(key=lambda x: x[1])
        # 牌型分组
        self._dict_card_type[user] = self._card_type(self._dict_user[user]['hand'])
        print(f"【{user}】抢到了地主！")
        return self

    def play(self):
        """
        出牌
        :return:
        """
        # 获取当前玩家
        index = self._list_name_index
        user = self._list_names[index]
        # 获取玩家的信息
        dict_user = self._dict_user[user]
        # 获取玩家的手牌
        list_hand = dict_user['hand']
        # 获取玩家手牌类型
        card_type = self._dict_card_type[user]
        # 返回出牌顺序列表
        list_order = self._card_order(card_type)
        if len(list_order) == 0:
            print(f"【{user}】赢了！------------------------------")
            exit()
        hand = "".join([v[0][-1] for v in list_hand if v])
        if len(self._dict_card_desktop.get('cards')) == 0 or self._dict_card_desktop.get('name') == user:
            # 将取出的牌从手牌中删除
            poker = self._card_pop(user, list_order, list_hand, card_type)
            if poker:
                self._dict_card_desktop = poker
                hand = "".join([v[0][2:] for v in list_hand if v])
                print(f"【{user}】出牌：", poker, len(hand))
            else:
                print(f"【{user}】赢了！++++++++++++++++++++++")
                exit()
        else:
            # 出比上家大的牌，如果没有则跳过
            poker = self._card_comp(user, self._dict_card_desktop, list_order, list_hand, card_type)
            if poker:
                self._dict_card_desktop = poker
                hand = "".join([v[0][2:] for v in list_hand if v])
                print(f"【{user}】出牌：", poker, len(hand))
            else:
                print(f"【{user}】不出！")
        index += 1
        if index >= len(self._list_names):
            index = 0
        self._list_name_index = index
        if len(hand) == 0:
            print(f"【{user}】赢了！==========================")
            exit()

    def _get_card_value(self, poker):
        """
        计算牌型的权重值
        :return:
        """
        weight = ('', 0)
        n = len(poker)
        if n == 1:
            a = poker[0][1]
            # 单张
            weight = ('1', a)
        elif n == 2:
            a, b = poker[0][1], poker[1][1]
            if a == int(b) == 16:
                # 王炸
                weight = ('4*4', b)
            elif a == b:
                # 对子
                weight = ('2', b)
        elif n == 3:
            a, b, c = poker[0][1], poker[1][1], poker[2][1]
            if a == b == c:
                # 三条
                weight = ('3', a)
        elif n == 4:
            a, b, c, d = poker[0][1], poker[1][1], poker[2][1], poker[3][1]
            if a == b == c == d:
                # 炸弹
                weight = ('4*4', a)
            elif a == b == c != d:
                # 三带一
                weight = ('3-1', a)
        elif n == 5:
            a, b, c, d, e = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1]
            if a == b == c == d and d != e:
                # 四带一
                weight = ('4-1', a)
            elif a == b == c != d and d == e:
                # 三带二
                weight = ('3-2', a)
            elif a+4 == b+3 == c+2 == d+1 == e:
                # 五连顺
                weight = ('5', a)
        elif n == 6:
            a, b, c, d, e, f = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1]
            if a == b == c == d and d != e == f:
                # 四带二
                weight = ('4-1-1', a)
            elif a+5 == b+4 == c+3 == d+2 == e+1 == f:
                # 六连顺
                weight = ('6', f)
            elif a+2 == b+2 == c+1 == d+1 == e == f:
                # 三连对
                weight = ('2-2-2', f)
        elif n == 7:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            if a == b == c == d and (e == f != g or e != f == g):
                # 四带二加一
                weight = ('4-2-1', a)
            elif a+6 == b+5 == c+4 == d+3 == e+2 == f+1 == g:
                # 七连顺
                weight = ('7', g)
        elif n == 8:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            h = poker[7][1]
            if a == b == c == d and e == f and g == h and f != g:
                # 四带对子
                weight = ('4-2-2', a)
            elif a+7 == b+6 == c+5 == d+4 == e+3 == f+2 == g+1 == h:
                # 八连顺
                weight = ('8', h)
            elif a+3 == b+3 == c+2 == d+2 == e+1 == f+1 == g == h:
                # 四连对
                weight = ('2-2-2-2', h)
            elif a == b == c and d == e == f and len({c, f, g, h}) == 4:
                # 飞机带小翼
                weight = ('3-3-1-1', f)
        elif n == 9:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            h, i = poker[7][1], poker[8][1]
            if a+8 == b+7 == c+6 == d+5 == e+4 == f+3 == g+2 == h+1 == i:
                # 九连顺
                weight = ('9', i)
            elif a == b == c and d == e == f and len({g, h, i}) == 2:
                # 飞机带小翼
                weight = ('3-3-2-1', i)
            elif a == b == c and d == e == f and g == h == i:
                # 飞机
                weight = ('3-3-3', i)
        elif n == 10:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            h, i, j = poker[7][1], poker[8][1], poker[9][1]
            if a+9 == b+8 == c+7 == d+6 == e+5 == f+4 == g+3 == h+2 == i+1 == j:
                # 十连顺
                weight = ('10', j)
            elif a+4 == b+4 == c+3 == d+3 == e+2 == f+2 == g+1 == h+1 == i == j:
                # 五连对
                weight = ('2-2-2-2-2', j)
            elif a == b == c and d == e == f and len({g, h, i, j}) == 2:
                # 飞机带大翼
                weight = ('3-3-2-2', f)
        elif n == 11:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            h, i, j, k = poker[7][1], poker[8][1], poker[9][1], poker[10][1]
            if a+10 == b+9 == c+8 == d+7 == e+6 == f+5 == g+4 == h+3 == i+2 == j+1 == k:
                # 十一连顺
                weight = ('11', k)
        elif n == 12:
            a, b, c, d, e, f, g = poker[0][1], poker[1][1], poker[2][1], poker[3][1], poker[4][1], poker[5][1], poker[6][1]
            h, i, j, k, l = poker[7][1], poker[8][1], poker[9][1], poker[10][1], poker[11][1]
            if a+11 == b+10 == c+9 == d+8 == e+7 == f+6 == g+5 == h+4 == i+3 == j+2 == k+1 == l:
                # 十二连顺
                weight = ('12', l)
            elif a+5 == b+5 == c+4 == d+4 == e+3 == f+3 == g+2 == h+2 == i+1 == j+1 == k == l:
                # 六连对
                weight = ('2-2-2-2-2-2', l)
            elif a == b == c and d == e == f and g == h == i and j == k == l:
                # 飞机
                weight = ('3-3-3-3', l)
        return weight

    def _card_comp(self, user, poker, list_order, list_hand, card_type):
        """
        比较手牌中的牌是否可出
        :return:
        """
        # 获取对方牌的牌型
        c_type = poker['type']
        cards = poker['cards']
        card_val1 = self._get_card_value(cards)
        # print("**********************************************", c_type, card_type[c_type])
        types = [c_type, '炸弹', '王炸']
        for c_type in types:
            for list_v in card_type[c_type]:
                list_v = [list_v] if c_type == '单张' else list_v
                cards = []
                # print("________________________________________", list_v, " = ", end=' ')
                for i in list_v:
                    # print(list_hand[i], end=' ')
                    # 获取列表中的对应位置是否有元素
                    ele = list_hand[i]
                    if ele is None:continue
                    # 获取牌是面值数字
                    cards.append(ele)
                # print()
                if len(cards) == 0: continue
                card_val2 = self._get_card_value(cards)
                if card_val1[0] != '4*4' and card_val2[0] == '4*4':
                    for j in list_v:
                        # print("===============================", j)
                        list_hand[j] = None
                        if j in card_type[c_type]:
                            card_type[c_type].remove(j)
                    return {'name': user, 'type': c_type, 'cards': cards}
                elif card_val1[0] == card_val2[0]:
                    if card_val1[1] < card_val2[1]:
                        # print("=======cards===========", cards)
                        for j in list_v:
                            # print("===============================", j)
                            list_hand[j] = None
                            if j in card_type[c_type]:
                                card_type[c_type].remove(j)
                        # print(card_val1, card_val2)
                        return {'name': user, 'type': c_type, 'cards': cards}
                else:
                    print(card_val1, card_val2)

    @classmethod
    def _card_pop(cls, user, list_order, list_hand, card_type) -> dict | None:
        """
        从手牌中取出指定的牌
        :param poker:
        :return:
        """
        # 获取玩家的手牌
        # list_hand: list = self._dict_user[user]['hand']
        # 获取玩家手牌类型
        # card_type = self._dict_card_type[user]
        # 将指定牌的牌型和手牌索引
        if len(list_order) == 0:
            return
        poker = list_order[0]
        c_type = poker[0]
        value = poker[1]
        # 从牌型里删除对应的牌的索引
        card_type[c_type].remove(value)
        # 单张返回的是非列表型
        if c_type == '单张':
            # 需要转换为列表型
            value = [value]
        # 将手牌的值复制一份到临时变量（避免引用到同一个内存地址）
        list_tmp = list_hand[:]
        # 定义返回的牌
        result = {'name': user, 'type': c_type, 'cards': []}
        # 遍历牌型所有索引
        for i in value:
            # 根据索引，从临时手牌中取出对应的牌
            card = list_hand[i]
            # 获取列表中的对应位置是否有元素
            if card is None: continue
            # 从手牌中删除对应的牌
            list_hand[i] = None
            # 将取出的牌放入返回的变量中
            result['cards'].append(card)
        if len(result['cards']) > 0:
            return result

    def _card_order(self, card_type: dict) -> list:
        """
        返回出牌顺序列表
        :param card_type: 牌型字典
        :return:
        """
        list_order = []
        list_type = ['飞机', '顺子', '连对', '单张', '对子', '三条', '炸弹', '王炸']
        for t in list_type:
            for v in card_type[t]:
                list_order.append([t, v])
        # print(list_order)
        return list_order

    def _card_type(self, list_hand: list) -> dict:
        """"
        玩家手牌进行牌型分组
        """
        # 定义分组字典，牌面数字相同的索引放到同一组
        dict_group = {}
        # 定义牌型字典，储存玩家手牌中的所有牌型
        card_type = {
            '王炸': [],
            '炸弹': [],
            '飞机': [],
            '顺子': [],
            '连对': [],
            '三条': [],
            '对子': [],
            '单张': []
        }
        # 获取玩家的手牌
        # list_hand: list = self._dict_user[user]['hand']
        # 遍历手牌中的每个牌，进行分组归类
        length = len(list_hand)
        for i in range(length):
            # 获取列表中的对应位置是否有元素
            ele = list_hand[i]
            if ele is None: continue
            # 获取牌是面值数字
            val = ele[1]
            # 强转整型（为了让大王和小王分到同一组）
            val = int(val)
            # 判断分组字典是否存在该面值数字
            if dict_group.get(val) is None:
                # 不存在则创建一个空列表
                dict_group[val] = []
            # 往列表中追加手牌的索引到分组字典中
            dict_group[val].append(i)
        # 遍历分组字典
        for key in dict_group:
            # 获取分组字典对应的键值
            value = dict_group[key]
            # 判断键值长度
            count = len(value)
            if count == 4:
                # 炸弹
                card_type['炸弹'].append(value)
            elif count == 3:
                # 三条
                card_type['三条'].append(value)
            elif count == 2:
                if key == 16:
                    # 王炸
                    card_type['王炸'].append(value)
                else:
                    # 对子
                    card_type['对子'].append(value)
            elif count == 1:
                # 单张
                card_type['单张'].append(value[0])
        # 从单牌中提取顺子
        card_type = self._extract_straight(list_hand, card_type)
        # 从三条中提取飞机
        card_type = self._extract_plane(list_hand, card_type)
        # 从对子中提取连对
        card_type = self._extract_double(list_hand, card_type)
        return card_type

    @classmethod
    def _extract_straight(cls, list_hand: list, card_type: dict) -> dict:
        """
        单牌中提取顺子
        :return:
        """
        # 获取玩家的手牌
        # list_hand: list = self._dict_user[user]['hand']
        # 提取玩家牌型
        # card_type = self._dict_card_type[user]
        # 获取单张列表
        list_single = card_type['单张'][:]
        # 遍历分析顺子
        straight_val = []
        straight_index = []
        end = False
        length = len(card_type['单张'])
        for i in range(length):
            if i == length - 1:
                end = True
            index = card_type['单张'][i]
            # 获取列表中的对应位置是否有元素
            ele = list_hand[index]
            if ele is None: continue
            # 获取牌是面值数字
            val = ele[1]
            if len(straight_val) == 0:
                straight_val.append(val)
                straight_index.append(index)
            elif straight_val[-1] == 15:
                end = True
            elif straight_val[-1] == val:
                pass
            elif straight_val[-1] + 1 == val:
                straight_val.append(val)
                straight_index.append(index)
            else:
                end = True
            if len(straight_val) >= 5 and end:
                for v in straight_index:
                    if v in list_single:
                        list_single.remove(v)
                card_type['顺子'].append(straight_index)
            if end:
                end = False
                straight_val = [val]
                straight_index = [index]
        card_type['单张'] = list_single
        # print(list_hand)
        # print(card_type)
        return card_type

    @classmethod
    def _extract_plane(cls, list_hand: list, card_type: dict) -> dict:
        """
        飞机（两个以上顺序的三条）
        :param user:
        :return:
        """
        # 获取玩家的手牌
        # list_hand: list = self._dict_user[user]['hand']
        # 提取玩家牌型
        # card_type = self._dict_card_type[user]
        # 获取三条列表
        list_three = card_type['三条'][:]
        # 遍历分析飞机
        plane_val = []
        plane_index = []
        end = False
        length = len(card_type['三条'])
        for i in range(length):
            if i == len(card_type['三条'])-1:
                end = True
            index = card_type['三条'][i]
            # 获取列表中的对应位置是否有元素
            ele = list_hand[index[0]]
            if ele is None: continue
            # 获取牌是面值数字
            val = ele[1]
            # print(index[0], list_hand[index[0]])
            if len(plane_val) == 0:
                plane_val.append(val)
                plane_index.append(index)
            elif plane_val[-1] == 15:
                end = True
            elif plane_val[-1]+1 == val:
                plane_val.append(val)
                plane_index.append(index)
            else:
                end = True
            if len(plane_val) >= 2 and end:
                for v in plane_index:
                    if v in list_three:
                        list_three.remove(v)
                if len(card_type['对子']) >= len(plane_val):
                    # 飞机带对子
                    wing = card_type['对子'][:len(plane_val)]
                    for v in wing:
                        card_type['对子'].remove(v)
                    wing = sum(wing, [])
                    plane_index.append(wing)
                elif len(card_type['单张']) >= len(plane_val):
                    # 飞机带单张
                    wing = card_type['单张'][:len(plane_val)]
                    for v in wing:
                        card_type['单张'].remove(v)
                    plane_index.append(wing)
                plane_index = sum(plane_index, [])
                card_type['飞机'].append(plane_index)
            if end:
                end = False
                plane_val = [val]
                plane_index = [index]
        card_type['三条'] = list_three
        # print(plane_val)
        # print(plane_index)
        # print(card_type)
        return card_type

    @classmethod
    def _extract_double(cls, list_hand: list, card_type: dict) -> dict:
        """
        连对（3个以上顺序的对子）
        :param user:
        :return:
        """
        # 获取玩家的手牌
        # list_hand: list = self._dict_user[user]['hand']
        # 提取玩家牌型
        # card_type = self._dict_card_type[user]
        # 获取对子列表
        list_pair = card_type['对子'][:]
        # 遍历分析连对
        double_val = []
        double_index = []
        end = False
        length = len(card_type['对子'])
        for i in range(length):
            if i >= length-1:
                end = True
            index = card_type['对子'][i]
            # 获取列表中的对应位置是否有元素
            ele = list_hand[index[0]]
            if ele is None: continue
            # 获取牌是面值数字
            val = ele[1]
            # print(index[0], list_hand[index[0]])
            if len(double_val) == 0:
                double_val.append(val)
                double_index.append(index)
            elif double_val[-1] == 15:
                end = True
            elif double_val[-1]+1 == val:
                double_val.append(val)
                double_index.append(index)
            else:
                end = True
            if len(double_val) >= 3 and end:
                for v in double_index:
                    if v in list_pair:
                        list_pair.remove(v)
                double_index = sum(double_index, [])
                card_type['连对'].append(double_index)
            if end:
                end = False
                double_val = [val]
                double_index = [index]
        card_type['对子'] = list_pair
        # print(double_val)
        # print(double_index)
        # print(card_type)
        return card_type


PL = PeasantsVsLandlordClass()
PL.generate()
PL.shuffle()
PL.deal('甲', '乙', '丙')
PL.rob_lord()
for i in range(30):
    PL.play()
    PL.play()
    PL.play()
