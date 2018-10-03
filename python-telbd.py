CREATE GENERATOR GEN_CASH_ID;

CREATE TABLE CASH (
    ID       INTEGER NOT NULL,
    FAM      VARCHAR(100),
    NAME     VARCHAR(100),
    OTH      VARCHAR(100),
    SPECIAL  VARCHAR(100),
    COMMENT  VARCHAR(100)
);



#! /usr/bin/python
#  coding: cp1251
import kinterbasdb as k, locale, sys
con = k.connect(dsn='10.5.30.182:/usr/games/bd.gdb', user='sadmin', password='0')
cur = con.cursor()

print 'База данных'
print '1 Добавить запись'
print '2 Удалить запись'
print '3 Редактировать запись'
print '4 Вывод всех записей'
param = int(raw_input("Введите значение: "))

def SelectALL():
    SELECT = "select fam, name, oth, special, comment from cash"
    cur.execute(SELECT)
    print '-'*78
    print 'Фамилия'+' '*2+'Имя'+' '*2+'Отчество'+' '*2+'Специальность'+' '*2+'Kомментарий'
    print '-'*78
    for row in cur:
        print "%s   %s   %s   %s   %s" % (row[0],row[1],row[2],row[3],row[4])


def InsertRecord(fam,name,oth,special,comment):
    INSERT="insert into cash (fam, name, oth, special, comment) values (?,?,?,?,?)"
    cur.execute(INSERT,(fam,name,oth,special,comment))
    con.commit()

def DeleteRecord():
    cur.execute("delete from cash")
    con.commit()

def UpdateRecord(fam,name,oth,special,comment,poisk):
    update="update cash set fam = ?,name=?,oth=?,special=?,comment=? where fam containing ?"
    cur.execute(update,(fam,name,oth,special,comment,poisk))
    con.commit()
if param==4:
    SelectALL()
if param==1:
    fam=raw_input('Введите Фамилию: ')
    name=raw_input('Введите Имя: ')
    oth=raw_input('Введите Отчество: ')
    special=raw_input('Введите должность: ')
    comment=raw_input('Введите комментарий: ')
    InsertRecord(fam,name,oth,special,comment)
if param==2:
    DeleteRecord()
if param==3:
    SelectALL()
    poisk=raw_input('Введите кого будем править: ')
    fam=raw_input('Введите Фамилию: ')
    name=raw_input('Введите Имя: ')
    oth=raw_input('Введите Отчество: ')
    special=raw_input('Введите должность: ')
    comment=raw_input('Введите комментарий: ')
    UpdateRecord(fam,name,oth,special,comment,poisk)

