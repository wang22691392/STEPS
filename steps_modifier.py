import requests

def modify_steps(account, password, steps):
    url = 'http://bs.svv.ink/index.php'
    data = {
        'account': account,
        'password': password,
        'steps': steps
    }

    response = requests.post(url, data=data)
    return response.json()

# 示例用法
account = '15033296069'
password = '20030101h'
new_steps = '50000'

result = modify_steps(account, password, new_steps)
print(result)
