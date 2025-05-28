import customtkinter   as ctk
import os
import sys
from pyperclip import copy
from generate import gen

class Window(ctk.CTk):
    def __init__(self, fg_color = "#222326", **kwargs):
        super().__init__(fg_color = fg_color, **kwargs)
        self.title('Passworld Generator')
        self.geometry("400x400")
        self.resizable(False,False)
        self.icon =os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), "icon", "ico.ico")
        self.iconbitmap(self.icon)
        
        
        self.slider = ctk.CTkSlider(self, from_=8,to=26,command=self.Switch_Slider_Current_Value,button_color="#666A73",button_hover_color="#3C3D40")
        self.l1 = ctk.CTkLabel(self,text=f'Passworld Lenght: {int(self.slider.get())}')
        self.l1.pack(padx=5,pady=(20,0))
        self.slider.pack(pady=(0,20))
        
        self.checks = ['Upper Letter (A-Z)','Lower Letter (a-z)','Numbers (0-9)','Simbols (!@#$...)']
        self.vars = []
        for _ in self.checks:
            var = ctk.IntVar()
            self.checks = ctk.CTkCheckBox(self,text=_,hover_color="#666A73",checkmark_color="#D7D7D9",fg_color="#3C3D40",variable=var).pack(pady=5,anchor='w',padx=30)
            self.vars.append((_ , var))
      
        self.p_entry = ctk.CTkEntry(self,state='disabled',justify='center',width=92)
        self.p_entry.pack(pady=(20,0))
        
        self.frame = ctk.CTkFrame(self,fg_color="#222326")
        self.button = ctk.CTkButton(self.frame, text='Generate Passworld',fg_color='#666A73',hover_color='#3C3D40',command=self.Generate_Passworld).pack(side="left", padx=10)
        self.copy_button = ctk.CTkButton(self.frame,text='Copy',fg_color='#666A73',hover_color='#3C3D40',command=self.Copy).pack(side='right')
        self.frame.pack(pady=(20,40))
        
      
    def Switch_Slider_Current_Value(self,*args):
        vL1 =f'Passworld Lenght: {int(self.slider.get())}'
        self.l1.configure(text = vL1)
    
    def Generate_Passworld(self):
        self.p_entry.configure(state='normal')
        self.p_entry.delete(0,ctk.END)
        self.p_entry.insert(0,gen(int(self.slider.get()),self.vars))
        self.p_entry.configure(width=((self.slider.get()*10)+12) if self.p_entry.get() != "" else None, state='disabled')
    def Copy(self):
        value = self.p_entry.get()
        copy(value)
        
