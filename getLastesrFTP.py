import ftplib
import socket
import os

HOST = 'ftp.mozilla.org'             #ftp网址
DIRN = 'pub/mozilla.org/webtools'    #文件目录
FILE = 'bugzilla-LASTEST.tar.gz'     #文件名

def main():
    try:
        f = ftplib.FTP(HOST)         #创建ftp对象，并连接到ftp服务器
    except (socket.error, socket.gaierror) as e:
        print('ERROR:cannot reach "%s"' %HOST)
        return
    print('***Connected to host "%s"' % HOST)

    try:
        f.login()                    #登录,以默认anonymous
    except ftplib.error_perm:
        print('ERROR:cannot login anonymously')
        f.quit()
        return
    print('***Logged in as "anonymously"')

    try:
        f.cwd(DIRN)                  #设置DIRN为工作目录
    except ftplib.error_perm:
        print('ERROR:cannot change directory to "%s"' %DIRN)
        f.quit()
        return
    print('***Changed directory to "%s"' % DIRN)

    try:
        f.retrbinary('RETR %s' %FILE, open(FILE, 'wb').write)   #下载文件，二进制
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' %FILE)
        os.unlink(FILE)
    else:
        print('***Downloaded "%s" to CWD' %FILE)
    f.quit()

if __name__ == '__main__':
    main()
