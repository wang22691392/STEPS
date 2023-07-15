import requests

def modify_steps(username, password, steps):
    url = 'http://bs.svv.ink'  # 接口 URL
    data = {
        'username': username,
        'password': password,
        'steps': steps
    }

    try:
        response = requests.post(url, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return f'Request error: {e}'

if __name__ == '__main__':
    # 在此处填入你的用户名、密码和要修改的步数
    username = '15033296069'
    password = '20030101h'
    steps = 50000

    result = modify_steps(username, password, steps)
    print(result)
    print('Request:', response.request.url)
    print('Request data:', response.request.body)
    print('Response:', response.text)

