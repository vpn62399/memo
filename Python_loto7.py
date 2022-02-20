# pip install numpy
# pip install pandas
# pip install pyplot
# pip install matplotlib
# pip list
# pip show selenium

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def t2k(tag):
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6,s7 from loto7 '''
    cas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

# print (t2k([37, 1]))
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

# print(t7t2k([2,16,17,24,25,35,36]))


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


def t5():
    # 番号指定
    import sqlite3
    con = sqlite3.connect('alll7.db')
    # 指定番号を固定,他の番号をランダム選択
    sqlcmd = '''select * from alll7 where s1=5 and s2=17 and s3!=18 and id>6850000 and id<6880000 and id=abs(random())%10295473 limit 3'''
    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            # print(xx)
            # print("T_cpt2([{},{},{},{},{},{},{},{}])".format(xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],xx[7],xx[0]))
            print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], 0, xx[0]))
            x = x+1
        if x > 5:
            break


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
    tag = [
        [459],  # 回数
        [12, 15, 9, 26, 33, 30, 35, 34, 11, 13, 21, 27, 23, 31, 36],  # 存在リスト
        [33, 20, 18, 29, 6, 1, 32, 28],  # 非存在リスト
        [1],  # 存在回数
        [1]  # 非存在回数
    ]

    tagx = [
        [459],
        list(range(1, 38)),
        list(range(38, 48)),
        [0],
        [0]
    ]

    x = 1
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
                            print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                                xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], tck, xx[0]))
                            x = x+1
        if x > 10:
            con.close()
            break


t6()
# t7t2klist()
# print(t2k([35, 36]))
# print(t7t2k([   7,11,12,14,19,21    ], 1))
# 000	2020/1/1	6	11	19	22	24	31	35	0	7425431	0	nx5	0	A	22	22	ll7


def t7():
    # 平均値の前後+2-2 (vls + lv)
    # 当たる確率低い
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select * from alll7 where id=abs(random())%10295473'''
    vls = [4, 12, 16, 20, 25, 29, 33]
    x = 0
    lv = 4
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            if int(xx[1]) > (vls[0]-lv) and int(xx[1]) < (vls[0]+lv):
                if int(xx[2]) > (vls[1]-lv) and int(xx[2]) < (vls[1]+lv):
                    if int(xx[3]) > (vls[2]-lv) and int(xx[3]) < (vls[2]+lv):
                        if int(xx[4]) > (vls[3]-lv) and int(xx[4]) < (vls[3]+lv):
                            if int(xx[5]) > (vls[4]-lv) and int(xx[5]) < (vls[4]+lv):
                                if int(xx[6]) > (vls[5]-lv) and int(xx[6]) < (vls[5]+lv):
                                    if int(xx[7]) > (vls[6]-lv) and int(xx[7]) < (vls[6]+lv):
                                        print("localStorage_additem([{},{},{},{},{},{},{},{},{}])".format(
                                            xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], xx[7], '', xx[0]))
                                        x = x+1
        if x > 10:
            cur.close()
            break
# t7()


def t8():
    # 番号指定 Loto6
    # 出る番号と除外番号を指定し，ランダムに番号を出す
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = '''select * from alll6 where id=abs(random())% 6096455'''

    inar = [2, 4, 8]
    notinar = [1, 3, 6, 19, 21, 27, 39]

    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            nocnt = 0
            cnt = 0
            for j in notinar:
                if j in xx:
                    nocnt = nocnt + 1

            if nocnt == 0:
                for j in inar:
                    if j in xx:
                        cnt = cnt + 1
                if cnt == 2:
                    tck = tx1(xx[0])
                    if tck == 0 or tck > 1:
                        print("localStorage_additem([{},{},{},{},{},{},{}])".format(
                            xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], tck, xx[0]))
                        x = x+1
        if x > 10:
            cur.close()
            break


# t8()

def t9():
    # 3個の数字組み合わせ数を確認する．
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select t1,d1,s1,s2,s3,s4,s5,s6,s7 from loto7'''
    list(range(1, 38))

    for i in range(1, 38):
        pass
        # print(i)

    cr = con.execute(sqlcmd)
    ct = 0
    # ck = [8,13,15,21,23,26,30,34]
    ck = [30, 23, 26]
    for b in ck:
        print(b)

    for jj in cr:
        if ck[0] in jj and ck[1] in jj and ck[2] in jj:
            print(jj)
            ct += 1
    print(ck, ct)
    con.close()


# t9()

def ta():
    # 組み合わせ確認
    import sqlite3
    import csv
    f = open('xList-L7.csv', 'w', newline='')
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6,s7 from loto7 '''
    aln = list(range(1, 38))
    print(aln)
    print("")

    cw = csv.writer(f, delimiter='\t')
    for tag in aln:
        cr = con.execute(sqlcmd)
        cas6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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


# ta()
