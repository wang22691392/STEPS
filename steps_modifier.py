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
    result = response.json()

    # 打印详细信息
    print(f"Account: {account}")
    print(f"Password: {password}")
    print(f"Steps: {steps}")
    print(f"Response: {result}")

    return result

# 从环境变量获取 Secrets 值
accounts = os.environ['ACCOUNTS'].split(',')
passwords = os.environ['PASSWORDS'].split(',')
min_steps = int(os.environ['MIN_STEPS'])
max_steps = int(os.environ['MAX_STEPS'])

results = []
for account, password in zip(accounts, passwords):
    result = modify_steps(account, password, min_steps, max_steps)
    results.append(result)

# 写入运行报告到 Logs.txt 文件
with open('Logs.txt', 'a') as file:
    file.write("Run Report:\n")
    for account, result in zip(accounts, results):
        file.write(f"Account: {account}\n")
        file.write(f"Result: {result}\n")
    file.write("\n")

print(results)
