#_*_ coding:utf-8 _*_
import wmi
import smtplib
import sys
import socket

def disk_space(f):   
    #通过wmi库，获取并返回当前磁盘空间剩余大小
    c = wmi.WMI()
    disk = c.Win32_LogicalDisk(DeviceID=f)
    result = int(disk[0].FreeSpace)
    print("Disk %s FreeSpace:%dG" % (f,int(result/1024/1024/1024)))
    return int(result/1024/1024/1024)



def get_ip():
    #获取当前检查PC的ip，
    hostname = socket.getfqdn(socket.gethostname())
    windows_ip = socket.gethostbyname(hostname)
    print(windows_ip)
    return windows_ip

def send_email():
    #通过QQ邮件发送邮件，需要一个登录的授权码
    #具体，进入QQ邮件设置：
    #账户，找到POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务，开启IMAP/SMTP服务
    #根据提示（如通过发送短信取得授权码）
    host = "smtp.qq.com"
    subject = 'out of disk space!'
    to = ['xxx@xxx.com','xxxx@xxxxx.com','405120932@qq.com'] 
    from_email = "405120932@qq.com"
    text = 'Windows %s disk free space:C:%dG,D%dG' % (get_ip(),disk_space(c),disk_space(d))
    body = "\r\n".join((
    "From:%s" % from_email,
    "To  :%s" % to,
    "Subject:%s" % subject,
    "",
    text))    
    server = smtplib.SMTP()
    server.connect(host,"587")
    server.starttls()
    server.login("405120932@qq.com","授权码")
    server.sendmail(from_email,to,body)
    server.quit()


def return_result():
    #判断，如果C小于20G，或D盘少于50G，则发邮件通知
    if disk_space(c) < 20 or disk_space(d) < 50:
        print("send email ...")        
        send_email()
    else:
        print("not send email")


if __name__ == "__main__":   
    #定义需要检查的PC 盘
    c=r'C:'
    d=r'D:'
    return_result() 
