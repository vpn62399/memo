import csv
import pathlib
import sqlite3
import sys
import os

# s1=1-31
# s2=(s1-1)-32
# s3=(s2-1)-33
# s4=(s3-1)-34
# s5=(s4-1)-35
# s6=(s5-1)-36
# s7=(s6-1)-37


############################################################################
#                           Loto7                                          #
############################################################################

"""
.mode csv
delete from loto7;
.import loto7.csv loto7
.mode table

+----------+
| count(*) |
+----------+
| 10295472 |
+----------+


1, select * from loto7,alll7 where loto7.s1=alll7.s1 and loto7.s2=alll7.s2 and loto7.s3=alll7.s3 and loto7.s4=alll7.s4 and loto7.s5=alll7.s5 and loto7.s6=alll7.s6 and loto7.s7=alll7.s7;
2, select * from loto7,alll7 where loto7.s1=alll7.s1 and loto7.s2=alll7.s2 and loto7.s3=alll7.s3 and loto7.s4=alll7.s4 and loto7.s5=alll7.s5 and loto7.s6=alll7.s6 and loto7.s7=alll7.s7 order by loto7.t1 desc;
3, update alll7 set n1=(select t1 from loto7 where z1=10274228) where id = 10274228
4, select "update alll7 set n1=(select t1 from loto7 where z2=",z2,") where id=",z2,";" from loto7;
5, select "update alll7 set b1=(select b1 from loto7 where b1=",b1,") where id=",z2,";" from loto7;
5, select "update alll7 set b2=(select b2 from loto7 where b2=",b2,") where id=",z2,";" from loto7;


1,  結果例
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+
| t1  |     d1     | s1 | s2 | s3 | s4 | s5 | s6 | s7 | b1 | b2 | n1 |  n2  | n3  | z2 |   z1    |   id    | s1 | s2 | s3 | s4 | s5 | s6 | s7 | b1 | b2 | t1  |
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+
| 454 | 2022/1/21  | 8  | 17 | 21 | 26 | 27 | 29 | 31 | 1  | 33 | 2  | 1 g  | -   | H  | 8691080 | 8691080 | 8  | 17 | 21 | 26 | 27 | 29 | 31 | 1  | 33 | 454 |
| 453 | 2022/1/14  | 2  | 8  | 10 | 21 | 24 | 26 | 35 | 9  | 13 | 1  | 3 g  | -   | C  | 3013039 | 3013039 | 2  | 8  | 10 | 21 | 24 | 26 | 35 | 9  | 13 | 453 |
| 452 | 2022/1/7   | 5  | 17 | 20 | 21 | 31 | 34 | 35 | 8  | 27 | 3  | 1 g  | -   | E  | 6882823 | 6882823 | 5  | 17 | 20 | 21 | 31 | 34 | 35 | 8  | 27 | 452 |
| 451 | 2021/12/24 | 2  | 15 | 22 | 25 | 28 | 33 | 37 | 10 | 17 | 1  | 8 g  | -   | I  | 3492751 | 3492751 | 2  | 15 | 22 | 25 | 28 | 33 | 37 | 10 | 17 | 451 |
| 450 | 2021/12/17 | 2  | 7  | 12 | 15 | 21 | 23 | 30 | 9  | 31 | -  | -    | 4 g | A  | 2916074 | 2916074 | 2  | 7  | 12 | 15 | 21 | 23 | 30 | 9  | 31 | 450 |
| 449 | 2021/12/10 | 2  | 21 | 26 | 27 | 32 | 33 | 34 | 8  | 9  | 1  | 5 g  | -   | D  | 3562253 | 3562253 | 2  | 21 | 26 | 27 | 32 | 33 | 34 | 8  | 9  | 449 |
| 448 | 2021/12/3  | 7  | 21 | 24 | 29 | 32 | 36 | 37 | 22 | 27 | 1  | 10 g | 2 g | B  | 8250297 | 8250297 | 7  | 21 | 24 | 29 | 32 | 36 | 37 | 22 | 27 | 448 |
| 447 | 2021/11/26 | 3  | 5  | 8  | 13 | 26 | 30 | 37 | 25 | 28 | -  | -    | 7 g | F  | 3880097 | 3880097 | 3  | 5  | 8  | 13 | 26 | 30 | 37 | 25 | 28 | 447 |
| 446 | 2021/11/19 | 1  | 7  | 9  | 12 | 15 | 29 | 32 | 11 | 28 | 1  | 10 g | 3 g | B  | 1241514 | 1241514 | 1  | 7  | 9  | 12 | 15 | 29 | 32 | 11 | 28 | 446 |
| 445 | 2021/11/12 | 4  | 22 | 25 | 27 | 28 | 30 | 33 | 2  | 3  | 1  | 10 g | 8 g | D  | 6017308 | 6017308 | 4  | 22 | 25 | 27 | 28 | 30 | 33 | 2  | 3  | 445 |
+-----+------------+----+----+----+----+----+----+----+----+----+----+------+-----+----+---------+---------+----+----+----+----+----+----+----+----+----+-----+


"""


def createSQL_loto7():
    dbname = "alll7.db"
    if not pathlib.Path(dbname).is_file():
        crt = "create table if not exists alll7(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER, s4 INTEGER, s5 INTEGER, s6 INTEGER, s7 INTEGER, b1 INTEGER, b2 INTEGER, t1 INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close
        print("sql-end")


def createNUM_loto7():
    f = open("alll7.csv", "a+", newline="")
    cw = csv.writer(f)
    s1, s2, s3, s4, s5, s6, s7 = 0, 0, 0, 0, 0, 0, 0
    cnt = 0
    lst = 31
    for s1 in range(1, lst + 1):
        for s2 in range(s1 + 1, lst + 2):
            for s3 in range(s2 + 1, lst + 3):
                for s4 in range(s3 + 1, lst + 4):
                    for s5 in range(s4 + 1, lst + 5):
                        for s6 in range(s5 + 1, lst + 6):
                            for s7 in range(s6 + 1, lst + 7):
                                cnt = cnt + 1
                                ast = [cnt, s1, s2, s3, s4, s5, s6, s7, "", "", ""]
                                cw.writerow(ast)
    pass
    f.close()
    print(cnt)
    cnt = 0
    print("end_loto7_10295472")


# createNUM_Loto7():
# createSQL()

############################################################################
#                           Loto6                                          #
############################################################################

"""
6,  select loto6.z1,alll6.id from loto6 inner join alll6 on loto6.z1=alll6.id;
    .mode column
7,  select "update alll6 set t1=(select t1 from loto6 where t1=",t1,") where id=",z1,";" from loto6;
8,  select * from loto6 inner join alll6 on loto6.t1 = alll6.t1 limit 3;
    select * from loto6 inner join alll6 on loto6.t1 = alll6.t1 order by loto6.t1 desc limit 3;
    select * from loto6,alll6 where loto6.s1=alll6.s1 and loto6.s2=alll6.s2 and loto6.s3=alll6.s3 and loto6.s4=alll6.s4 and loto6.s5=alll6.s5 and loto6.s6=alll6.s6;

t1    d1         s1  s2  s3  s4  s5  s6  b1  n1  n2   n3  z2  z1    id    s1  s2  s3  s4  s5  s6  b1  t1
----  ---------  --  --  --  --  --  --  --  --  ---  --  --  ----  ----  --  --  --  --  --  --  --  ----
43    2001/7/26  1   2   3   15  24  26  27  3   -    -   B   6416  6416  1   2   3   15  24  26      43
1574  2021/4/5   1   2   3   20  31  32  13  1   3 g  -   E   8032  8032  1   2   3   20  31  32      1574
423   2008/12/4  1   2   3   30  35  36  21  7   -    -   J   9559  9559  1   2   3   30  35  36      423

9,  select * from loto6c inner join alll6 on loto6c.s1 = alll6.s1 and loto6c.s2 = alll6.s2 and loto6c.s3 = alll6.s3 and loto6c.s4 = alll6.s4 and loto6c.s5 = alll6.s5 and loto6c.s6 = alll6.s6;

    .mode csv
    .once t6cc.csv
10, select loto6c.t1,loto6c.d1,loto6c.s1,loto6c.s2,loto6c.s3,loto6c.s4,loto6c.s5,loto6c.s6,loto6c.b1,loto6c.z2,alll6.id from loto6c inner join alll6 on loto6c.s1 = alll6.s1 and loto6c.s2 = alll6.s2 and loto6c.s3 = alll6.s3 and loto6c.s4 = alll6.s4 and loto6c.s5 = alll6.s5 and loto6c.s6 = alll6.s6;


+------+------------+----+----+----+----+----+----+----+----+----+---------+----+----+----+----+----+----+----+------+
|  t1  |     d1     | s1 | s2 | s3 | s4 | s5 | s6 | b1 | z2 | z1 |   id    | s1 | s2 | s3 | s4 | s5 | s6 | b1 |  t1  |
+------+------------+----+----+----+----+----+----+----+----+----+---------+----+----+----+----+----+----+----+------+
| 1658 | 2022/01/27 | 10 | 11 | 19 | 29 | 30 | 36 | 37 | E  |    | 4776435 | 10 | 11 | 19 | 29 | 30 | 36 |    | 1658 |
| 1658 | 2022/01/27 | 4  | 11 | 14 | 15 | 40 | 41 |    |    |    | 2605423 | 4  | 11 | 14 | 15 | 40 | 41 |    |      |
| 1658 | 2022/01/27 | 7  | 19 | 25 | 29 | 34 | 36 |    | 5  |    | 4102691 | 7  | 19 | 25 | 29 | 34 | 36 |    |      |



"""


def createSQL_loto6():
    dbname = "alll6.db"
    if not pathlib.Path(dbname).is_file():
        crt = "create table if not exists alll6(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER, s4 INTEGER, s5 INTEGER, s6 INTEGER, b1 INTEGER, t1 INTEGER,fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close
        print("sql-end")


def createNUM_loto6():
    f = open("alll6.csv", "a+", newline="")
    cw = csv.writer(f)
    s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
    cnt = 0
    lst = 38
    for s1 in range(1, lst + 1):
        for s2 in range(s1 + 1, lst + 2):
            for s3 in range(s2 + 1, lst + 3):
                for s4 in range(s3 + 1, lst + 4):
                    for s5 in range(s4 + 1, lst + 5):
                        for s6 in range(s5 + 1, lst + 6):
                            cnt = cnt + 1
                            ast = [cnt, s1, s2, s3, s4, s5, s6, "0", "0", "0"]
                            cw.writerow(ast)
    pass
    f.close()
    print(cnt)
    cnt = 0
    print("end_loto6_6096454")


# createSQL_loto6()
# createNUM_loto6()


def fcck434():
    import itertools
    import sqlite3

    dbname = "alll6.db"
    try:
        crt = "create table if not exists fcck434(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER, s4 INTEGER, fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close
    except:
        print("error")
        exit

    con = sqlite3.connect(dbname)
    combos = list(itertools.combinations(range(1, 44), 4))
    for k in combos:
        addint = "insert into fcck434(s1,s2,s3,s4)values(%d,%d,%d,%d)" % (
            k[0],
            k[1],
            k[2],
            k[3],
        )
        print(addint)
        con.execute(addint)
    con.commit()
    con.close
    print("kkk")


# fcck434()


def fcck432():
    import itertools
    import sqlite3

    dbname = "alll6.db"
    try:
        crt = "create table if not exists fcck432(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close
    except:
        print("error")
        exit

    con = sqlite3.connect(dbname)
    combos = list(itertools.combinations(range(1, 44), 2))
    for k in combos:
        addint = "insert into fcck432(s1,s2)values(%d,%d)" % (
            k[0],
            k[1],
        )
        print(addint)
        con.execute(addint)
    con.commit()
    con.close
    print("kkk")

# fcck432()


def fcck373():
    import itertools
    import sqlite3

    try:
        dbname = "alll7.db"
        crt = "create table if not exists fcck37(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER,fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close()
    except:
        print("error")

    con = sqlite3.connect(dbname)
    combos = list(itertools.combinations(range(1, 38), 3))
    for k in combos:
        addint = "insert into fcck37(s1,s2,s3)values(%d,%d,%d)" % (k[0], k[1], k[2])
        print(addint)
        con.execute(addint)
    con.commit()
    con.close
    print("kkk")


# fcck373()


def fcck374():
    import itertools
    import sqlite3

    try:
        dbname = "alll7.db"
        crt = "create table if not exists fcck374(id INTEGER PRIMARY KEY,s1 INTEGER, s2 INTEGER, s3 INTEGER,s4 INTEGER,fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close()
    except:
        print("error")

    try:
        con = sqlite3.connect(dbname)
        combos = list(itertools.combinations(range(1, 38), 4))
        for k in combos:
            addint = "insert into fcck374(s1,s2,s3,s4,fcck)values(%d,%d,%d,%d,%d)" % (
                k[0],
                k[1],
                k[2],
                k[3],
                0,
            )
            print(addint)
            con.execute(addint)
        con.commit()
        con.close
        print("kkk")
    except:
        print("error")


# fcck374()


def fcck372():
    import sqlite3
    import itertools

    try:
        dbname = "alll7.db"
        con = sqlite3.connect(dbname)
        crt = "create table if not exists fcck372(id INTEGER PRIMARY KEY,s1 INTEGER, s2 ,fcck INTEGER)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close()
    except:
        print("error")
        pass

    try:
        combos = list(itertools.combinations(range(1, 38), 2))
        con = sqlite3.connect(dbname)
        for k in combos:
            addint = "insert into fcck372(s1,s2,fcck)values(%d,%d,%d)" % (
                k[0],
                k[1],
                0,
            )
            print(addint)
            con.execute(addint)
        con.commit()
        con.close
        print("kkk")
        pass
    except:
        pass


# fcck372()
