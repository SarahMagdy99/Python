from tkinter import *
import random
import tk_tools

def update():
		global Temp_rand
		global Time_rand 
		global Time_List
		global Hum_rand
		Temp_rand = random.randint(0,500)
		Temp_Label['text'] = str(Temp_rand) + "  DegC"
		Time_rand = random.randint(0,3)
		Time_Label['text'] = Time_List[Time_rand]
		Hum_rand = random.randint(0,100)
		Hum_Label['text'] = str(Hum_rand)+'%'
		window_2.after(1000, update)

def Temp():
	Temp_Wind = Tk()
	Temp_Wind.title("Temperature")
	Temp_Wind.geometry("500x500")
	global Temp_Gauge
	Temp_Gauge=tk_tools.Gauge(Temp_Wind,max_value = 500,min_value =0,divisions=10,height = 400,width=400,label='Temperature',unit="DegC")
	Temp_Gauge.pack()
	def Gauge_update():
		global Temp_rand
		global Temp_Gauge
		Temp_Gauge.set_value(Temp_rand)
		Temp_Wind.after(1000,Gauge_update)
	Gauge_update()
	Temp_Wind.mainloop()

def Time():
	global Time_rand 
	Time_Wind = Tk()
	Time_Wind.title("Time")
	Time_Wind.geometry("400x200")
	T_Label = Label(Time_Wind,font=("Arial", 60))
	T_Label.place(x=50 , y=50)
	def Time_update():
		global Time_rand
		if (Time_rand == 0):
			T_Label['text'] = str(random.randint(5,12))+':'+str(random.randint(0,60))+':'+str(random.randint(0,60))
		elif (Time_rand == 1):
			T_Label['text'] = str(random.randint(12,17))+':'+str(random.randint(0,60))+':'+str(random.randint(0,60))
		elif (Time_rand == 2):
			T_Label['text'] = str(random.randint(17,21))+':'+str(random.randint(0,60))+':'+str(random.randint(0,60))
		elif (Time_rand == 3):
			T_Label['text'] = str(random.randint(0,4))+':'+str(random.randint(0,60))+':'+str(random.randint(0,60))
		Time_Wind.after(1000, Time_update)
	Time_update()
	Time_Wind.mainloop()

def Hum():
	Hum_Wind = Tk()
	Hum_Wind.title("Humidity")
	Hum_Wind.geometry("500x500")
	global Hum_Gauge
	Hum_Gauge=tk_tools.Gauge(Hum_Wind,max_value = 100,min_value =0,divisions=10,height = 400,width=400,label='Humidity',unit="%")
	Hum_Gauge.pack()
	def Hum_Gauge_update():
		global Hum_rand
		global Hum_Gauge
		Hum_Gauge.set_value(Hum_rand)
		Hum_Wind.after(1000,Hum_Gauge_update)
	Hum_Gauge_update()
	Hum_Wind.mainloop()	
def Submit():
	global name_var
	global pass_var
	name = name_var.get()
	password = pass_var.get()
	if (name == "User" and password == "1234"):
		name_var.set("")
		pass_var.set("")
		global Pass_Right 
		Pass_Right = 1
		window_1.destroy()
	else:
		name_var.set("")
		pass_var.set("")
		wnd_label = Label(window_1 , text = "Username or password incorrect" , fg = 'red')
		name_Label = Label(window_1 , text="Username: ")
		name_Entry = Entry(window_1,textvariable = name_var )
		pass_Label = Label(window_1 , text="Password: ")
		pass_Entry = Entry(window_1,textvariable = pass_var , show = '*' )
		sub_btn = Button(window_1 , text = "Submit", bd = '5',bg ='green', command = Submit )
		wnd_label.grid(row = 0 , column = 0)
		name_Label.grid(row = 1 , column = 0)
		name_Entry.grid(row = 1 , column = 1)
		pass_Label.grid(row = 2 , column = 0)
		pass_Entry.grid(row = 2 , column = 1)
		sub_btn.grid(row = 3 , column = 1)
Pass_Right = 0	
window_1 = Tk()
window_1.title("Username and Password")
window_1.geometry("350x100")
name_var = StringVar()
pass_var = StringVar()
wnd_label = Label(window_1 , text="Enter Username and Password " , fg = 'blue')
name_Label = Label(window_1 , text="Username: ")
name_Entry = Entry(window_1,textvariable = name_var )
pass_Label = Label(window_1 , text="Password: ")
pass_Entry = Entry(window_1,textvariable = pass_var , show = '*' )
sub_btn = Button(window_1 , text = "Submit", bd = '5',bg ='green', command = Submit )
wnd_label.grid(row = 0 , column = 0)
name_Label.grid(row = 1 , column = 0)
name_Entry.grid(row = 1 , column = 1)
pass_Label.grid(row = 2 , column = 0)
pass_Entry.grid(row = 2 , column = 1)
sub_btn.grid(row = 3 , column = 1)
window_1.mainloop()
Time_List = ["Morning","Afternoon","Evening","Night"]
if(Pass_Right == 1):
	window_2 = Tk()
	window_2.title("Nuclear Reactor")
	window_2.geometry("750x500")
	Nuclear_Photo = PhotoImage(file = 'Nuclear6.png')
	Nuclear_Photo = Nuclear_Photo.subsample(2,1)
	Nuclear_Label = Label(window_2 , image = Nuclear_Photo)
	Nuclear_Label.place (x = 350 , y = 1)
	window_2.update()
	Temp_btn = Button(window_2 , text = "Temperature", bd = '5',bg ='blue', command = Temp )
	Temp_btn.place (x = 85 , y = 80)
	Temp_rand = random.randint(0,500)
	Temp_Label = Label(window_2)
	Temp_Label.place (x = 260 , y = 80)
	Time_btn = Button(window_2 , text = "       Time      ", bd = '5',bg ='blue', command = Time )
	Time_btn.place (x = 85 , y = 240)
	Time_Label = Label(window_2)
	Time_Label.place (x = 260 , y = 240)
	Hum_btn = Button(window_2 , text = "  Humidity  ", bd = '5',bg ='blue', command = Hum )
	Hum_btn.place (x = 85 , y = 400)
	Hum_Label = Label(window_2)
	Hum_Label.place (x = 260 , y = 400)
	update()
	window_2.mainloop()