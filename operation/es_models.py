import math
from elasticsearch import Elasticsearch
from django.conf import settings


class EsModules:
    def __init__(self) -> None:
        self.es = Elasticsearch(
            cloud_id=settings.ELASTICSEARCH["default"]["cloud_id"],
            http_auth=settings.ELASTICSEARCH["default"]["http_auth"],
            timeout=300,
            max_retries=10,
            retry_on_timeout=True,
        )
        self.search_index = settings.ELASTICSEARCH["default"]["index"]
        self.log_index = settings.ELASTICSEARCH["default"]["log_index"]
        # search values
        self.GONDOR_BOOST = settings.ELASTICSEARCH["default"]["GONDOR_BOOST"]
        self.MALLORN_DEPTH1_BOOST = settings.ELASTICSEARCH["default"][
            "MALLORN_DEPTH1_BOOST"
        ]
        self.MALLORN_DEPTH2_BOOST = settings.ELASTICSEARCH["default"][
            "MALLORN_DEPTH2_BOOST"
        ]

    def recent_log(self, page=0):
        if page > 0:
            page -= 1
        page *= 100
        query = {
            "query": {
                "bool": {
                    "must_not": [{"term": {"priming": True}}],
                    "must": [{"term": {"insertBrandId": ""}}],
                }
            },
            "size": 100,
            "from": page,
            "_source": {"excludes": ["t800", "mallorn"]},
            "sort": [{"@timestamp": {"order": "desc"}}],
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_mgId_set(self, last_mgId=""):
        if last_mgId:
            query = {
                "size": 0,
                "query": {
                    "bool": {
                        "must_not": [{"term": {"priming": True}}],
                        "must": [{"term": {"insertBrandId": ""}}],
                    }
                },
                "aggs": {
                    "unique_mgId": {
                        "composite": {
                            "sources": [
                                {"mgId": {"terms": {"field": "mgId", "order": "desc"}}}
                            ],
                            "size": 30,
                            "after": {"mgId": last_mgId},  # 이전 페이지의 마지막 mgId 값 입력
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {"includes": ["_id"], "excludes": []},
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        else:
            query = {
                "size": 0,
                "query": {
                    "bool": {
                        "must_not": [{"term": {"priming": True}}],
                        "must": [{"term": {"insertBrandId": ""}}],
                    }
                },
                "aggs": {
                    "unique_mgId": {
                        "composite": {
                            "sources": [
                                {"mgId": {"terms": {"field": "mgId", "order": "desc"}}}
                            ],
                            "size": 30,
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {"includes": ["_id"], "excludes": []},
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        result = self.es.search(index=self.search_index, body=query)

        return result

    def get_mgId(self, mgId, page=0):
        if page > 0:
            page = page - 1
        page = page * 9
        query = {
            "size": 9,  # // 가져올 문서의 개수를 5로 설정
            "from": page,  # // 시작 인덱스를 20으로 설정
            "query": {"bool": {"must": {"term": {"mgId": mgId}}}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_shire(self, shire, page=0):
        size = 30
        if page > 0:
            page -= 1
        page = page * size
        query = {
            "size": size,
            "from": page,
            "query": {
                "bool": {
                    "must": [
                        {"term": {"insertBrandId": ""}},
                        {"term": {"shire": shire}},
                    ],
                    "must_not": [{"term": {"priming": True}}],
                }
            },
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_category(self):
        query = {
            "aggs": {"shire_terms": {"terms": {"field": "shire", "size": 10}}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        aggregations = result.get("aggregations", {})
        shire_terms = aggregations.get("shire_terms", {})
        buckets = shire_terms.get("buckets", [])
        return buckets

    def get_userId(self, userId, page=0):
        size = 30
        if page > 0:
            page -= 1
        page = page * size
        query = {
            "size": size,  # // 가져올 문서의 개수를 5로 설정
            "from": page,  # // 시작 인덱스를 20으로 설정
            "query": {"bool": {"must": {"term": {"userId": userId}}}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_mgId(self, mgId, page=0):
        if page > 0:
            page = page - 1
        page = page * 9
        query = {
            "size": 9,  # // 가져올 문서의 개수를 5로 설정
            "from": page,  # // 시작 인덱스를 20으로 설정
            "query": {"bool": {"must": {"term": {"mgId": mgId}}}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_userId(self, userId, page=0):
        size = 30
        if page > 0:
            page -= 1
        page = page * size
        query = {
            "size": size,  # // 가져올 문서의 개수를 5로 설정
            "from": page,  # // 시작 인덱스를 20으로 설정
            "query": {"bool": {"must": {"term": {"userId": userId}}}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_key_log(self, key):
        query = {"query": {"match": {"_id": key}}}
        result = self.es.search(index=self.log_index, body=query)
        return result

    def get_latest_log(self):
        query = {
            "query": {"match_all": {}},
            "size": "40",
            "sort": [{"@timestamp": {"order": "desc"}}],
            "_source": {"includes": ["_id"], "excludes": []},
        }
        result = self.es.search(index=self.log_index, body=query)

        return result

    def get_priming(self, page=0):
        if page > 0:
            page -= 1
        page *= 100
        query = {
            "size": 100,
            "from": page,
            "query": {"bool": {"must": [{"term": {"priming": True}}]}},
            "_source": {"excludes": ["t800", "mallorn"]},
        }
        result = self.es.search(index=self.search_index, body=query)
        return result

    def get_priming_mgId_set(self, last_mgId=""):
        if last_mgId:
            query = {
                "size": 0,
                "query": {"bool": {"must": [{"term": {"priming": True}}]}},
                "aggs": {
                    "unique_mgId": {
                        "composite": {
                            "sources": [
                                {"mgId": {"terms": {"field": "mgId", "order": "desc"}}}
                            ],
                            "size": 60,
                            "after": {"mgId": last_mgId},  # 이전 페이지의 마지막 mgId 값 입력
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {"includes": ["_id"], "excludes": []},
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        else:
            query = {
                "size": 0,
                "query": {"bool": {"must": [{"term": {"priming": True}}]}},
                "aggs": {
                    "unique_mgId": {
                        "composite": {
                            "sources": [
                                {"mgId": {"terms": {"field": "mgId", "order": "desc"}}}
                            ],
                            "size": 60,
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {"includes": ["_id"], "excludes": []},
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        result = self.es.search(index=self.search_index, body=query)

        return result

    def get_productId_set(self, last_productId=""):
        if last_productId:
            query = {
                "size": 0,
                "query": {"bool": {"must_not": [{"term": {"insertBrandId": ""}}]}},
                "aggs": {
                    "unique_insertProductId": {
                        "composite": {
                            "sources": [
                                {
                                    "insertProductId": {
                                        "terms": {
                                            "field": "insertProductId",
                                            "order": "desc",
                                        }
                                    }
                                }
                            ],
                            "size": 60,
                            "after": {
                                "insertProductId": last_productId
                            },  # 이전 페이지의 마지막 mgId 값 입력
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {
                                        "includes": ["_id", "insertBrandId"],
                                        "excludes": [],
                                    },
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        else:
            query = {
                "size": 0,
                "query": {"bool": {"must_not": [{"term": {"insertBrandId": ""}}]}},
                "aggs": {
                    "unique_insertProductId": {
                        "composite": {
                            "sources": [
                                {
                                    "insertProductId": {
                                        "terms": {
                                            "field": "insertProductId",
                                            "order": "desc",
                                        }
                                    }
                                }
                            ],
                            "size": 60,
                        },
                        "aggs": {
                            "unique_id": {
                                "top_hits": {
                                    "size": 1,
                                    "sort": [{"@timestamp": "asc"}],
                                    "_source": {
                                        "includes": ["_id", "insertBrandId"],
                                        "excludes": [],
                                    },
                                }
                            }
                        },
                    }
                },
                "from": 0,
            }
        result = self.es.search(index=self.search_index, body=query)

        return result

    def get_new_mgid(self, page_size, page):
        query = {
            "query": {
                "bool": {
                    "must": [{"match_all": {}}],
                    "must_not": [{"exists": {"field": "search-results"}}],
                    "filter": [{"term": {"query-analysis-result.insertProductId": ""}}],
                }
            }
        }

        result = self.es.count(index=self.log_index, body=query)
        total_count = result["count"]

        if page < 1:
            page = 1
        elif page > total_count // page_size + 1:
            page = total_count // page_size + 1

        start = (page - 1) * page_size

        query = {
            "query": {
                "bool": {
                    "must": [{"match_all": {}}],
                    "must_not": {"exists": {"field": "search-results"}},
                    "filter": [{"term": {"query-analysis-result.insertProductId": ""}}],
                }
            },
            "sort": [{"@timestamp": {"order": "desc"}}],
            "from": start,  # 시작 위치 설정
            "size": page_size,  # 페이지 크기 설정
            "_source": {
                "includes": [
                    "_id",
                    "@timestamp",
                    "userId",
                    "query-analysis-result.shire",
                    "query-analysis-result.mgId",
                ],
                "excludes": [],
            },
        }

        search_data = self.es.search(index=self.log_index, body=query)
        last_page = math.ceil(search_data["hits"]["total"]["value"] / page_size)
        all_results = search_data["hits"]["hits"]

        return page, last_page, all_results

    def embedding_query(
        self,
        type_,
        embedding,
        last_processed_timestamp,
        data_size,
        gondor="",
        geohash="",
        T800_MIN_SCORE=0,
        MALLORN_MIN_SCORE=0,
    ):
        query = {}
        if type_ == "t800":
            if gondor == "not_accurate" or gondor == "":
                should_query = {}
            else:
                should_query = {
                    "query": {
                        "bool": {
                            "should": [{"term": {"gondor": gondor}}],
                            "boost": self.GONDOR_BOOST,
                        }
                    },
                }
            query = {
                "size": data_size,
                "knn": {
                    "field": "t800",
                    "query_vector": embedding,
                    "k": data_size,
                    "num_candidates": data_size,
                    "filter": [
                        {"term": {"shire": "homegood"}},
                        {"term": {"query-analysis-result.insertProductId": ""}},
                        {"range": {"@timestamp": {"lt": last_processed_timestamp}}},
                    ],
                },
                "min_score": T800_MIN_SCORE,
                "_source": {
                    "excludes": ["t800", "mallorn"],
                },
            }
            query.update(should_query)
            return query

        elif type_ == "mallorn":
            if geohash != "xxxxxxxxxxxx":
                should_query = {
                    "query": {
                        "bool": {
                            "should": [
                                {
                                    "geo_distance": {
                                        "distance": "100m",
                                        "geohash": geohash,
                                        "boost": self.MALLORN_DEPTH1_BOOST,
                                    }
                                },
                                {
                                    "geo_distance": {
                                        "distance": "300m",
                                        "geohash": geohash,
                                        "boost": self.MALLORN_DEPTH2_BOOST,
                                    }
                                },
                            ]
                        }
                    }
                }
            else:
                should_query = {}

            query = {
                "size": data_size,
                "knn": {
                    "field": "mallorn",
                    "query_vector": embedding,
                    "k": data_size,
                    "num_candidates": data_size,
                    "filter": [
                        {"term": {"shire": "place"}},
                        {"term": {"query-analysis-result.insertProductId": ""}},
                        {"range": {"@timestamp": {"lt": last_processed_timestamp}}},
                    ],
                },
                "min_score": MALLORN_MIN_SCORE,
                "_source": {
                    "excludes": ["t800", "mallorn"],
                },
            }
            query.update(should_query)
            return query
        else:
            return query

    def search(self, query_body):
        res = self.es.search(index=self.search_index, body=query_body)
        return res
