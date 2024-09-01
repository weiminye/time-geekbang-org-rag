
import subprocess


def 生成每日简报(今天的新闻list:list):
    print("生成每日简报")

    # 获取当前日期和时间
    now = datetime.now()

    # 将其格式化为字符串，例如 "2023-04-05_14-30-00"
    formatted_date = now.strftime("%Y-%m-%d")

    # 使用日期字符串作为文件名
    每日简报文件 = f"{formatted_date}.CNET每日简报.html"

    with open(每日简报文件, 'w', encoding='utf-8') as f:
        f.write('''<html>
    <head>
        <title>CNET每日简报</title>
        <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <link
      href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.6.2/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link href="https://cdn.bootcdn.net/ajax/libs/bootstrap-icons/1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.6.2/js/bootstrap.bundle.min.js"></script>
    </head>
<body>

                ''')
        f.write(f"<h1>CNET每日简报-{formatted_date}</h1>")
        f.write('<div class="container" id="main_div">')
        for current in 今天的新闻list:
            f.write('''
<div class="row">
            <div class="accordion" id="accordionExample">
                <div class="card">
                <div class="card-header" id="headingOne">
                    <h2 class="mb-0">
                    <button class="btn btn-link text-left" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne"><p><h3>
                    ''')
            f.write(current.元数据.标题_中文翻译)
            f.write("</h3></p><p>")
            f.write(current.摘要)
            f.write('''
 </p>
                    </button>
                    </h2>
                </div>
                <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                    <div class="card-body"><p>
                    ''')
            f.write(current.新闻内容_中文翻译)
            f.write('''
</p
<p><a href="
''')
            f.write(current.元数据.url)
            f.write('''
" target="_blank">阅读原文</a></p>
                    </div>
                </div>
            </div>
        </div>
''')
        f.write("</ul>")
        f.write("</div></body></html>")

    return 每日简报文件
def 打开每日简报(每日简报文件):
    # 使用默认的应用程序打开HTML文件
    subprocess.run(['start', 每日简报文件], shell=True, check=True)
