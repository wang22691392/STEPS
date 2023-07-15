import os
import requests

def main():
    url = os.environ.get("URL")
    data = {
        "username": "15033296069",
        "password": "20030101h",
        "steps": 50000
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("步数修改成功！")
    else:
        print("步数修改失败。")
        print("错误码:", response.status_code)
        print("错误信息:", response.text)

if __name__ == "__main__":
    main()
