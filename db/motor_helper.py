import asyncio
from logger.log import storage
from motor.motor_asyncio import AsyncIOMotorClient
from bson import SON
import pprint

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

except ImportError:
    pass

# 数据库基本信息
db_configs = {
    'type': 'mongo',
    'host': '192.168.33.11',
    'port': '27017',
    'user': '',
    'password': '',
    'db_name': 'spider_data'
}

class MotorBase(object):
    def __init__(self):
        self.__dict__.update(**db_configs)
        if self.user:
            self.motor_uri = f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource={self.user}'
        else:
            self.motor_uri = f'mongodb://{self.host}:{self.port}/{self.db_name}'
        self.client = AsyncIOMotorClient(self.motor_uri)
        self.db = self.client.spider_data

    async def save_data(self,item):
        try:
            await self.db.infoq_details.update_one(
                {'uuid': item.get("uuid")},
                {'$set': item},
                upsert=True)
        except Exception as e:
            storage.error(f'数据插入出错:{e.args},此时的item是{item}')

    async def change_status(self,uuid,item,status_code=0):
        """
        status_code 0:初始 1:开始下载 2:下载完成
        """
        try:
            item['status'] = status_code
            await self.db.infoq_seed.update_one({'uuid': uuid}, {'$set': item}, upsert=True)
        except Exception as e:
            if 'immutable' in e.args[0]:
                await self.db.infoq_seed.delete_one({'_id':item['_id']})
                storage.info(f'数据重复删除:{e.args},此时的数据是:{item}')
            else:
                storage.error(f'修改状态出错:{e.args},此时的数据是:{item}')

    async def reset_status(self):
        """
        状态重设
        """
        await self.db.infoq_seed.update_many({'status': 1},{'$set':{'status': 0}})

    async def reset_all_status(self):
        """
        重设所有状态
        """
        await self.db.infoq_seed.update_many({},{'$set': {"status": 0}})

    async def get_detail_datas(self):
        data = self.db.infoq_seed.find({'status': 1})

        async for item in data:
            print(item)
        return data

    async def use_count_command(self):
        response = await self.db.command(SON([("count", "infoq_seed")]))
        print(f'response:{pprint.pformat(response)}')

if __name__ == '__main__':
    client = MotorBase()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.get_detail_datas())