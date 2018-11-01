#Josh Malnati
#COMP 2100-05 Network Programming
import socket
import time

HOST = '127.0.0.1' #server IP address
PORT = 12000 #server's port number

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientSocket.settimeout(1) #Sets timeout to 1 sec.

#---------------ORIGINAL CODE------------------
#for i in range(10):
#    dtStart = time.time()
#    msg='Ping ' + str(i+1) + ': ' + str(dtStart)
#    clientSocket.sendto(msg.encode(),(HOST,PORT))
#    try:
#        msgReturn, serverAddr = clientSocket.recvfrom(1024)
#        dtEnd = time.time()
#        elapseTime = dtEnd - dtStart
#
#        print(msgReturn.decode())
#        print('Elapsed time:', elapseTime, 'seconds\n')
#    
#    except socket.timeout:
#        print('Request timed out. :(\n')

#---------------Part 1 Optional Excercises ----------------
import numpy as np #used to find .min() and .max()

RTT = np.array([]) #to put RTT's of successful pings
timeoutCount = 0 #counts number of packet losses
inp=False

while(inp==False): #Input handling
    try:
        numPing = int(input('How many requests would you like to send?: '))
        if(numPing>0):
            inp=True
        else:
            raise ValueError
    except ValueError:
        print('Input must be a positive number')

for i in range(numPing): #Start requests
    dtStart = time.time()
    msg='Ping ' + str(i+1) + '\t Time: ' + str(dtStart)
    clientSocket.sendto(msg.encode(),(HOST,PORT))
    try:
        msgReturn, serverAddr = clientSocket.recvfrom(1024)
        dtEnd = time.time()
        elapseTime = dtEnd - dtStart
        RTT = np.append(RTT,elapseTime)

        print(msgReturn.decode())
#        print('Elapsed time:', elapseTime, 'seconds\n')
    
    except socket.timeout:
        timeoutCount+=1
        print('Request timed out. :(')
        
print('\nMin RTT:',round(RTT.min(),10),'seconds\nMax RTT:',round(RTT.max(),10),
      'seconds\nAverage RTT:',round(RTT.mean(),10),'seconds')
print('Packet Loss Rate:',str(round((timeoutCount/numPing)*100,2))+'%')
clientSocket.close()