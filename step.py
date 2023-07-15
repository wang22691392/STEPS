import requests

def main():
    url = "http://bs.svv.ink/index.php"
    data = {
        "username": "your_username",
        "password": "your_password",
        "steps": 5000
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
