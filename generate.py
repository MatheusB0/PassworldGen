import random
import string
import tkinter.messagebox as msg
def gen(Len,Values):
    chars = list("")
    dic = {}
    for i,v in Values:
        dic[i] = v.get()
    if dic['Upper Letter (A-Z)']:
        chars += list(string.ascii_uppercase)
    if dic['Lower Letter (a-z)']:
        chars += list(string.ascii_lowercase)
    if dic['Numbers (0-9)']:
        chars += list(string.digits)
    if dic['Simbols (!@#$...)']:
        chars+= list("!@#$%&*?")
        
    if len(chars) > 1:
        return ''.join(random.choice(chars) for i in range(Len))
    else:
        return msg.showinfo("Invalid","Select at least one of the options") and ""
   
   