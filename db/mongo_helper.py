import pymongo
from logger.log import storage
from motor.motor_asyncio import AsyncIOMotorClient

# 数据库基本信息
db_configs = {
    'type': 'mongo',
    'host': '192.168.33.11',
    'port': '27017',
    'user': '',
    'password': '',
    'db_name': 'spider_data'
}


class Mongo(object):
    def __init__(self):
        """
        初始化数据库基本信息
        """
        self.db_name = db_configs.get('db_name')
        self.host = db_configs.get('host','127.0.0.1')
        self.port = db_configs.get('port')
        self.client = pymongo.MongoClient(f'mongodb://{self.host}:{self.port}')
        self.username = db_configs.get('username')
        self.password = db_configs.get('password')
        if self.username and self.password:
            self.db = self.client[self.db_name].authenticate(self.username,self.password)
        self.db = self.client[self.db_name]

    def find_data(self,col='infoq_seed'):
        """
        获取状态为0的数据
        """
        data = self.db[col].find({'status':0})
        gen = (item for item in data)
        return gen

    def change_status(self,uuid,item,col='infoq_seed',status_code=0):
        """
         status_code 0:初始 1:开始下载 2:下载完成
        """
        item['status'] = status_code
        self.db[col].update_one({'uuid':uuid},{'$set':item})

    def save_data(self,items,col='infoq_seed'):
        if isinstance(items,list):
            for item in items:
                try:
                    self.db[col].update_one(
                        {
                        'uuid': item.get("uuid")},
                        {'$set': item},
                        upsert=True)
                except Exception as e:
                    storage.error(f'数据插入出错:{e.args},此时的item是:{item}')
        else:
            try:
                self.db[col].update_one({
                    'uuid': items.get("uuid")},
                    {'$set': items},
                    upsert=True)
            except Exception as e:
                storage.error(f"数据插入出错:{e.args},此时的item是:{items}")

if __name__ == '__main__':
    client = Mongo()
    for _ in client.find_data():
        print(_)
