import requests
import random
import os
from datetime import datetime

def modify_steps(account, password, min_steps=None, max_steps=None):
    url = 'http://bs.svv.ink/index.php'
    steps = random.randint(min_steps, max_steps)
    data = {
        'account': account,
        'password': password,
        'steps': steps
    }

    response = requests.post(url, data=data)
    result = response.json()

    # 打印详细信息
    print("账号:", account)
    print("密码:", password)
    print("步数:", steps)
    print("响应:", result)
    print("时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 30)  # 分隔线，以提高可读性

    return result

# 从环境变量获取 Secrets 值
accounts = os.environ['ACCOUNTS'].split(',')
passwords = os.environ['PASSWORDS'].split(',')
min_steps = int(os.environ['MIN_STEPS'])
max_steps = int(os.environ['MAX_STEPS'])

results = []
successful_accounts = []  # 存储成功响应的账号和步数
for account, password in zip(accounts, passwords):
    result = modify_steps(account, password, min_steps, max_steps)
    results.append(result)
    if result['code'] == 1 and result['message'] == 'success':
        successful_accounts.append((account, result['steps']))

# 输出成功响应的账号和步数
print("成功的账号和步数：")
for account, steps in successful_accounts:
    print("账号:", account)
    print("步数:", steps)
    print("=" * 30)
