from dl_core.downloader import *
import tkinter.font as tkFont
# dl.dl_submit(username, int(b), int(e), passwd)

def togglePassInput():
    print(hasP.get())
    if hasP.get() == 1:
        Ls[3].config(state=tk.NORMAL)
        Es[3].config(state=tk.NORMAL)
    else:
        Ls[3].config(state=tk.DISABLED)
        Es[3].config(state=tk.DISABLED)

def submit2website():
    summitB.config(state=tk.DISABLED)
    if hasP.get() == 1:
        out2buffer('--------------------')
        try:
            dl_submit(Es[0].get(), int(Es[1].get()), int(Es[2].get()), Es[3].get())
        except:
            out2buffer('error')
            summitB.config(state=tk.NORMAL)
            return
    else:
        out2buffer('--------------------')
        try:
            dl_submit(Es[0].get(), int(Es[1].get()), int(Es[2].get()))
        except:
            out2buffer('error')
            summitB.config(state=tk.NORMAL)
            return
    out2buffer('username: \'' + Es[0].get() + '\' index ' + Es[1].get() + ' to ' + Es[2].get() + ' finished.')
    summitB.config(state=tk.NORMAL)
    

mainW.title('uxDownloader v1.0.0-alpha')
mainW.geometry('600x600')
labelFont = tkFont.Font(size=16)

hasP = tk.BooleanVar()

outF = tk.Frame(mainW)
outF.pack(padx=30, pady=30)
upperF = tk.LabelFrame(outF)
upperF.pack(padx=10, pady=10)
mainF = tk.LabelFrame(outF)
mainF.pack(padx=10, pady=10)
lowerF = tk.LabelFrame(outF)
lowerF.pack(padx=10, pady=10)
summitB = tk.Button(outF, text='Download all!', font=labelFont, command=submit2website)
summitB.pack(padx=10, pady=10)
summitB.config(state=tk.NORMAL)
outputL = tk.Label(outF, text='', relief=tk.SUNKEN, bg='white', width=70, height=8, anchor='nw', textvariable=outputBuf, justify=tk.LEFT)
outputL.pack(padx=10, pady=10)

passC = tk.Checkbutton(upperF, text='has password', font=labelFont, \
    variable=hasP, onvalue=True, offvalue=False, command=togglePassInput)
passC.pack()
passC.deselect()

inputFs = []
for i in range(4):
    inputFs.append(tk.Frame(mainF))
    inputFs[i].pack(padx=15, pady=15, anchor='e')

Ls = []
for i in range(4):
    Ls.append(tk.Label(inputFs[i], font=labelFont))
    Ls[i].pack(side=tk.LEFT)

Es = []
for i in range(4):
    Es.append(tk.Entry(inputFs[i], font=labelFont))
    Es[i].pack(side=tk.LEFT)

Ls[0].config(text='Target username :')
Ls[1].config(text='Download from index No. :')
Ls[2].config(text='To index No. :')
Ls[3].config(text='Password :')

Ls[3].config(state=tk.DISABLED)
Es[3].config(state=tk.DISABLED)

mainW.mainloop()