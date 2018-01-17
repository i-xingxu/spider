#coding=utf-8
import urllib.request
import urllib.parse

class UrlReqest():

    def url_open(self,url):
        '''
        请求url
        :param url: url地址
        :return:
        '''
        try:
            req=urllib.request.urlopen(url)
            self.data=req.read().decode("utf-8")
            self.code=req.detail()
            return req
        except Exception as e:
            print(e)

    def url_parse(self,url,urldata):
        '''
        post参数
        :param url: url地址
        :param urldata: 参数
        :return:
        '''

        try:
            urldata=urllib.parse.urlencode(urldata)
            urldata=urldata.encode("utf-8")
            _url=urllib.request.Request(url,urldata)
            return _url
        except Exception as e:
            print(e)