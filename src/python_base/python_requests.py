import requests

"""
    requests 模块的使用
"""
if __name__ == "__main__":
    response = requests.get('https://www.baidu.com')
    #print(response.content)
    #print(response.text)
    print(response.status_code)
    pass
