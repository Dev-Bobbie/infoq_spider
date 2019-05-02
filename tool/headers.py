from collections.abc import Mapping
from pprint import pprint

#请求头的抽象类
class Headers(dict):
    def __init__(self,seq=None):
        super().__init__()
        if seq:
            self.update(seq)

    def __getitem__(self, key):
        return dict.__getitem__(self, self.normkey(key))

    def __setitem__(self, key, value):
        dict.__setitem__(self, self.normkey(key), self.normvalue(value))

    def get(self, key, def_val=None):
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    def setdefault(self, key, def_val=None):
        return dict.setdefault(self, self.normkey(key), self.normvalue(def_val))

    def update(self, seq):
        seq = seq.items() if isinstance(seq, Mapping) else seq
        iseq = ((self.normkey(k), self.normvalue(v)) for k, v in seq)
        super().update(iseq)


    def normkey(self,key):
        return key.lower()

    def normvalue(self,value):
        return value

    def pop(self, key,*args):
        return dict.pop(self,self.normkey(key),*args)

    def __contains__(self, key):
        return dict.__contains__(self,self.normkey(key))


# 一个标准简单 请求头实现类
class SimpleHeaders(Headers):
    def __init__(self, seq=None):
        seq = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "connection": "keep-alive",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)'
        }

        super().__init__(seq)

if __name__ == '__main__':
    s = SimpleHeaders()
    header = (dict(s))
    pprint(header)
