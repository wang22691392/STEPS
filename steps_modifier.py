import requests
import random
import os

def modify_steps(account, password, min_steps=None, max_steps=None):
    url = 'http://bs.svv.ink/index.php'
    steps = random.randint(min_steps, max_steps)
    data = {
        'account': account,
        'password': password,
        'steps': steps
    }

    response = requests.post(url, data=data)
    return response.json()

# 从环境变量获取 Secrets 值
num_accounts = int(os.environ['NUM_ACCOUNTS'])
min_steps = int(os.environ['MIN_STEPS'])
max_steps = int(os.environ['MAX_STEPS'])

for i in range(1, num_accounts + 1):
    account = os.environ[f'ACCOUNT{i}']
    password = os.environ[f'PASSWORD{i}']
    result = modify_steps(account, password, min_steps, max_steps)
    print(f"Account {i} - Result: {result}")
