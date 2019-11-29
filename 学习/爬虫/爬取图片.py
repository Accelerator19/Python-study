import requests
import os
url = "http://sc0.hao123img.com/res/r/image/2019-10-09/6c4be1da4ab240c1b61a8f5fd8a4f8c4.png"
root = "D://图片爬取//"
path = root+url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        response = requests.get(url)
        with open(path,"wb") as f:
            f.write(response.content)
            f.close()
            print("文件保存成功")
    else:
        print("图片已存在")
except:
    print("爬取失败")
