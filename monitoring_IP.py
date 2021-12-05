from ipaddress import IPv4Address
from ping3 import ping
import PySimpleGUI as sg

class check_ping:
    
    def set_status(self,temp):
        if temp:
            status =f'ONLINE [{temp}]' if temp>0 else 'WARNING'
        else:
            status ='OFFLINE'
        return status

    def ping_ip(self):
        start=IPv4Address('')
        finish=IPv4Address('')
        
        ips = [str(IPv4Address(ip)) for ip in range(int(start), int(finish))]
        for idx, ip in enumerate(ips):
                t = ping(ip, timeout=2)
                status= check_ping.set_status(self, temp=t) 
                print(f'IP: {ip}\nSTATUS: {status}\n') 
                if idx == len(ips)-1:
                   check_ping.ping_ip(self) 
    
class ScrenPython:             
    def __init__(self):
        layout = [
            [sg.Text('IP INI', size=(15,0)),sg.Input(k='INI')],
            [sg.Text('IP FIN',size=(15,0)),sg.Input(k='FIN')],
            [sg.Slider(range=(2,10),default_value=0,orientation='h',size=(15,20),key='TIMEOUT')],
            [sg.Button('START')],
            [sg.Output(size=(50,20),key='-OUT-')]
        ]   
        self.interf = sg.Window("MONITORING IP").layout(layout) 

    def start(self):    
        while True:
            self.values,self.button = self.interf.Read();
            while True:
                check_ping.ping_ip(self) 
                
        
v = ScrenPython()
v.start()