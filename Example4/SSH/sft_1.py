import paramiko
import getpass

transport = paramiko.Transport(('114.71.220.79', 22))

user = input('Username: ')
pwd = getpass.getpass('Password: ')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

src_file_path = 'test/iot.txt'
dst_file_path = src_file_path.split('/')[1]
sftp.get(src_file_path, dst_file_path)

src_file_path = 'index.html'
dst_file_path = src_file_path
sftp.put(src_file_path, dst_file_path)

sftp.close()
transport.close()