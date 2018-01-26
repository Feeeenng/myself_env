# -*- coding: UTF-8 -*-
'''
__title__ = 'test_1.py'
__author__ = 'FenG'
__mtime__ = '2018/1/25 17:46'
'''
from __future__ import unicode_literals

import requests,json


class TableauApi(object):

    def __init__(self):
        self.http = ''
        self.version = ''
        self.name = ''
        self.password = ''
        self.url = 'http://{0}/api/{1}'.format(self.http,self.version)
        self.headers =  {
              'accept': 'application/json',
              'content-type': 'application/json'
            }
        self.site_id = ''
        self.login()

    def req(self,path,info=None):
        urlpath = self.url + path
        s = requests.session()
        info = json.dumps(info)
        return s.post(urlpath,info,headers=self.headers)

    def req_get(self,path):
        urlpath = self.url+ path
        s = requests.session()
        return s.get(urlpath,headers=self.headers)

    def login(self):
        '''
        认证API
        :return:
        '''
        data ={
          "credentials": {
            "name": self.name,
            "password": self.password,
            "site": {
              "contentUrl": ''
            }
          }
        }
        ret_info = self.req('/auth/signin',data).json()
        self.headers['X-Tableau-Auth'] = ret_info['credentials']['token']
        self.site_id = ret_info['credentials']['site']['id']
        return self.headers

    def query_project(self,pageNumber=None):
        '''
        Query Projects
        doc :
        https://onlinehelp.tableau.com/current/api/rest_api/en-us/help.htm#REST/rest_api_ref.htm#Query_Projects%3FTocPath%3DAPI%2520Reference%7C_____64
        :param pageNumber:
        :return:
        '''
        urlpath = '/sites/{0}/projects'.format(self.site_id)
        if pageNumber:
            urlpath = urlpath+'?pageNumber={0}'.format(pageNumber)

        data = self.req_get(urlpath).json()
        data = self.__json_to_data(data)
        return data

    def query_workbook(self,workbook_id=None):
        '''
        Query Workbook
        doc :
        https://onlinehelp.tableau.com/current/api/rest_api/en-us/help.htm#REST/rest_api_ref.htm#Query_Workbook%3FTocPath%3DAPI%2520Reference%7C_____77
        :param workbook_id:
        :return:
        '''
        urlpath = '/sites/{0}/workbooks/{1}'.format(self.site_id,workbook_id)
        data = self.req_get(urlpath).json()
        data = self.__json_to_data(data)
        return  data

    def query_workbook_views(self,workbook_id=None):
        '''
        Query workbook_views
        doc :
        https://onlinehelp.tableau.com/current/api/rest_api/en-us/help.htm#REST/rest_api_ref.htm#Query_Views_for_Workbook%3FTocPath%3DAPI%2520Reference%7C_____76
        :param workbook_id:
        :return:
        '''

        urlpath = '/sites/{0}/workbooks/{1}/views'.format(self.site_id,workbook_id)
        data = self.req_get(urlpath).json()
        data = self.__json_to_data(data)
        return data


    def __json_to_data(self,data):
        return json.dumps(data,indent=4)


