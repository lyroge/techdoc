
在尝试demo时我们创建如下例子： 

可以针对如下情况搜索：

    分词及单个单词的搜索查询
    
    如：摄影、 摄 影 应该都可以查询到的


创建索引：

    curl -XPUT 'http://localhost:9200/demo/'


索引结构：

    curl -XPUT 'http://localhost:9200/demo/_mapping/pinyin' -d '{
        "pinyin": {
            "properties": {
                "msg": {
                    "type": "string",
                    "analyzer": "ik",
                    "include_in_all": true,
                    "fields": {
                        "msg_raw": {
                            "type": "string",
                            "analyzer": "standard"
                        },
                        "msg_pinyin": ""
                    }
                }
            }
        }
    }'


索引数据：

    curl -XPUT 'http://localhost:9200/demo/pinyin/23' -d '{ "msg" : "韩国泡菜对华出口重启 官方大办活动庆祝" }'


索引查询

    {
        "query": {
            "query_string": {
                "default_operator": "AND",
                "query": "msg.msg_raw:大启 OR msg:大启"
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
