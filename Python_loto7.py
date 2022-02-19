# pip install numpy
# pip install pandas
# pip install pyplot
# pip install matplotlib
# pip list
# pip show selenium

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

# print (t2k([1, 12]))
# t2k([1, 12])


def t7t2k(tag, v):
    import sqlite3
    con = sqlite3.connect('alll7.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6,s7 from loto7 '''
    # print(tag)
    # print(len(tag))
    x = len(tag)
    y = len(tag)
    f = 1
    fc = 0
    for i in range(x):
        for j in range(y):
            if v == 1:
                print(tag[i], tag[j])
                print(t2k([tag[i], tag[j]]))
            if t2k([tag[i], tag[j]]) < 8:
                fc = fc+1
            if fc == 2:
                f = 0
    con.close()
    return f

# print(t7t2k([2,16,17,24,25,35,36]))


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


def t2():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    lpd = pd.read_csv(url1, header=None)
    lpd.plot()
    plt.show()


def t3():
    filename = 'alll7.csv'
    lpd = pd.read_csv(filename)
    tpd = lpd['n1']
    print(tpd.head())
    # tpd.plot()
    # lpd.plot()
    # plt.show()


def t4():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    url1 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7.csv'
    url2 = 'https://raw.githubusercontent.com/kankanla/memo/master/loto7c.csv'

    lpd1 = pd.read_csv(url1, header=None, usecols=[0, 2, 15])
    lpd2 = pd.read_csv(url2, header=None)

    temp2 = lpd1.loc[lpd1[2] == 3]
    temp = lpd2.loc[lpd2[11].isnull()]
    lpd2 = temp.loc[:, [0, 12]]
    lpd3 = pd.merge(lpd2, temp2, left_on=0, right_on=0)
    print(lpd3.head(10))
    # plt.plot(lpd3[0:100])
    lpd3[0:900].plot()
    plt.show()


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
        [459],
        [12, 15, 9, 26, 30, 35, 34, 11, 13, 21, 27, 23, 31, 36],
        [33, 20, 18, 29, 6, 1, 32, 28]
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

            if nocnt == 1:
                for j in tag[1]:
                    if j in xx:
                        incnt = incnt + 1
                if incnt > 1:
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


# t6()
# print(t2k([35, 36]))
# print(t7t2k([5,17,20,21,31,34,35], 1))
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


ta()
