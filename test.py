import httplib,os
test_data_urlencode = os.environ["sf_data"]
print test_data_urlencode
#'account=%E4%B9%A6%E5%AE%A260435783759&device_token=ciweimao_00%3A08%3Ac7%3Aa9%3Ac4%3A5f&app_version=2.6.020&login_token=469eaf7eb4ad9b5d1b7a308442f25272'

requrl = "http://app.hbooker.com/task/get_sign_record"
headerdata = {"Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"gzip","User-Agent":"Android  com.kuangxiangciweimao.novel  2.6.020,vivo, vivo X6D, 22, 5.1","Connection":"Keep-Alive","Content-Length":152}

conn = httplib.HTTPConnection("app.hbooker.com")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()

print res