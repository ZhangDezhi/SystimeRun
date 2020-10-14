import datetime
import time
import os
import ctypes, sys

# 管理员 身份声明
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # Code of your program here
    pass
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)









a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(a)
startTime = str(a)  # 输入一个时间，此是个字符串
# endTime = '2019-07-11 15:35'
# for i in range(100):
while True:
    # 参数days=1（天+1） 可以换成 minutes=1（分钟+1）、seconds=1（秒+1）
    endTime = (datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
        seconds=10)).strftime("%Y-%m-%d %H:%M:%S")
    # print(startTime,endTime)
    print(endTime)
    startTime = endTime
    x = startTime[11]+startTime[12]
    x = str(x)
    print("时：%s" % x)
    y = startTime[14]+startTime[15]
    y = str(y)
    print("分钟：%s" % str(startTime[14])+startTime[15])
    z = startTime[17]+startTime[18]
    z = str(z)
    print("秒：% s" % str(startTime[17])+startTime[18])
    _date = 'time  ' + x + ":" + y + ":" + z + "." + z
    os.system(_date)
    time.sleep(1)