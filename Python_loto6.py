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
    con = sqlite3.connect('alll6.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6 from loto6 '''
    cas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    fw = open('xList2-l6.csv', 'w', newline='')
    fr = open('loto6c.csv', 'r')
    cr = csv.reader(fr)

    for cc in cr:
        cw = csv.writer(fw, delimiter='\t')
        tl = []
        tl.append(cc)
        temp = t7t2k([int(cc[2]), int(cc[3]), int(cc[4]), int(
            cc[5]), int(cc[6]), int(cc[7])], 2)
        for i in temp:
            tl.append(i)
        cw.writerow(tl)
        # break
    fw.close()
    fr.close()


# t7t2klist()


def tx1(num):
    # xStep-L6.csv ファイルから出番の間隔確認
    import csv
    f = open('xStep-L6.csv', 'r')
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
    con = sqlite3.connect('alll6.db')
    # 指定番号を固定,他の番号をランダム選択
    sqlcmd = '''select * from alll6 where s1=5 and s2=17 and s3!=18 and id>6850000 and id<6880000 and id=abs(random())%10295473 limit 3'''
    x = 1
    while True:
        cur = con.execute(sqlcmd)
        for xx in cur:
            print("localStorage_additem([{},{},{},{},{},{},{},{}])".format(
                xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], 0, xx[0]))
            x = x+1
        if x > 5:
            break


def t6():
    # 番号指定 Loto6
    # 出る番号と除外番号を指定し，ランダムに番号を出す
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = '''select * from alll6 where id=abs(random())%6096454'''

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >1458200 and id < 8041128 '''
    # loto7.loc[:,12].describe()

    # sqlcmd = '''select * from alll7 where id=abs(random())%10295473 and id >2940107 and id < 9016912 '''
    # loto7.loc[0:20,[12]].describe()

    # 番号指定 Loto7
    # tag = [[回数],[予想番号],[除外番号]]
    # tag = [[458],[5, 9, 15, '17+', 31, '33+', 36],[3, 4, 6, '11+', '12+', 16, 20, 23]]
    # tag = [
    #     [1668],  # 回数
    #     [28,37,2,38,12,26,8],  # 存在リスト
    #     [34,20,3,41,1,7,29],  # 非存在リスト
    #     [3],  # 存在回数
    #     [1]  # 非存在回数
    # ]

    tag = [
        [1699],
        list(range(19, 44)),
        list(range(1, 18)),
        [3],
        [0]
    ]

    f = open('temp.txt', 'w')
    ccont = 1000    # 結果の回数
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
                        if t7t2k(list(xx[1:7]), 0) == 1:   # 組合せよく出る番号の組合せ
                            if ccont < 11:
                                print("localStorage_additem([{},{},{},{},{},{},{}])".format(
                                    xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], tck))
                            f.write("localStorage_additem([{},{},{},{},{},{},{}])\n".format(
                                    xx[1], xx[2], xx[3], xx[4], xx[5], xx[6], tck))
                            print(x, end='\r')
                            if list(xx[1:7]) == [5, 16, 21, 24, 31, 34]:
                                print(list(xx[1:7]))
                                break
                        x = x+1
        if x > ccont:
            con.close()
            f.close()
            break

def bas2(tag, l=7):
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = 'select * from loto6'
    cas = [i for i in range(1, 44)]
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



def t7():
    print('////////////////////////////////////////////')
    print('////////////////////////////////////////////')
    print('////////////////////////////////////////////')
    import random
    import sqlite3
    con = sqlite3.connect('alll6.db')
    sqlcmd = 'select * from alll6 where id='
    pool = list(range(1, 44))

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
        cur = con.execute(sqlcmd+str(random.randint(1, 6096454)))
        sqlcnt = sqlcnt+1
        for val in cur:
            tf = True
            temp = val[1:7]
            print('                                                       ', end='\r')
            print(sqlcnt, val, end='\r')
            if keep > 0:
                sqlcnt = sqlcnt-1
                break
            keep = 100
            # 7 8 11 13 14 26 30
            # 5, 6, 7, 8, 32, 33, 34, 36
            # すべての数字が含むか
            # if (temp[0] != 5 or temp[1] != 6 or temp[2] != 7 or temp[3] != 8 or temp[4] != 32 or temp[5] != 34 ):
            #     break
            # else:
            #     print('sqlcnt', sqlcnt)

            # 先頭数字が含むか
            if (temp[0] != 14 or temp[1] != 19):
                break

            # 数字が含むか
            # if 8 not in temp or 13 not in temp :
            #     break
            # if 8 or 13 not in temp:
            #     break

            if t7t2k(list(val[1:7]), 0) == 1:
                for v in temp:
                    if v not in pool:
                        tf = False
                        break

                if tf == True:
                    for vx in temp:
                        pool.remove(vx)

                    tck = tx1(val[0])
                    print("localStorage_additem([{},{},{},{},{},{},{}])".format(
                        val[1], val[2], val[3], val[4], val[5], val[6], val[0]))
                    f = open('xList2-l6temp.txt', 'a')
                    f.write("localStorage_additem([{},{},{},{},{},{},{}])\n".format(
                        val[1], val[2], val[3], val[4], val[5], val[6], val[0]))
                    f.close()
                    tl = []
                    tl.append(val)
                    ttx = list(val[1:7])
                    ttxtag = [7, 8, 13, 17, 30, 32, 36]
                    if ttx == ttxtag:
                        print("////////////////////////////////////////////////////")
                        print(ttx, ttxtag)
                        print(list(val[1:7]))
                        print("////////////////////////////////////////////////////")
                        break

                    temp = t7t2k([int(val[1]), int(val[2]), int(val[3]), int(
                        val[4]), int(val[5]), int(val[6])], 2)
                    for i in temp:
                        tl.append(i)
                    fw = open('xList2-l6temp.txt', 'a', newline='')
                    cw = csv.writer(fw, delimiter='\t')
                    cw.writerow(tl)
                    fw.close()
                    sqlcnt = 0
                    xc = xc+1
                    print('///', pool)

                if sqlcnt > 300:
                    pool = list(range(1, 44))
                    for val in epool:
                        for v in val:
                            if v in pool:
                                pool.remove(v)
                    sqlcnt = 0
                    print('//4//', pool)
                    print('///////////////////////////////////333////////')
                    print('                                                ', end='\r')

                    f = open('xList2-l6temp.txt', 'a')
                    f.write('//------\n')
                    f.close()

                    fw = open('xList2-l6temp.txt', 'a', newline='')
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
# bas2([27,37],7) #7 or 8

# t6()
# t7t2klist()
# print(t2k([22, 25]))
# print(t7t2k([   7,11,12,14,19,21    ], 1))
# 000	2020/1/1	6	11	19	22	24	31	35	0	7425431	0	nx5	0	A	22	22	ll7


def ta():
    # 組み合わせ確認
    import sqlite3
    import csv
    f = open('xList-L6.csv', 'w', newline='')
    con = sqlite3.connect('loto.db')
    sqlcmd = '''select s1,s2,s3,s4,s5,s6 from loto6 '''
    aln = list(range(1, 44))
    print(aln)
    print("")

    cw = csv.writer(f, delimiter='\t')
    for tag in aln:
        cr = con.execute(sqlcmd)
        cas6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for jj in cr:
            if tag in jj:
                for x in jj:
                    if x >= tag:
                        cas6[x] = cas6[x]+1
        print(tag, cas6)
        cw.writerow(cas6)
    con.close()
    f.close()


ta()
