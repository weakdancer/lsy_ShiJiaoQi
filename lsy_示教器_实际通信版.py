# -*- coding: utf-8 -*-
#lsy_示教器 20170502 lsy_示教器_实际通信版
import serial
import winsound

import time
import sys


from Tkinter import *


class ShiJiaoQi(object):
	def __init__(self):
		print "dummy_shijiao_test initlized."
		self.s=serial.Serial(port="COM4",baudrate=250000,timeout=0.01,bytesize=8,stopbits=1)
		time.sleep(5)
		self.s.write("G91\n")
	def write(self,str_):
		print str_
		self.s.write(str_)
	def move(self,coordinate_var,axis,flag,num):
		self.write("G1 "+axis+flag+num+"\n")
		x,y=eval(coordinate_var.get())
		if axis=="X":
			coordinate_var.set(str((x+float(flag+num),y)))
		if axis=="Y":
			coordinate_var.set(str((x,y+float(flag+num))))
	def home(self,coordinate_var):
		self.write("G28 X0 Y0\n")
		coordinate_var.set("(0,0)")
		
s=ShiJiaoQi()
# s=serial.Serial(port=3,baudrate=115200,timeout=0.01,bytesize=8,stopbits=1)

root = Tk()

def gen_coordinate(coordinate_var):
	x,y=eval(coordinate_var.get())
	return "G1 X%f Y%f\n"%(x,y)

increment = StringVar()
increment.set("0.1")


B_s1 = Button(root, text="0.1mm", command=lambda :increment.set("0.1"))
B_s2 = Button(root, text="1mm", command=lambda :increment.set("1"))
B_s3 = Button(root, text="10mm", command=lambda :increment.set("10"))

B_forward=Button(root, text="forward", command=lambda :s.move(E_coordinate_current_var,"Y","-",increment.get()))
B_backward=Button(root, text="backward", command=lambda :s.move(E_coordinate_current_var,"Y","+",increment.get()))
B_left=Button(root, text="left", command=lambda :s.move(E_coordinate_current_var,"X","-",increment.get()))
B_right=Button(root, text="right", command=lambda :s.move(E_coordinate_current_var,"X","+",increment.get()))


B_home=Button(root, text="home", command=lambda :s.home(E_coordinate_current_var))


E_coordinate_current_var=StringVar()
E_coordinate_current_var.set("(0,0)")
E_coordinate_current=Entry(root,textvariable = E_coordinate_current_var,font="courier 12 bold",width=25)



Text_records=Text(root,font ="courier 12 bold",width=30,height=28,bg = 'green')


B_record=Button(root, text="record", command=lambda :Text_records.insert(END,gen_coordinate(E_coordinate_current_var)))

def undo():
	global Text_records
	print Text_records.delete("end-1c linestart", "end")
def export():
	global Text_records
	print Text_records.get("1.0",END)
	f=file("export.gcode","w+")
	f.write(Text_records.get("1.0",END))
	f.close()
B_undo = Button(root, text="undo",command=undo)
#TODO1

	
B_export=Button(root, text="export",command=export)
#TODO2


B_s1.grid(column=5,row=0)
B_s2.grid(column=5,row=1)
B_s3.grid(column=5,row=2)
B_forward.grid(column=2,row=0)
B_backward.grid(column=2,row=2)
B_left.grid(column=1,row=1)
B_right.grid(column=3,row=1)
B_record.grid(column=5,row=6)
B_undo.grid(column=5,row=7)
B_home.grid(column=5,row=9)
B_export.grid(column=8,row=8)
E_coordinate_current.grid(column=2,row=4)
Text_records.grid(column=9,row=9)

SPEED=10
def loop():
	pass
	root.after(SPEED,loop)
root.after(SPEED,loop)
root.mainloop()
