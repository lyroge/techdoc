### 在尝试中文搜索时，我们创建如下demo例子： 


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
                        }
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




### 在尝试中文及pinyin搜索时，我们创建如下demo例子： 


可以针对如下情况搜索：

    分词及单个单词的搜索查询

        如：摄影、 摄 影 应该都可以查询到的

        如：sheying、she ying同样也可以搜索到

    这样我们就需要把搜索和索引统一转换为pinyin格式


创建索引：

    curl -XPUT 'http://localhost:9200/demo/'


索引结构：

    curl -XPUT 'http://localhost:9200/demo/_mapping/pinyin' -d '{
        "pinyin": {
            "properties": {
                "msg": {
                    "type": "string",
                    "analyzer": "ik_pinyin",
                    "include_in_all": true,
                    "fields": {
                        "msg_raw": {
                            "type": "string",
                            "analyzer": "standard_pinyin"
                        }
                    }
                }
            }
        }
    }'


索引数据：

    curl -XPUT 'http://localhost:9200/demo/pinyin/23' -d '{ "msg" : "韩国泡菜对华出口重启 官方大办活动庆祝" }'

查看分词

    http://127.0.0.1:9200/demo/_analyze?text=韩国泡菜对华出口重启 官方大办活动庆祝&analyzer=standard_pinyin


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


拼音搜索几个词

    {
        "query": {
            "query_string": {
                "default_operator": "AND",
                "query": "msg.msg_raw:(han guo)"
            }
        },
        "highlight": {
            "fields": {
                "msg": {
                    "type": "plain"
                }
            }
        }
    }


搜索试用情况：比如搜索"摄影"相关
    
    1. 摄影           ik
    2. 摄    影       standard
    3. sheying        
    4. she ying       ik_pinyin
    5. she ying       ik_standard_pinyin


应该均可以匹配相关内容

    index:  
      analysis:         
        filter:
          whitespace_remove:
            type: pattern_replace
            pattern: " "
            replacement: ""
        analyzer:        
          ik:  
              alias: [ik_analyzer]
              type: ik
          ik_max_word:  
              type: ik  
              use_smart: false  
          ik_smart:  
              type: ik  
              use_smart: true  
          ik_pinyin:
              type: custom
              tokenizer: ik
              filter: [pinyin, whitespace_remove, lowercase, trim]
          standard_pinyin:
              type: custom
              filter: [pinyin, lowercase, trim]
              tokenizer: standard

相似内容推荐

    {
      "query": {
        "more_like_this": {
          "fields": [
            "msg"
          ],
          "like_text": "菜",
          "min_term_freq": 1,
          "min_doc_freq": 1,
          "max_query_terms": 12
        }
      }
    }
