from django.db import migrations, models
from django.db import transaction

销售入账记录_data = [
    {'id': 1, '客户': '广州神机妙算有限公司', '入账日期': '2024-07-06', '入账金额': 9527, '已到账款项': 57980, '剩余到账款项': 2908},
    {'id': 2, '客户': '北京测试数据有限公司', '入账日期': '2024-06-01', '入账金额': 996, '已到账款项': 7653, '剩余到账款项': 2521},
    {'id': 3, '客户': '宇宙洪荒测试公司', '入账日期': '2024-04-05', '入账金额': 251, '已到账款项': 8960, '剩余到账款项': 22463},
]

 
def initial_data(apps, schema_editor):
    model = apps.get_model("home", "销售入账记录")
    db_alias = schema_editor.connection.alias

    with transaction.atomic():
        for data in 销售入账记录_data:
            model .objects.using(db_alias).create(**data)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='销售入账记录',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('客户', models.CharField(max_length=255)),
                ('入账日期', models.DateTimeField()),
                ('入账金额', models.TextField(null=True)),
                ('已到账款项', models.IntegerField(null=True)),
                ('剩余到账款项', models.IntegerField(null=True)),
            ],
        ),
        migrations.RunPython(initial_data), #添加这一行
    ]
