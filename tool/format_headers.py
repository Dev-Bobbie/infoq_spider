headers = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BIDUPSID=9401EF4C8B5165B65D133B8A9F93DF6D; BAIDUID=1DB5FBCD3A30AEE43CD9C933044789F4:FG=1; PSTM=1553177180; BD_UPN=123253; BDUSS=dNLVcwazY2ak01Z3ZXNkxxZ1o3S0JUa3JKcXVvejlyUkNsbnV4Wmtnak4tTDljQVFBQUFBJCQAAAAAAAAAAAEAAAAH3PcqYTE1MzI0NzYwNWxvdmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM1rmFzNa5hcRz; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; delPer=0; BD_CK_SAM=1; PSINO=5; locale=zh; BDRCVFR[pNjdDcNFITf]=mk3SLVN4HKm; H_PS_645EC=0171KvQilPnZeDdfzTx1%2BfcuPJaY4s%2BjqNmj6crBNTUU6uCocmuCImOXzcRJh812QVsKHw; BD_HOME=1; H_PS_PSSID=28882_1435_28804_21111_28771_28721_28964_28837_28584_28890
Host: www.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
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
