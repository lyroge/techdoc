针对es中的分词我们可以利用ik插件，针对拼音的搜索我们可以用pinyin插件

在尝试demo时我们创建如下例子：
curl -XPUT 'http://localhost:9200/demo/'

curl -XPUT 'http://localhost:9200/demo/_mapping/pinyin' -d '
{
    "pinyin" : {
        "properties" : {
            "msg" : {"type" : "string", "analyzer":"ik", "include_in_all":true, "fields":  {"msg_raw" :{"type" : "string", "analyzer": "standard"}, "msg_pinyin":""} }
        }
    }
}'

curl -XPUT 'http://localhost:9200/demo/pinyin/23' -d '{
        "msg" : "韩国泡菜对华出口重启 官方大办活动庆祝"
}'

构建了针对ik分词及standard分词的2个标题，分别对应分词匹配及模糊的单词匹配

上面的过程没有问题，当我们通过拼音搜索时，我们需要设置一些策略


其实在考虑拼音搜索时，我们是否有必要存储纯粹的中文字段

因为通过拼音处理时，我们全部会转成拼音数据

于是进行了如下尝试：
进行分词时出现问题，目前搁置等待作者回复


{
  "query": {
    "query_string": {
      "default_operator": "AND",
      "query": "msg.msg_raw:大启  OR msg:大启"
    }
  },
  "highlight": {
    "fields": {
      "msg.msg_raw": {
        "type": "plain"
      }
    }
  }
}












