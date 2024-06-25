from tkinter import ttk
import tkinter as t
c=t.Tk()
a=t.IntVar()
b=t.IntVar()
cv=t.IntVar()
r=t.IntVar()
c.geometry('600x450')
c.title('Employee Entry Form')
c.resizable(0,0)

def show():
    s=''
    s1=''
    name=ename.get()
    if a.get()==1:
        s=s+c1.cget('text')
    if b.get()==1:
        if len(s)!=0:
            s=s+','
        s=s+c2.cget('text')
    if cv.get()==1:
        if len(s)!=0:
            s=s+','
        s=s+c3.cget('text')
    if r.get()==2:
        s1=rb1.cget('text')
    if r.get()==3:
        s1=rb2.cget('text')
    if r.get()==4:
        s1=rb3.cget('text')
    print('Employee Name:',name)
    print('Post:',s)
    print('Gender:',s1)
    print('State:',st.get())
    print('Address:',ad.get(1.0,'end-1c'))

def reset():
    ename.delete(0,t.END)
    ad.delete(1.0,'end-1c')
    # rb1.set(None)
    # rb2.set(None)
    # rb3.set(None)
    # c1.set(0)
    # c2.set(0)
    # c3.set(0)

    

t.Label(c,text='Employee Name',font=('bold',14)).place(x=20,y=30)
ename=t.Entry(c,width=30,font=('bold',14))
ename.place(x=200,y=35)
t.Label(c,text='Post',font=('bold',14)).place(x=20,y=80)
c1=t.Checkbutton(c,text='Analyst',font=('bold',10),variable=a,onvalue=1,offvalue=0)
c1.place(x=140,y=80)
c2=t.Checkbutton(c,text='Manager',font=('bold',10),variable=b,onvalue=1,offvalue=0)
c2.place(x=240,y=80)
c3=t.Checkbutton(c,text='Executive',font=('bold',10),variable=cv,onvalue=1,offvalue=0)
c3.place(x=340,y=80)
t.Label(c,text='Gender',font=('bold',14)).place(x=20,y=120)
rb1=t.Radiobutton(c,text='Male',font=('bold',10),value=2,variable=r)
rb1.place(x=140,y=120)
rb2=t.Radiobutton(c,text='Female',font=('bold',10),value=3,variable=r)
rb2.place(x=240,y=120)
rb3=t.Radiobutton(c,text='Binary',font=('bold',10),value=4,variable=r)
rb3.place(x=340,y=120)
t.Label(c,text='State',font=('bold',14)).place(x=20,y=160)
st=ttk.Combobox(c,width=52,font=('bold',10))
st['values']=('Bihar','UP','MP','Jharkhand','Assam')
st.place(x=145,y=160)
t.Label(c,text='Address',font=('bold',14)).place(x=20,y=200)
ad=t.Text(c,font=('bold',14),width=35,height=5)
ad.place(x=145,y=210)
b1=t.Button(c,text='Submit',command=show,font=('bold',14),fg='green',width=16)
b1.place(x=140,y=350)
b2=t.Button(c,text='Reset',command=reset,font=('bold',14),fg='red',width=16)
b2.place(x=350,y=350)

c.mainloop()




