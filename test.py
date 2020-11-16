import httplib,os
test_data_urlencode = os.environ["cwm_data"]

requrl = "https://app.hbooker.com/reader/get_task_bonus_with_sign_recommend"
headerdata = {"Content-Type":"application/x-www-form-urlencoded","User-Agent":"Android  com.kuangxiangciweimao.novel  2.6.020,vivo, vivo X6D, 22, 5.1"}

conn = httplib.HTTPConnection("app.hbooker.com")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()

print res