uwsgi日志分析常用脚本
===================

在用uwsgi服务时，经常需要提取日志中的一些信息分析性能、ip、及访问情况等
本处记录用到的一些脚本

#### 统计uwsgi日志中url访问量次数情况

说明：对于接口、web的访问频次查看时，我们之间提取url及对应访问次数

    cat api.20160614.log | awk '{print $18}'| sort | uniq -c | sort -nr | head -n 10*


#### 统计uwsgi日志中ip请求次数情况

说明：有时受到攻击时需查看请求中的客户端ip情况

    cat api.20160614.log | awk '{print $5}'| sort | uniq -c | sort -nr | head -n 10

#### 统计uwsgi日志中请求响应情况

说明：分析请求中的慢查询
    
    cat api.20160614.log | awk '{print $18, $24}' | sort -nr -k2 | head -n 20
