#####################################
#Скрипт консольной телефонной книги #
#####################################
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import pgdb
conn = pgdb.connect('localhost:testdb:postgres')

def vivod_all():
    cur = conn.cursor()
    cur.execute("select * from phbook")
    rows = cur.fetchall()
    for row in rows:
        print row[0], row[1], row[2]
    cur.close()

def insert_phbook(in_person, in_post, in_tel):
    cur = conn.cursor()
    cur.execute("insert into phbook (person, post, phone) values (?,?,? )", (in_person, in_post, in_tel))
    conn.commit()
    print "Запись сделанна"
    conn.close()
    #print in_person

print '1) Вывести все записи'
print '2) Добавить запись'
print '3) Удалить все записи'
str = input("Выберите значение: ");
#print "Received input is : ",str
if str == 1:
    vivod_all()
else:
    if str == 2:
        in_person = raw_input("Введите ФИО: ");
        in_post = raw_input("Введите должность: ");
        in_phone = raw_input("Введите телефон: ");
        insert_phbook(in_person, in_post, in_phone)
    else:
        if str == 3:
            print 'Нажад 3'
################################################################################################################################
#Скрипт смотрит ип  в файло и заходит на них выполняя линуксовую команду
###############################################################################################################################

import fdb,paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
con = fdb.connect(
    host='10.1.108.234', database='/base/stp_gm.gdb',
    user='XXX', password='XXX'
  )
cur = con.cursor()  
f = open('C:\install\work\gm.txt', 'r')
SpisokGmSergo = [line.strip() for line in f]

with open(r"\\10.5.5.16\share\itog.csv", "w") as file:
    file.write('ip;code;name;count\n')     
for i in SpisokGmSergo:
    cur.execute("select ip_gm.lan_ip, gms.code, gms.namegm from ip_GM, gms where ip_GM.id=gms.id and gms.filial_id is not null and gms.code='%s'" % i)
    for row in cur:
        try:
                #print(row[0]+' '+row[1]+' '+row[2])
                ssh.connect(row[0], username='root', password='stenosis')
                stdin,stdout,stderr=ssh.exec_command("ls -ldt /var/db/salepoint/transact/* |wc -l")
                result=str(stdout.readlines()[0])
                s=row[0]+';'+row[1]+';'+row[2]+';'+result
                print (s)
                with open(r"\\10.5.5.16\share\itog.csv", "a") as file:
                    file.write('%s' % s)
        except Exception as u:
            print(u)

