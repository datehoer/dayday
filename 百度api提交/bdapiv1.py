import requests
import re
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36,',
    'Host': 'data.zz.baidu.com',
    'Content-Length':'83'
}
print("*"*30)
print('links.txt示例:\nhttps://xxxxx.html\nhttps://xxxxx.html\nhttps://xxxxx.html\nhttps://xxxxx.html')
print("*"*30)
print('api示例:\nhttp://data.zz.baidu.com/urls?site=xxxxxxxxxxx')
push_num = 1
while push_num < 9999:
    if push_num == 1:
        answer = input("请问你是否已经将链接填入links.txt，api填入api.txt中呢，如果是则回答1\n")
    if answer == '1':
        try:
            with open('links.txt', 'r') as links:
                links = links.read()
        except FileNotFoundError:
            print("links.txt文件不存在")
        try:
            with open('api.txt', 'r') as api:
                api = api.read()
        except FileNotFoundError:
            print("links.txt文件不存在")

        def thinklink(links, api):
            if links == '':
                print("links.txt文件为空")
            else:
                if api == '':
                    print('api.txt为空')
                else:
                    try:
                        html_result = requests.post(api, headers=headers, timeout=5, data=links).text
                        return html_result
                    except:
                        return print("失败")
        push_result = thinklink(links, api)
        print('提交完成:'+push_result)
        surplus_push_num = re.findall('"remain":(.*),"', push_result)
        surplus_push_num = surplus_push_num.pop()
        print('剩余' + surplus_push_num + '次提交机会')
    else:
        print("请将内容填充!5秒钟后自动关闭")
        time.sleep(5)
        break
    print('*'*30)
    new_answer = input("是否还需要提交，如果是的话请先去更改一下相应文件，如果是请输入1,如果否请输入0\n")
    if new_answer == '0':
        print("提交结束,5秒钟后自动关闭")
        time.sleep(5)
        break
    push_num += 1
    print("现在开始第"+str(push_num)+'次提交')


