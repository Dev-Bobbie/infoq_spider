headers = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
content-length: 2241
content-type: application/x-www-form-urlencoded
cookie: ASP.NET_SessionId=rnpemlbnv0mgy2dnppik35ek; FirstVisit=2019/4/3 10:27:34; _uab_collina=155425845464800163441555; comefrom=https://www.cmd5.com/?md5_str=5d41402abc4b2a76b9719d911017c592&button=md5%d4%da%cf%df+%bc%d3%c3%dc/%bd%e2%c3%dc; Hm_lvt_0b7ba6c81309fff7ce4498ec7b107c0b=1554264312,1554264635,1554264956,1554266675; Hm_lpvt_0b7ba6c81309fff7ce4498ec7b107c0b=1554267787
origin: https://www.cmd5.com
referer: https://www.cmd5.com/
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
"""

hs = headers.split('\n')
b = [k for k in hs if len(k)]
e = b
f = {(i.split(":")[0], i.split(":", 1)[1].strip()) for i in e}
g = sorted(f)
index = 0
print("{")
for k, v in g:
    print(repr(k).replace('\'','"'), repr(v).replace('\'','"'), sep=':', end=",\n")
print("}")
