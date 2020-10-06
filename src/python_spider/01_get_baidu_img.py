 
######################################################################
# 
# @author zhangxiaomin(1396729865@qq.com)
# 
######################################################################
 
import requests
if __name__ == '__main__':
    url = 'https://dss2.bdstatic.com/lfoZeXSm1A5BphGlnYG/skin/205.jpg?2'
    file_name = 'baidu_background_yangmi.jpg'
    url = 'https://dss0.bdstatic.com/l4oZeXSm1A5BphGlnYG/skin/211.jpg?2'
    file_name = 'baidu_background_yangmi2.jpg'
    url = 'https://dss1.bdstatic.com/kvoZeXSm1A5BphGlnYG/skin/200.jpg?2'
    file_name = 'baidu_background_yangmi3.jpg'
    url='https://bkimg.cdn.bcebos.com/pic/8d5494eef01f3a292df58a938a6fab315c6034a8d61e?x-bce-process=image/resize,m_lfit,h_452,limit_1'
    file_name = 'baidu_background_yangmi4.jpg'
    response = requests.get(url)
#    with open(file_name,'wb') as file:
#        file.write(response.content)
    print(response.request.url)
    print(response.url)
    print(response.status_code)
    print(response.request.headers)
    print(response.headers)
    pass

