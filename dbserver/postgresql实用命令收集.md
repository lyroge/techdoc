## postgresql实用命令收集（更新ing）
*** 

#### 查询空间大小
1. ##### 查看数据库占用磁盘空间大小
> select pg_database_size('dbname')

2. ##### 查看数据库中占空间最大的表？
> select relname, relpages from pg_class order by relpages desc;

3. ##### 查看表大小 pg_relation_size(不含索引)  pg_total_relation_size(含索引)
> select pg_size_pretty(pg_total_relation_size('big_table'))



#### 查询应用技巧
1. ##### 将查询结果保存到文件 
> \o output_file \o

2. ##### 查看当前数据库连接情况
> select * from pg_stat_activity;
 
3. ##### 查看锁情况 procpid/pic
> SELECT distinct(procpid), waiting FROM pg_stat_activity WHERE datname='venti' and waiting=true;

4. ##### 清理锁情况 procpid/pid
> SELECT pg_terminate_backend(procpid) FROM pg_stat_activity WHERE procpid <> pg_backend_pid() AND datname = 'venti' ;


### 其他参考资料
1. [15 Practical PostgreSQL Database Administration Commands](http://www.thegeekstuff.com/2009/04/15-practical-postgresql-database-adminstration-commands/)
2. other
