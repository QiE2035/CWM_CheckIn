import httplib,os
test_data_urlencode = os.environ["cwm_data"]
print test_data_urlencode

requrl = "http://app.hbooker.com/task/get_sign_record"
headerdata = {"Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"gzip","User-Agent":"Android  com.kuangxiangciweimao.novel  2.6.020,vivo, vivo X6D, 22, 5.1","Connection":"Keep-Alive","Content-Length":152}

conn = httplib.HTTPConnection("app.hbooker.com")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()

print res
