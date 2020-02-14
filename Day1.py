# -*- coding: utf-8 -*- 
#--帅淼出品--质量保证--
import requests
import unittest
import re
class Text_sx(unittest.TestCase):
    def setUp(self):
        self.head={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'http://192.168.1.35/fsmarket/user.php',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ECS[username]=liumiao; ECS_ID=47d5f4f5cba7498fd73ae9980394697a95ab6780; ECS[visit_times]=10; Hm_lvt_090f45997b7b0cf2271bce729f4c9349=1581395046,1581395619,1581395634,1581396008; ECS[user_id]=258; ECS[password]=a3bf75e49a8a4727d9f2773338bc38b2; Hm_lpvt_090f45997b7b0cf2271bce729f4c9349=1581396067'
        }
        self.body = {
            'username':'liumiao',
            'password':'123456',
            'remember':'1',
            'login_type':'0',
            'act':'act_login',
            'back_act':'http://192.168.1.35/fsmarket/',
            'submit':'登录'
        }

        self.url = 'http://192.168.1.35/fsmarket/user.php'
    def test_denglu(self):
        res = requests.post(url=self.url,data=self.body,headers=self.head)
        re_dy = re.search('<span class="name">(.*?)</span><i class=',res.text)
        print(re_dy.group(1))
        relust = re_dy.group(1)
        self.assertIn('liumiao', str(relust))

# '''
# HTTP/1.1 200 OK
# Date: Tue, 11 Feb 2020 04:27:34 GMT
# Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16
# X-Powered-By: PHP/5.4.16
# Set-Cookie: ECS_ID=68ff0c496e8792e5b464951e8dfa83d51fc21964; path=/
# Cache-control: private
# Set-Cookie: ECS[visit_times]=1; expires=Tue, 09-Feb-2021 20:27:35 GMT; path=/
# Set-Cookie: ECS[username]=liumiao; expires=Wed, 26-Feb-2020 04:27:35 GMT; path=/
# Set-Cookie: ECS[user_id]=258; expires=Wed, 26-Feb-2020 04:27:35 GMT; path=/
# Set-Cookie: ECS[password]=a3bf75e49a8a4727d9f2773338bc38b2; expires=Wed, 26-Feb-2020 04:27:35 GMT; path=/
# Keep-Alive: timeout=5, max=100
# Connection: Keep-Alive
# Content-Type: text/html; charset=utf-8
# Content-Length: 55343
# '''
# head={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#     'Referer': 'http://192.168.1.35/fsmarket/user.php',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'ECS[display]=grid; ECS[history]=100; ECS[username]=liumiao; ECS[user_id]=258; ECS[password]=a3bf75e49a8a4727d9f2773338bc38b2; ECS_ID=982f0aed9876df08f2eadd5d042959b705aea6aa; ECS[visit_times]=13; Hm_lvt_090f45997b7b0cf2271bce729f4c9349=1581395634,1581396008,1581407551,1581409276; Hm_lpvt_090f45997b7b0cf2271bce729f4c9349=1581409417'
# }
# body = {
#     'step':'payinfo',
#     'order_id':'227'
# }
# url = 'http://192.168.1.35/fsmarket/flow.php?step=checkout'
# res = requests.post(url=url,headers=head,data=body)
# with open('1.html','wb') as f:
#     f.write(res.content)