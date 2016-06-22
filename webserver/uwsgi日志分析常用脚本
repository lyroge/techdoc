uwsgi日志分析常用脚本
===================

1. **统计url访问量Top10**
*cat api.20160614.log | awk '{print $18}'| sort | uniq -c | sort -nr | head -n 10*

2. **统计ip访问量Top10**
*cat api.20160614.log | awk '{print $5}'| sort | uniq -c | sort -nr | head -n 10*
  
3. **统计响应耗时Top10**
*cat api.20160614.log | awk '{print $18, $24}' | sort -nr -k2 | head -n 20*
