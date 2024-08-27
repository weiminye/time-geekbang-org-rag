import json

class 元数据:
    def __init__(self):
        self.标题 = None
        self.作者 = None
        self.创建日期 = None
        self.url = None

    def set_标题(self, 标题):
        self.标题 = 标题

    def set_作者(self, 作者):
        self.作者 = 作者

    def set_创建日期(self, 创建日期):
        self.创建日期 = 创建日期

    def set_url(self, url):
        self.url = url

class 元数据Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, 元数据):
            return {"标题": obj.标题, "作者": obj.作者, "创建日期": obj.创建日期, "url": obj.url}
        return super().default(obj)