# pip install numpy
# pip install pandas
# pip install pyplot
# pip install matplotlib
# pip list
# pip show selenium

import csv
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def t2k(tag):
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6,s7 from loto7 '''
    cas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cas = [0 for i in range(39)]
    cr = con.execute(sqlcmd)
    for da in cr:
        if tag[0] in da:
            for x in da:
                cas[x] = cas[x]+1
        pass

    # print(cas)
    # print(tag[1])
    # print(cas[tag[1]])
    con.close()
    if cas[tag[1]] < 13:
        return cas[tag[1]]
    else:
        return cas[tag[1]]

# print (t2k([37, 13]))
# print (t2k([37, 21]))
# print (t2k([37, 2]))
# t2k([1, 37])


def t7t2k(tag, v):
    x = len(tag)
    y = len(tag)
    f = 1
    fc8 = 0  # 8より小さいの組合せ
    fc8c = 2  # 8より小さいの組合せ2個より多い場合,廃棄
    fc16 = 0  # 16より小さいの組合せ
    fc16c = 27  # 16より小さいの組合せ27個より多い場合,場合廃棄
    vw = []
    for i in range(x):
        for j in range(y):
            if v == 1:
                print(tag[i], tag[j])
                print(t2k([tag[i], tag[j]]))
                vw.append(t2k([tag[i], tag[j]]))
            if v == 2:
                vw.append(t2k([tag[i], tag[j]]))
            temp = t2k([tag[i], tag[j]])
            if temp < 8:
                fc8 = fc8+1
            if fc8 == fc8c:
                f = 0
            if temp < 16:
                fc16 = fc16+1
            if fc16 > fc16c:
                f = 0
    if v == 1:
        vw.sort()
        print(tag, vw)
    if v == 2:
        vw.sort()
        return vw
    return f

# print(t7t2k([2,16,17,24,25,35,36],1))   ## return 0
# print(t7t2k([9,14,22,26,27,33,37],1))   ## return 1


def t7t2klist():
    fw = open('xList2-l7.csv', 'w', newline='')
    fr = open('loto7c.csv', 'r')
    cr = csv.reader(fr)

    for cc in cr:
        cw = csv.writer(fw, delimiter='\t')
        tl = []
        tl.append(cc)
        temp = t7t2k([int(cc[2]), int(cc[3]), int(cc[4]), int(
            cc[5]), int(cc[6]), int(cc[7]), int(cc[8])], 2)
        for i in temp:
            tl.append(i)
        cw.writerow(tl)
        # break
    fw.close()
    fr.close()


# t7t2klist()

def t7t2kone(cc):
    # print(cc)
    temp = t7t2k([int(cc[0]), int(cc[1]), int(cc[2]), int(
        cc[3]), int(cc[4]), int(cc[5]), int(cc[6])], 2)
    print(temp)


# t7t2one([0,0,1,2,3,4,5,6,7])

def bas2(tag, l=9):
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = 'select * from loto7'
    cas = [i for i in range(1, 38)]
    cr = con.execute(sqlcmd)
    llist = []
    print('////////////////////////////////////////')
    print('///////////////           //////////////')
    print('////////////////////////////////////////')
    for val in cr:
        temp = list(val[2:l])
        flg = 0
        for k in tag:
            if k not in temp:
                flg = 1
        if flg == 0:
            print(val)
            # print(str(val[0])+'  '+str(val[1]), temp)
            for k in temp:
                llist.append(k)
            # llist.append(temp)
    print('////////////////////////////////////////')
    print('all', llist)
    for k in cas:
        if llist.count(k) >= 5:
            print(k, str(llist.count(k))+'  ++')
        elif llist.count(k) == 0:
            print(k, str(llist.count(k))+'  --')
        else:
            print(k, str(llist.count(k))+'    ')
# bas2([7,11])


def t1():
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    url2 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7c.csv'
    # lpd = pd.read_csv(url1, header=None)
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    # lpd = pd.read_csv(url1,names=('t1','d1','s1','s2','s3','s4','s5','s6','s7','b1','b2','n1','n2','n3','z1','z2'))
    lpd = pd.read_csv(url1, names=('t1', 'd1', 's1', 's2', 's3', 's4', 's5', 's6', 's7',
                      'b1', 'b2', 'n1', 'n2', 'n3', 'z1', 'z2'), usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])
    # lpd = pd.read_csv(url1, header=None, usecols=[1, 2, 3, 4, 5, 6, 7, 8, ])

    lpd.set_index('d1')
    lpd.index
    lpd.plot()
    # lpd.plot('d1', ['s1', 's2', 's3', 's4', 's5', 's6', 's7'])
    plt.show()
    print('77')


def tx1(num):
    # xStep-L7.csv ファイルから出番の間隔確認
    import csv
    f = open('xStep-L7.csv', 'r')
    da = csv.reader(f)
    for x in da:
        if int(num) > int(x[0]) and int(num) < int(x[1]):
            if int(x[2]) > 1:
                return 2
            return 1
    return 0

# tx1(8149925)


def t6():
    # 番号指定 Loto7
    # 出る番号と除外番号を指定し，ランダムに番号を出す
    import sqlite3
    con = sqlite3.connect('alll7.db')
    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473'''
    sqlcmd = '''select * from alll7 where id=abs(random())%10280000'''

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >1458200 and id < 8041128 '''
    # loto7.loc[:,12].describe()
    # mean	5365861e+06
    # std	3031056e+06
    # min	1458200e+04
    # 25%	2820762e+06
    # 50%	5539011e+06
    # 75%	8041128e+06
    # max	1027423e+07

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >2940107 and id < 9016912 '''
    # loto7.loc[0:20,[12]].describe()
    # mean	4965708e+06
    # std	5729267e+06
    # min	9145050e+05
    # 25%	2940107e+06
    # 50%	4965708e+06
    # 75%	6991310e+06
    # max	9016912e+06

    # 番号指定 Loto7
    # tag = [[回数],[予想番号],[除外番号]]
    # tag = [[458],[5, 9, 15, '17+', 31, '33+', 36],[3, 4, 6, '11+', '12+', 16, 20, 23]]
    tag2 = [
        [459],  # 回数
        [12, 15, 9, 26, 33, 30, 35, 34, 11, 13, 21, 27, 23, 31, 36],  # 存在リスト
        [33, 20, 18, 29, 6, 1, 32, 28],  # 非存在リスト
        [3],  # 存在回数
        [3]  # 非存在回数
    ]

    # tag = [[459], [2+,5,6,7+,8+,9,10+,11,12,13,14,15,17,18,21,22,23,24,26,27,31,33,34,36], [1,3,4+,16,19,20+,25,28,29+,30,32,35,37], [3], [3]]
    # tag = [[460], [1, 2, 3, 4+, 5*, 6*, 7, 9*, 10, 11, 12, 14, 15, 17, 19, 20, 21, 23*, 24, 26, 27*, 28*, 30*, 31, 32, 33, 34, 35, 36, 37], [8, 13+, 16, 18, 22, 25, 29], [3], [1]]
    tag = [[463], [5, 6, 27], [0], [2], [0]]

    tagx = [
        [459],
        list(range(1, 38)),
        list(range(38, 48)),
        [0],
        [0]
    ]

    ccont = 100    # 結果の回数
    x = 1
    pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    pool = [i for i in range(1, 38)]
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            nocnt = 0  # 除外カウンタ
            incnt = 0  # 存在カウンタ
            for j in tag[2]:
                if j in xx:
                    nocnt = nocnt + 1

            if nocnt == tag[4][0]:
                for j in tag[1]:
                    if j in xx:
                        incnt = incnt + 1
                if incnt > tag[3][0]:
                    tck = tx1(xx[0])  # 間隔確認
                    if tck == 0 or tck > 1:
                        # print(xx)
                        # print(xx[1:8])
                        # print (t7t2k(list(xx[1:8])))
                        if t7t2k(list(xx[1:8]), 0) == 1:   # 組合せよく出る番号の組合せ
                            if ccont < 11:
                                print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                                    xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], tck, xx[0]))
                            f = open('xList2-l7temp.txt', 'a')
                            f.write("localStorage_additem([{},{},{},{},{},{},{},{},{}])\n".format(
                                xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], tck, xx[0]))
                            f.close()
                            x = x+1
                            print(x, end='\r')
                            ttx = list(xx[1:8])
                            break
        if x > ccont:
            con.close()
            f.close()
            # sys.stdout.write('end')
            break


def t7():
    print('////////////////////////////////////////////')
    print('////////////////////////////////////////////')
    print('////////////////////////////////////////////')
    import random
    import sqlite3
    con = sqlite3.connect('alll7.db')
    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473'''
    # sqlcmd = '''select * from alll7 where id=abs(random())%10280000'''
    sqlcmd = 'select * from alll7 where id='
    pool = list(range(1, 38))

    epool = [
        # [7,11,24,28,31,33,37],
        # [4,8,13,18,22,23,35],
        # [3,6,9,15,25,30,32],
        # [2,7,15,24,29,32,37],
        # [3,7,11,17,29,31,37],
        # [1,7,9,14,25,31,34]
    ]

    tag = [
        [2, 4, 0, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 0],
        [7, 8, 0, 0, 0, 0, 0],
        [7, 11, 0, 0, 0, 0, 0]
    ]

    for val in epool:
        for v in val:
            if v in pool:
                pool.remove(v)
    xc = 0
    sqlcnt = 0
    keep = 40000
    while True:
        keep = keep-1
        cur = con.execute(sqlcmd+str(random.randint(1, 10280000)))
        sqlcnt = sqlcnt+1
        for val in cur:
            tf = True
            temp = val[1:8]
            print('                                                       ', end='\r')
            print(sqlcnt, val, end='\r')
            if keep > 0:
                sqlcnt = sqlcnt-1
                break
            keep = 100
            # 7 8 11 13 14 26 30
            # 5, 6, 7, 8, 32, 33, 34, 36
            # すべての数字が含むか
            # if (temp[0] != 5 or temp[1] != 6 or temp[2] != 7 or temp[3] != 8 or temp[4] != 32 or temp[5] != 34 or temp[6] != 36):
            #     break
            # else:
            #     print('sqlcnt', sqlcnt)

            # # 先頭数字が含むか
            if (temp[0] != 10 or temp[1] != 19):
                break

            # 数字が含むか
            # if 8 not in temp or 13 not in temp :
            #     break
            # if 8 or 13 not in temp:
            #     break

            if t7t2k(list(val[1:8]), 0) == 1:
                for v in temp:
                    if v not in pool:
                        tf = False
                        break

                if tf == True:
                    for vx in temp:
                        pool.remove(vx)

                    tck = tx1(val[0])
                    print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                        val[1], val[2], val[3], val[4], val[5], val[6], val[7], tck, val[0]))
                    f = open('xList2-l7temp.txt', 'a')
                    f.write("localStorage_additem([{},{},{},{},{},{},{},{},{}])\n".format(
                        val[1], val[2], val[3], val[4], val[5], val[6], val[7], tck, val[0]))
                    f.close()
                    tl = []
                    tl.append(val)
                    ttx = list(val[1:8])
                    ttxtag = [7, 8, 13, 17, 30, 32, 36]
                    if ttx == ttxtag:
                        print("////////////////////////////////////////////////////")
                        print(ttx, ttxtag)
                        print(list(val[1:8]))
                        print("////////////////////////////////////////////////////")
                        break

                    temp = t7t2k([int(val[1]), int(val[2]), int(val[3]), int(
                        val[4]), int(val[5]), int(val[6]), int(val[7])], 2)
                    for i in temp:
                        tl.append(i)
                    fw = open('xList2-l7temp.txt', 'a', newline='')
                    # fw = open('xList2-l7.csv', 'a', newline='')   del
                    cw = csv.writer(fw, delimiter='\t')
                    cw.writerow(tl)
                    fw.close()
                    sqlcnt = 0
                    xc = xc+1
                    print('///', pool)

                if sqlcnt > 300:
                    pool = list(range(1, 38))
                    for val in epool:
                        for v in val:
                            if v in pool:
                                pool.remove(v)
                    sqlcnt = 0
                    print('//4//', pool)
                    print('///////////////////////////////////333////////')
                    print('                                                ', end='\r')

                    f = open('xList2-l7temp.txt', 'a')
                    f.write('//------\n')
                    f.close()

                    fw = open('xList2-l7temp.txt', 'a', newline='')
                    # fw = open('xList2-l7.csv', 'a', newline='')    del
                    cw = csv.writer(fw, delimiter='\t')
                    cw.writerow([])
                    fw.close()

        if xc == 100:
            print(pool)
            break
        if sqlcnt == 100000000000:
            print("///1Gend", pool)
            sqlcnt = 0
            con.close()
            break
    con.close()


# t7()


# t6()
# bas2([3,21])  # 9 or 11
# bas2([7,17],9)  # 9 or 11
# 7,11,15,22,26,?,35
# localStorage_additem([7,11,24,28,31,36,37,0,8028009])
# localStorage_additem([7,11,24,30,31,32,36,0,8028089])
# localStorage_additem([7,11,24,28,31,33,37,0,8028003])
# localStorage_additem([7,11,24,30,32,36,37,0,8028110])
# t7t2klist()
# print(t2k([35, 36]))
# print(t7t2k([3,7,10,16,18,19,32,35,37], 1))
# print(t7t2k([3,14, 16, 17, 23, 25, 36], 1))
# 2,3,13,16,20,25,27,30,37
# 000	2020/1/1	6	11	19	22	24	31	35	0	7425431	0	nx5	0	A	22	22	ll7
# fns([4,7,10,21,28,34,36])
# localStorage_additem([12,15,21,25,26,31,0,0,0])
# localStorage_additem([3,4,16,20,23,28,30,32,0])


def ta():
    # 組み合わせ確認
    import csv
    import sqlite3
    f = open('xList-L7.csv', 'w', newline='')
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6,s7 from loto7 '''
    aln = list(range(1, 38))
    print(aln)
    print("")

    cw = csv.writer(f, delimiter='\t')
    for tag in aln:
        cr = con.execute(sqlcmd)
        cas6 = [0 for i in range(45)]
        cas7 = [0 for i in range(38)]
        cas7 = [0] * 38
        cas7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for jj in cr:
            if tag in jj:
                for x in jj:
                    if x >= tag:
                        cas7[x] = cas7[x]+1
        print(tag, cas7)
        cw.writerow(cas7)
    con.close()
    f.close()


ta()
