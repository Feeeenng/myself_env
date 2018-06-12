# -*- coding: UTF-8 -*-
'''
__author__: 'FenG_Vnc'
__date__: 2018/6/12 14:08
__file__: rabbitmq_demo.py
'''
from __future__ import unicode_literals


import json
import pika

from config import config


class BaseAuth(object):
    def __init__(self):
        self.username = config.RABBITMQ_USER
        self.password = config.RABBITMQ_PASSWORD
        self.host = config.RABBITMQ_HOST
        self.v_host = config.RABBITMQ_V_HOST
        self.channel = self.login()
    def login(self):
        credentials = pika.PlainCredentials(self.username,self.password)
        connection =  pika.BlockingConnection(
            pika.ConnectionParameters(self.host,credentials=credentials,virtual_host=self.v_host))
        return  connection.channel()

class RabbitmqProducer(BaseAuth):

    def __init__(self):
        self.queue = "xxxxxxxxxxx"  # 声明队列
        self.exchange = "xxxxxxxxxxx"      # 交换机
        self.routing_key = "xxxxxxxxxxx"  #路由键
        self.body = 'aaaaaaaaaa'   # 发送的消息
        super(RabbitmqProducer, self).__init__()

    def base_producer(self):
        '''
        发布/订阅系统  生产者
        :return:
        '''
        self.channel.queue_declare(queue = self.queue)
        self.channel.basic_publish(
            exchange = self.exchange,
            routing_key = self.routing_key,
            body = self.body
        )
        print "发送消息: %s",self.body

class RabbitmqCunsumer(BaseAuth):
    def __init__(self):
        self.queue = "xxxxxxxxxxx"  # 声明同样的队列
        super(RabbitmqCunsumer, self).__init__()

    def callback(self,channl,method,properties,body):
        print "接到消息: %s",body
        data = json.loads(body)
        print(type(body))

    def base_cumsumber(self):
        '''
        发布/订阅系统  消费者
        :return:
        '''
        self.channel.basic_consume(self.callback,   # 调用回调函数
                                   queue=self.queue,   # 指定队列

                                   no_ack = True   #取完一条消息后，不给生产者发送确认消息，默认是False的，即  默认给rabbitmq发送一个收到消息的确认，一般默认即可
                                   )
        self.channel.start_consuming()
if __name__ == '__main__':
    while 1:
        produc_s = RabbitmqProducer()
        cunsumber = RabbitmqCunsumer()
        produc_s.base_producer()
        cunsumber.base_cumsumber()

