import nmap
import socket
nmScan=nmap.PortScanner()
print('\nAll Hosts:\n')
print(nmScan.all_hosts())
print('\nSpecify The IP Address Of The System To Run The Port Scan.')
ip=input()
print('\nSpecify The Range Of Ports To Scan.')
print('\nEnter The Starting Port.')
start=input()
print('\nEnter The Ending Port.')
end=input()
print('\n\n\nPort Numbers & Corresponding Services:\n\n\n')
for i in range(0,(int(end))+1):
     try:
          service=socket.getservbyport(i)
          print ("Port: ", i, "runs service ", service)
     except:
               continue
ran=(str(start))+"-"+(str(end))
nmScan.scan(ip, ran)
print('\n\n\nPort Scan Completed.\n\n\n')
print('\nScan Information:\n')
print(nmScan.scaninfo())
openport=0
filteredport=0
for host in nmScan.all_hosts():
     print('Host : %s (%s)' % (host, nmScan[host].hostname()))
     print('State : %s' % nmScan[host].state())
     for proto in nmScan[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
         lport = nmScan[host][proto].keys()
         #lport.sort()
         sorted(lport)
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
             if(nmScan[host][proto][port]['state']=='open'):
                 openport+=1
             elif(nmScan[host][proto][port]['state']=='filtered'):
                 filteredport+=1
print('\nNumber Of Open Ports: ',openport)
print('\nNumber Of Filtered Ports: ',filteredport)
print('\nEnter Any Key To Exit.\n')
exi=input()
