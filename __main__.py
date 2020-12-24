# -*- coding: UTF-8 -*-	
import datetime
import time
import os
import ctypes, sys
import platform
print(platform.system())

#plat_tuple=platform.architecture()
system=platform.system()
#plat_version=platform.platform()
if system == 'Windows':
    print('this is windows system')
#    print('version is: '+plat_version)
    import tkinter as tk
    import _thread

elif system == 'Linux':
    print('this is linux system ')
#    print('version is: '+plat_version)
    import Tkinter as tk
    import thread
    import subprocess

class APP:
    m_runmark=True
    m_value=1
    frame = None

    def __init__(self,master):
        global frame
        frame = tk.Frame(master,height=200,bd=2,width=250)
        frame.pack()

        self.label1=tk.Label(frame,text="实际时间(s)",bg="yellow",height=2,bd=2,width=10)
        self.label1.place(x=10,y=10)

        self.label1=tk.Label(frame,text="目标时间(s)",bg="green",height=2,bd=2,width=10)
        self.label1.place(x=10,y=50)

        self.entry1 = tk.Entry(frame,width=20,bd=2)
        self.entry1.insert('insert','1')
        self.entry1.config(state=tk.DISABLED)
        self.entry1.place(x=90,y=20)

        self.entry2 = tk.Entry(frame,width=20,bd=2)
        self.entry2.insert('insert','10')
        self.entry2.place(x=90,y=60)

        self.button1 = tk.Button(frame,text="退出",fg="red",command=frame.quit,height=2,bd=2,width=8)
        self.button1.place(x=15,y=120)

        self.button2 = tk.Button(frame,text="运行",fg="red",command=self.start,height=2,bd=2,width=8)
        self.button2.place(x=90,y=120)

        self.button2 = tk.Button(frame,text="停止",fg="red",command=self.stop,height=2,bd=2,width=8)
        self.button2.place(x=165,y=120)

    def exit(self):
        global frame
        frame.quit


    def stop(self):
        global m_runmark
        m_runmark = False
        print('已经停止')

    def start(self):
        global m_runmark ,m_value
        m_runmark = True
        print ('已点击按钮')
        oldtime=self.entry1.get()
        newtime=self.entry2.get()
        m_value = int(newtime)/int(oldtime)
        a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("当前时间: %s 时间尺为: %d" %( a ,m_value))
        if system == 'Windows':
            _thread.start_new_thread(self.threadloop,("thread_loop",1,))   #创建子线程执行循环动作
        elif system == 'Linux':
           thread.start_new_thread(self.threadloop,("thread_loop",1,))   #创建子线程执行循环动作
        

    def threadloop ( nloop,nsec,lock):
        a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        startTime = str(a)  # 输入一个时间，此是个字符串
        # endTime = '2019-07-11 15:35'
        # for i in range(100):
        global m_runmark ,m_value
        while m_runmark:
            # 参数days=1（天+1） 可以换成 minutes=1（分钟+1）、seconds=1（秒+1）
            endTime = (datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta( 
                seconds=m_value)).strftime("%Y-%m-%d %H:%M:%S")
            # print(startTime,endTime)
            print("修改时间: %s --> %s" %(startTime, endTime))
            startTime = endTime
            x = startTime[11]+startTime[12]
            x = str(x)
            # print("时：%s" % x)
            y = startTime[14]+startTime[15]
            y = str(y)
            # print("分钟：%s" % str(startTime[14])+startTime[15])
            z = startTime[17]+startTime[18]
            z = str(z)
            # print("秒：% s" % str(startTime[17])+startTime[18])
            if system == 'Windows':
                _date = 'time  ' + x + ":" + y + ":" + z + "." + z 
                os.system(_date)
            elif system == 'Linux':
                _date = 'date -s  ' + x + ":" + y + ":" + z + "." + z
                su_root("root123",_date)
           # os.system("date -s "2015-02-10 23:28:00"")
            time.sleep(1)


# Windows 管理员 身份声明
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Linux root 
def su_root(root_pwd,rcmd):
    cmd="su -"
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdin.write(root_pwd.encode('utf-8'))
    p.stdin.write("\n".encode('utf-8'))
    # p.stdin.write(rcmd.encode('utf-8'))
    out,err=p.communicate(rcmd.encode('utf-8'))
    # p.stdin.flush()
    if err == None:
        print(out)
    else:
        print(err)


if __name__ == '__main__':

    root=tk.Tk()
    app=APP(root)

    if system == 'Windows':
        if is_admin():
            # Code of your program here
            root.mainloop()
            root.destroy()
            pass
        else:
            app.exit
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    elif system == 'Linux':
        root.mainloop()
        root.destroy()
        pass

