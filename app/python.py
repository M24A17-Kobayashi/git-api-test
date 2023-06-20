from flask import Flask
import mysql.connector

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = 'db-server',      #localhostでもOK
              user = 'localadmin',
              passwd = 'passwd',
              db = 'sample'
      )
      return conn

#本体
sql = 'SELECT * FROM sample'

try:
      conn = conn_db()              #ここでDBに接続
      cursor = conn.cursor()       #カーソルを取得
      cursor.execute(sql)             #selectを投げる
      rows = cursor.fetchall()      #selectの結果を全件タプルに格納
except(mysql.connector.errors.ProgrammingError) as e:
      print('エラー')
      print(e)

print('select結果')
for t_rows in rows:
      print(t_rows[0], t_rows[1], t_rows[2])    #selectの結果を1行ずつ表示