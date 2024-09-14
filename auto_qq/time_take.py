import schedule
import time
from test_k import main

# 设置每天22:10执行main函数
def schedule_job():
    schedule.every().day.at("19:29").do(main)

    while True:
        # 检查是否有任务需要执行
        schedule.run_pending()
        # 每隔40s检查一次
        time.sleep(10)

if __name__ == '__main__':
    schedule_job()