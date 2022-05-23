# Docker+MySQL環境

## 1. 起動

以下のコマンド実行すると、Docker環境が構築され、コンテナが起動する。

```bash
$ docker-compose up -d
```

コンテナリストの表示

```bash
$ docker-compose ps
      Name                   Command            State            Ports
--------------------------------------------------------------------------------
docker_mysql_db_1   docker-entrypoint.sh        Up      0.0.0.0:3314->3306/tcp,
                    mysqld                              33060/tcp
```

## 2. MySQLサーバに接続

bashで入って確認する手順。


```
$ docker exec -it docker_mysql_db_1 bash
# mysql -u user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.24 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use fap_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------+
| Tables_in_fap_db |
+------------------+
| users            |
+------------------+
1 row in set (0.01 sec)

mysql> select * from users;
+----+-------+--------------------------------+
| id | name  | email                          |
+----+-------+--------------------------------+
|  1 | kioto | kioto-hirahara.kh1@mamezou.com |
+----+-------+--------------------------------+
1 row in set (0.00 sec)

mysql> quit;
# exit
```

ターミナルから接続する手順。

```bash
$ mysql --host 127.0.0.1 --port 3314 -u user -p
Enter password:
（以下略）
```

## 3. 停止と削除

普通に止めるのはstop。

```bash
$ docker-compose stop
```

再び起動する場合はstart。

```bash
$ docker-compose start
```

停止して削除する場合。`docker rm`までやってくれる。

```bash
$ docker-compose down -v
```

以上
