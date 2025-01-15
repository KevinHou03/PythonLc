def jobScheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)    # 将作业按照利润从大到小排序
    max_deadline = max(job[1] for job in jobs)# 找到最大的截止日期
    slots = [None] * (max_deadline + 1)  # 初始化时间槽数组，初始值为None表示时间槽未被占用

    total_profit = 0
    for job in jobs:
        job_id, deadline, profit = job
        for d in range(deadline, 0, -1):    # 从作业的截止日期开始，向前寻找空闲的时间槽
            if slots[d] is None:  # 如果找到了空闲的时间槽
                slots[d] = job_id  # 将作业安排到这个时间槽
                total_profit += profit  # 累加总利润
                break  # 跳出循环，继续安排下一个作业
    # 返回总利润和安排的作业列表（None表示时间槽未被占用）
    return total_profit, slots[1:]  # 从索引1开始，因为没有0号时间槽
# 示例作业列表，每个作业由[作业ID, 截止日期, 利润]组成
jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

total_profit, scheduled_jobs = jobScheduling(jobs)
print("Total Profit:", total_profit)
print("Scheduled Jobs:", scheduled_jobs)
