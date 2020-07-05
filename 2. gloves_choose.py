# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Yunsheng Liu
# Date: 2020/7/5

"""
Task:【手套选择】

在抽屉里有20只手套。其中，5双黑手套，3双棕色手套和2双灰手套。
你只能在黑暗中挑手套，并且只有将手套挑出之后才能检査其颜色。
最少要挑几次オ能满足以下条件?
(a)至少挑出一双颜色匹配的手套。
(b)所有颜色的手套都至少挑出一双匹配的。

【参考文献】
[1] Anany Levitin, MariaLevitin, 列维京, et al. 算法谜题[M]. 人民邮电出版社, 2014.
[2] https://www.cnblogs.com/wj033/p/9131528.html
"""


def has_black_pair(data):
    """
    是否含有一对黑手套

    :param data, list, 各手套被取出的数目
    :return: bool
    """
    return data[0] * data[1] > 0


def has_blown_pair(data):
    """
    是否含有一对棕手套

    :param data, list, 各手套被取出的数目
    :return: bool
    """
    return data[2] * data[3] > 0


def has_grey_pair(data):
    """
    是否含有一对灰手套

    :param data, list, 各手套被取出的数目
    :return: bool
    """
    return data[4] * data[5] > 0


def base(max_data, data, task):
    """
    取手套基函数

    :param max_data, list, 各手套最大数目
    :param data, list, 各手套被取出的数目
    :param task, str, 问题任务。
    :return: bool
    """
    for i in range(len(max_data)):
        if data[i] < max_data[i]:
            data[i] += 1
            if task == 'a':
                # 一双手套只能取左或右，直到一边取完不能满足条件，即要保持一双手套一边一直不能取
                cond = (has_black_pair(data)) or (has_blown_pair(data)) or (has_grey_pair(data))
            elif task == 'b':
                # 将最多的两种手套取完，最后再取到颜色最少的灰手套成匹配的
                cond = (has_black_pair(data)) and (has_blown_pair(data)) and (has_grey_pair(data))
            else:
                raise ValueError("参数task只能为的'a'或'b'!")
            if cond:
                data[i] -= 1
            else:
                return True
    return False


def fun(max_data, data, task='a'):
    """
    取手套主函数

    :param max_data, list, 各手套最大数目
    :param data, list, 各手套被取出的数目
    :param task, str, 问题任务。默认为a,可选[a | b]。
        a: 至少挑出一双颜色匹配的手套；
        b: 所有颜色的手套都至少挑出一双匹配的。

    :return: int
    """
    # 初始化挑选次数
    result = 0
    # 计算次数
    while base(max_data, data, task):
        result += 1
    return result + 1


if __name__ == '__main__':
    # 手套数目,分别表示：黑左手套、黑右手套、棕左手套、棕右手套、灰左手套、灰右手套
    max_count = [5, 5, 3, 3, 2, 2]
    # 初始化各手套被取出的数目
    count = [0] * len(max_count)
    # 问题任务a
    ans_a = fun(max_count.copy(), count.copy(), 'a')
    print('(a)至少挑出一双颜色匹配的手套，最多挑{}次。'.format(ans_a))
    # 问题任务b
    ans_b = fun(max_count.copy(), count.copy(), 'b')
    print('(b)所有颜色的手套都至少挑出一双匹配的，最多挑{}次。'.format(ans_b))
