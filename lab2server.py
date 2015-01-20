#running sample 5
import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread
def clientthread(conn):
    while 1:
        data=conn.recv(1024)
        if not data:
            break
        data2=str(data)
        data2=data2[2:len(data2)-5]
        reply= data2+" Tarek\n"
        conn.sendall(reply.encode('UTF-8'))    
    conn.close()

    
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("failed to create socket")
    print("Error code:"+str(msg[0])+" ,Error message: "+msg[1])
    sys.exit()
print("socket created")
host= ''
port= 8888
try:
    s.bind((host,port))
except socket.error:
    print("Bind faled. Error Code: "+str(msg[0])+' ,message:, '+msg[1])
    sys.exit()
s.listen(5)
#Running Sample 7
while 1:
    conn,addr=s.accept()
    thread.start_new_thread(clientthread,(conn,))
    #print("Connection with "+addr[0]+":"+str(addr[1]))
    #running sample 6

s.close()