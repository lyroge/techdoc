### postgresql实用命令收集（更新ing）

1. **查看数据库占用磁盘空间大小<br/>**
    `select pg_database_size('dbname')`

2. **查看数据库中占空间最大的表？<br/>**
    `select relname, relpages from pg_class order by relpages desc;`

3. **查看表大小 pg_relation_size(不含索引)  pg_total_relation_size(含索引) <br/>**
    `select pg_size_pretty(pg_total_relation_size('big_table'));`

4. **将查询结果保存到文件 <br/>**
    `\o output_file \o`