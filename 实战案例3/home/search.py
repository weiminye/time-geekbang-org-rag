from .models import 销售入账记录

def 查询(查询参数):
    if '模块' in 查询参数:
        if 查询参数['模块'] == 1: #'销售对账'
            if '客户名称' in 查询参数:
                客户 = 查询参数['客户名称'].strip()
                return 销售入账记录.objects.filter(客户__icontains=客户)