#! /usr/bin/env python3
# coding:utf-8
"""
测试去重，及各种方法文件
"""
# abc = "25050@qq.com"
# tt = "nihao中国"
# tel = "1310062"
# ll = ['2505034080@qq.com,中国第一,2017/07/07 14:05', ''], ['23455642@qq.com', '日本倒数第一', '2017/07/07 14:05', '13100625913']]
# with open('temp.txt', mode='a') as f:
#     f.writelines(ll)





# a1 = [12, 1, 32, 12, 43, 32, 1]
# ll = []
# for i in range(0, len(a1)):
#     if a1.index(a1[i]) != i:
#         ll.append(i)
# # 将重复元素的索引序号反序，
# # 从列表后面开始删除元素，这很重要，
# # 否则，从前面开始删除元素导致原列表长度改变，
# # 从而索引位置不对应，造成下标超出错误
# ll.reverse()
# if ll:
#     for y in ll:
#         del a1[y]
# print(a1)
#
#



# print(a1.index(a1[2]))
# temp = []
# for x in range(0, len(a1)):
#     temp.append(a1.index(a1[x]))
#
# print(temp)
# index = list(set(temp))
# target = []
# for i in range(0, len(index)):
#     target.append(a1[index[i]])
# print(target)
