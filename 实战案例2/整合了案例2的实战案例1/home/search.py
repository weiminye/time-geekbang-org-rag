from .models import CNET新闻, 销售入账记录

def 查询(查询参数):
    if '模块' in 查询参数:
        if 查询参数['模块'] == 1: #'销售对账'
            if '客户名称' in 查询参数:
                客户 = 查询参数['客户名称'].strip()
                return 销售入账记录.objects.filter(客户__icontains=客户)
        if 查询参数['模块'] == 6: #'CNET新闻'
            if '日期' in 查询参数:
                日期 = 查询参数['日期'].strip()
                print(f'日期={日期}')
                return CNET新闻.objects.filter(新闻发布日期__date=日期).values('标题中文翻译')