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

# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 打印脚本目录和可写性
print(f"Script Directory: {script_directory}")
print(f"Is Writable: {os.access(script_directory, os.W_OK)}")

# 写入运行报告到 Logs.txt 文件
log_file = os.path.join(script_directory, 'Logs.txt')
with open(log_file, 'a') as file:
    file.write("Run Report:\n")
    for account, result in zip(accounts, results):
        file.write(f"Account: {account}\n")
        file.write(f"Result: {result}\n")
    file.write("\n")

print(results)
