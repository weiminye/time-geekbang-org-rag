from .models import 销售入账记录
from .api import 调用向量编码服务

def 查询(查询参数):
    if '模块' in 查询参数:
        if 查询参数['模块'] == 1: #'销售对账'
            if '客户名称' in 查询参数:
                客户 = 查询参数['客户名称'].strip()
                精确搜索结果 = 销售入账记录.objects.filter(客户=客户).values('客户', '入账日期', '入账金额', '已到账款项', '剩余到账款项')
                if 精确搜索结果 is not None and len(精确搜索结果) > 0:
                    return 精确搜索结果
                else:
                    查询字符串向量编码 = 调用向量编码服务(客户)
                    模糊搜索结果RawQuerySet = 销售入账记录.objects.raw('SELECT *, 1 - (客户向量编码 <=> %s) AS 余弦相似度,客户 FROM public."home_销售入账记录" order by 余弦相似度 desc;',[str(查询字符串向量编码),])

                    模糊搜索结果 = []
                    for item in 模糊搜索结果RawQuerySet:
                        模糊搜索结果.append({
                            '客户': item.客户,
                            '入账日期': str(item.入账日期),
                            '入账金额': item.入账金额,
                            '已到账款项': item.已到账款项,
                            '剩余到账款项': item.剩余到账款项
                        })
                    return 模糊搜索结果