#!/usr/bin/env python3

import threading
import time

import tkinter as tk
import tkinter.ttk as ttk

import serial
import serial.tools.list_ports
 
# 'COM7' 9600bps Parityなしの場合
#Serial_Port=serial.Serial(port='COM9', baudrate=9600, parity= 'N')
#Serial_Port=serial.Serial(port='COM7', baudrate=9600)

#送信(tx)
#data=input()+'\r\n'
#data=data.encode('utf-8')
#Serial_Port.write(data)

#受信(rx)
#data=Serial_Port.readline() # 1byte受信なら data=Serial_Port.read(1)
#data=data.strip()
#data=data.decode('utf-8')
#print(data)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #self.master = tk.Tk()
        # GUIの設定
        self.master.title("シリアル通信テスト")
        self.master.geometry("500x300")

        self.comNo:str = []
        for port in serial.tools.list_ports.comports():
            self.comNo += port.device

        left = 10;
        top = 10
        marginY = 30
        
        self.labelComSet = tk.Label(self.master, text="通信設定")
        self.labelComSet.place(x=left, y=top)


        top += marginY

        self.comNo = []
        for port in serial.tools.list_ports.comports():
            self.comNo.append(port.device)
            
        self.comboCOM = ttk.Combobox(self.master, values=self.comNo, state="readonly", width=20)
        self.comboCOM.place(x=left, y=top)
        self.comboCOM.current(0)
        
        top += marginY

        self.baudRate:str = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        self.comboBaudRate = ttk.Combobox(self.master, values=self.baudRate, state="readonly", width=20)
        self.comboBaudRate.place(x=left, y=top)
        self.comboBaudRate.current(3)

        top += marginY

        self.dataBit:str = ["7bit", "8bit"]
        self.comboDataBit = ttk.Combobox(self.master, values=self.dataBit, state="readonly", width=20)
        self.comboDataBit.place(x=left, y=top)
        self.comboDataBit.current(0)
        
        top += marginY

        self.parity:str = ["なし", "あり"]
        self.comboParity = ttk.Combobox(self.master, values=self.parity, state="readonly", width=20)
        self.comboParity.place(x=left, y=top)
        self.comboParity.current(0)

        top += marginY

        self.stopBit:str = ["0", "1"]
        self.comboStopBit = ttk.Combobox(self.master, values=self.stopBit, state="readonly", width=20)
        self.comboStopBit.place(x=left, y=top)
        self.comboStopBit.current(0)

        top += marginY

        # ボタンの設定
        self.buttonSetSerial = tk.Button(self.master, text="Set", width=10, command=self.ButtonSetSerial_Click)
        self.buttonSetSerial.place(x=left, y=top)
        self.buttonSetSerial['state'] = tk.NORMAL

        left = 250;
        top = 10
               
        self.labelComSet = tk.Label(self.master, text="送信内容")
        self.labelComSet.place(x=left, y=top)

        top += marginY

        self.entryText = ttk.Entry(self.master) 
        self.entryText.place(x=left, y=top)
        
        top += marginY

        # ボタンの設定
        self.buttonSendMsg = tk.Button(self.master, text="Send", width=10, command=self.ButtonSendMsg_Click)
        self.buttonSendMsg.place(x=left, y=top)
        self.buttonSendMsg['state'] = tk.NORMAL

        top += (marginY * 2)

        # 受信
        self.labelComSet = tk.Label(self.master, text="受信内容")
        self.labelComSet.place(x=left, y=top)

        top += marginY

        self.entryText = ttk.Entry(self.master) 
        self.entryText.place(x=left, y=top)
        

    def ButtonSetSerial_Click(self):
        Serial_Port=serial.Serial(port=self.comboCOM, baudrate=9600)



    def ButtonSendMsg_Click(self):
        self.serial_Port=serial.Serial(port='COM10', baudrate=9600)
        #data='a'+'\r\n'
        #data=data.encode('utf-8')
        #self.serial_Port.write(data)
        #self.serial_Port.close()
        msg = self.entryText.get()
        if msg != "":
            msg=msg+'\r\n'
            msg=msg.encode('utf-8')
            self.serial_Port.write(msg)
        self.serial_Port.close()


def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()