import requests
url = 'https://g.58.com/j-gllosangeles/glcar/?PGTID=0d000000-050a-325b-c1d3-375683e6c60f&ClickID=1'
headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Cookie':'id58=c5/nfF85OBC031y3MEeXAg==; gm58lang=zh_CN; 58tj_uuid=e4040510-61a1-488a-b45d-43569a3f6733; new_session=0; new_uv=1; utm_source=; spm=; init_refer=https%253A%252F%252Fduckduckgo.com%252F; Hm_lvt_f1527f186a53bd6e02d9e810f8b47b4d=1602220617; Hm_lpvt_f1527f186a53bd6e02d9e810f8b47b4d=1602220647; als=0; citylistname=gllosangeles',
        }

if __name__ == "__main__":
    data = requests.get(url)
    print(data.status_code)
    print(data.content)
    
    pass
