# -*- coding: UTF-8 -*-
'''
__title__ = 'test_requests.py'
__author__ = 'FenG'
__mtime__ = '2017/11/20 14:21'
'''
from __future__ import unicode_literals

import json
import os

from elasticsearch import Elasticsearch
from sshtunnel import SSHTunnelForwarder

SSH_IP = os.environ.get('SSH_IP','localhost')
SSH_PWD = os.environ.get('SSH_PWD','123456')



if __name__ == '__main__':

    with SSHTunnelForwarder(
            (SSH_IP, 22),  # B机器的配置
            ssh_password=SSH_PWD,
            ssh_username="root",
            remote_bind_address=("10.27.157.14", 9200)) as server:
        es = Elasticsearch(hosts='127.0.0.1',port=server.local_bind_port)
        data = es.search(
            index='index',
            doc_type='test',
            body={
                'query':{
                    'match_all':{}
                }
            }
        )
        print json.dumps(data,indent=4)


