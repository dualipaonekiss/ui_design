#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Jun 14, 2023 11:58:22 AM +0630  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import kaungkaung2_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    kaungkaung2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    kaungkaung2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1536x793+-8+-8")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.169, rely=0.013, height=63, width=1035)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 30")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(takefocus="10")
        self.Label1.configure(text='''Short Physical Performance Battery(SPPB):Sit And Stand''')
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.007, rely=0.113, relheight=0.878
                , relwidth=0.465)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.475, rely=0.113, relheight=0.875
                , relwidth=0.518)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffffff")
        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.075, rely=0.014, height=71, width=123)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 20")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Score''')
        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.742, rely=0.014, height=71, width=105)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 18")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Duration:''')
        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.075, rely=0.161, height=52, width=124)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ff0000")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 19")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''4''')
        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.73, rely=0.146, height=53, width=124)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ff0000")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 18")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''3.7s''')
        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.0, rely=0.248, relheight=0.457, relwidth=0.497)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#ffffff")
        self.Label6 = tk.Label(self.Frame3)
        self.Label6.place(relx=0.025, rely=0.057, height=35, width=156)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 12")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Predicted Distance''')
        self.Label7 = tk.Label(self.Frame3)
        self.Label7.place(relx=0.025, rely=0.227, height=23, width=156)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 12")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Predicted Pixel Len:''')
        self.Label8 = tk.Label(self.Frame3)
        self.Label8.place(relx=0.025, rely=0.369, height=35, width=134)
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 12")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Person Aeras''')
        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.608, rely=0.057, height=35, width=123)
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#ff0000")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 15")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''3m''')
        self.Label10 = tk.Label(self.Frame3)
        self.Label10.place(relx=0.608, rely=0.199, height=35, width=123)
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#ff0000")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Segoe UI} -size 14")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''3m''')
        self.Label11 = tk.Label(self.Frame3)
        self.Label11.place(relx=0.608, rely=0.369, height=35, width=123)
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#ff0000")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Segoe UI} -size 13")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''3m''')
        self.Label12 = tk.Label(self.Frame3)
        self.Label12.place(relx=0.025, rely=0.574, height=45, width=156)
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#ffffff")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Segoe UI} -size 12")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Current line length:''')
        self.Label13 = tk.Label(self.Frame3)
        self.Label13.place(relx=0.025, rely=0.767, height=52, width=144)
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#ffffff")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Segoe UI} -size 12")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Current pixcel len:''')
        self.Label14 = tk.Label(self.Frame3)
        self.Label14.place(relx=0.608, rely=0.606, height=32, width=124)
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#ff0000")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font="-family {Segoe UI} -size 12")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''3m''')
        self.Label15 = tk.Label(self.Frame3)
        self.Label15.place(relx=0.608, rely=0.798, height=32, width=124)
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#ff0000")
        self.Label15.configure(compound='left')
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font="-family {Segoe UI} -size 13")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''3m''')
        self.Frame4 = tk.Frame(self.Frame2)
        self.Frame4.place(relx=0.503, rely=0.248, relheight=0.458
                , relwidth=0.483)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")
        self.Label16 = tk.Label(self.Frame4)
        self.Label16.place(relx=0.339, rely=0.031, height=42, width=174)
        self.Label16.configure(anchor='w')
        self.Label16.configure(background="#80ff00")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(font="-family {Segoe UI} -size 12")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Measuring times''')
        self.Label17 = tk.Label(self.Frame4)
        self.Label17.place(relx=0.026, rely=0.223, height=42, width=104)
        self.Label17.configure(anchor='w')
        self.Label17.configure(background="#ffffff")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font="-family {Segoe UI} -size 12")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(text='''Point-1 :''')
        self.Label18 = tk.Label(self.Frame4)
        self.Label18.place(relx=0.026, rely=0.381, height=42, width=104)
        self.Label18.configure(anchor='w')
        self.Label18.configure(background="#ffffff")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font="-family {Segoe UI} -size 12")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(text='''Point-2 :''')
        self.Label19 = tk.Label(self.Frame4)
        self.Label19.place(relx=0.026, rely=0.541, height=42, width=104)
        self.Label19.configure(anchor='w')
        self.Label19.configure(background="#ffffff")
        self.Label19.configure(compound='left')
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(font="-family {Segoe UI} -size 12")
        self.Label19.configure(foreground="#000000")
        self.Label19.configure(text='''Point-3 :''')
        self.Label20 = tk.Label(self.Frame4)
        self.Label20.place(relx=0.026, rely=0.733, height=41, width=104)
        self.Label20.configure(anchor='w')
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(compound='left')
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(font="-family {Segoe UI} -size 12")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Point-4 :''')
        self.Label21 = tk.Label(self.Frame4)
        self.Label21.place(relx=0.573, rely=0.223, height=42, width=134)
        self.Label21.configure(anchor='w')
        self.Label21.configure(background="#800040")
        self.Label21.configure(compound='left')
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(font="-family {Segoe UI} -size 12")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''3s''')
        self.Label22 = tk.Label(self.Frame4)
        self.Label22.place(relx=0.573, rely=0.381, height=42, width=134)
        self.Label22.configure(anchor='w')
        self.Label22.configure(background="#800040")
        self.Label22.configure(compound='left')
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(font="-family {Segoe UI} -size 12")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(text='''3s''')
        self.Label23 = tk.Label(self.Frame4)
        self.Label23.place(relx=0.573, rely=0.541, height=42, width=134)
        self.Label23.configure(anchor='w')
        self.Label23.configure(background="#800040")
        self.Label23.configure(compound='left')
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(font="-family {Segoe UI} -size 13")
        self.Label23.configure(foreground="#000000")
        self.Label23.configure(text='''3s''')
        self.Label24 = tk.Label(self.Frame4)
        self.Label24.place(relx=0.573, rely=0.733, height=41, width=134)
        self.Label24.configure(anchor='w')
        self.Label24.configure(background="#800040")
        self.Label24.configure(compound='left')
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(font="-family {Segoe UI} -size 13")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(text='''3s''')

        self.Label25 = tk.Label(self.Frame2)  
        self.Label25.place(relx=0.013, rely=0.731, height=42, width=135)
        self.Label25.configure(command=kaungkaung2_support.btn_chooseVideo_action)  
        self.Label25.configure(anchor='w')                    
        self.Label25.configure(background="#ff0080")        
        self.Label25.configure(compound='left')
        self.Label25.configure(disabledforeground="#a3a3a3")
        self.Label25.configure(font="-family {Segoe UI} -size 13")
        self.Label25.configure(foreground="#000000")
        self.Label25.configure(text='''Choose Video''')

        self.Frame5 = tk.Frame(self.Frame2)
        self.Frame5.place(relx=0.252, rely=0.731, relheight=0.065
                , relwidth=0.736)
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#d9d9d9")
        self.Label26 = tk.Label(self.Frame2)
        self.Label26.place(relx=0.013, rely=0.831, height=42, width=135)
        self.Label26.configure(anchor='w')
        self.Label26.configure(background="#ff0080")
        self.Label26.configure(compound='left')
        self.Label26.configure(disabledforeground="#a3a3a3")
        self.Label26.configure(font="-family {Segoe UI} -size 13")
        self.Label26.configure(foreground="#000000")
        self.Label26.configure(text='''Load_model''')
        self.Frame6 = tk.Frame(self.Frame2)
        self.Frame6.place(relx=0.252, rely=0.831, relheight=0.066
                , relwidth=0.736)
        self.Frame6.configure(relief='groove')
        self.Frame6.configure(borderwidth="2")
        self.Frame6.configure(relief="groove")
        self.Frame6.configure(background="#d9d9d9")
        self.Label27 = tk.Label(self.Frame2)
        self.Label27.place(relx=0.05, rely=0.922, height=43, width=133)
        self.Label27.configure(anchor='w')
        self.Label27.configure(background="#808000")
        self.Label27.configure(compound='left')
        self.Label27.configure(disabledforeground="#a3a3a3")
        self.Label27.configure(font="-family {Segoe UI} -size 10")
        self.Label27.configure(foreground="#000000")
        self.Label27.configure(text='''Predict line length''')
        self.Label28 = tk.Label(self.Frame2)
        self.Label28.place(relx=0.39, rely=0.922, height=41, width=133)
        self.Label28.configure(anchor='w')
        self.Label28.configure(background="#808000")
        self.Label28.configure(compound='left')
        self.Label28.configure(disabledforeground="#a3a3a3")
        self.Label28.configure(font="-family {Segoe UI} -size 10")
        self.Label28.configure(foreground="#000000")
        self.Label28.configure(text='''Predict Score''')
        self.Label29 = tk.Label(self.Frame2)
        self.Label29.place(relx=0.767, rely=0.922, height=41, width=144)
        self.Label29.configure(anchor='w')
        self.Label29.configure(background="#808000")
        self.Label29.configure(compound='left')
        self.Label29.configure(disabledforeground="#a3a3a3")
        self.Label29.configure(font="-family {Segoe UI} -size 10")
        self.Label29.configure(foreground="#000000")
        self.Label29.configure(text='''Clear line''')

def start_up():
    kaungkaung2_support.main()

if __name__ == '__main__':
    kaungkaung2_support.main()




