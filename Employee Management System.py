import mysql.connector as mys
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
global i
global z
global t
global l1
global q
global win
z=0

def submit():
    global win
    global l1
    global u
    global p
    global l
    u=uname.get()
    p=pname.get()
    global db
    db=mys.connect(host='localhost',user=u,passwd=p,database='frr_workplace')
    c=db.cursor()
    if db.is_connected==True:
        print('You have been connected to our database successfully!!')
    win=tk.Tk()
    win.title('Employee')
    win.geometry('1000x500')
    c.execute('select* from employee')
    i=1
    u=0
    t=[]
    l1=[]
    l=['EMP NO','Name','Department','Salary']
    for z in l:
        print(z)
        q=Label(win,text=z,foreground='red',width=25,borderwidth=2,relief='ridge',anchor="w")
        q.grid(row=0,column=u)
        u+=1
    for x in c:
        l1.append(x)
        
        for j in range(len(x)):
            e=Label(win,text=x[j],width=25,borderwidth=2,relief='ridge', anchor="w")
            e.grid(row=i,column=j)
            
        edi=Button(win,text='Edit',width=5, command=lambda i=i: editdat(i))
        edi.grid(row=i,column=j+1)
        dele=Button(win,text='Delete',width=10, command= lambda i=i: deldat(i))
        dele.grid(row=i,column=j+2)
        i=i+1
    p=Button(win,text='Add',width=10,command=adddat)
    p.grid(row=i+1,column=2)
    exp=Button(win,text='Export as CSV', width=15, command=export)
    exp.grid(row=i+2, column=2)
    win.mainloop()

def refresh():
    global db
    global win
    global l1
    c=db.cursor()
    if db.is_connected==True:
        print('You have been connected to our database successfully!!')
    win=tk.Tk()
    win.title('Employee')
    win.geometry('1000x500')
    c.execute('select* from employee')
    i=1
    u=0
    t=[]
    l1=[]
    l=['EMP NO','Name','Department','Salary']
    for z in l:
        print(z)
        q=Label(win,text=z,foreground='red',width=25,borderwidth=2,relief='ridge',anchor="w")
        q.grid(row=0,column=u)
        u+=1
    for x in c:
        l1.append(x)
        
        for j in range(len(x)):
            e=Label(win,text=x[j],width=25,borderwidth=2,relief='ridge', anchor="w")
            e.grid(row=i,column=j)
            
        edi=Button(win,text='Edit',width=5, command=lambda i=i: editdat(i))
        edi.grid(row=i,column=j+1)
        dele=Button(win,text='Delete',width=10, command= lambda i=i: deldat(i))
        dele.grid(row=i,column=j+2)
        i=i+1
    p=Button(win,text='Add',width=10,command=adddat)
    p.grid(row=i+1,column=2)
    exp=Button(win,text='Export as CSV', width=15, command=export)
    exp.grid(row=i+2, column=2)
    win.mainloop()

def export():
    global ut
    global xt
    xt=tk.Tk()
    xt.title('Export')
    xt.geometry('500x500')
    u=Label(xt,text='Enter the file name:',width=20).grid(row=1,column=1)
    ut=Entry(xt, width=20)
    ut.grid(row=1,column=2)
    sub=Button(xt,text='Export', width=10, command=lambda:[filexp(),xt.destroy()])
    sub.grid(row=2,column=2)

def filexp():
    global db
    import csv
    global xt
    global l
    x=ut.get()
    fh=open(x+'.csv','w')
    c=csv.writer(fh)
    cr=db.cursor()
    q='select * from employee;'
    cr.execute(q)
    result=cr.fetchall()
    c.writerow(l)
    for row in result:
        c.writerow(row)
    z=tk.messagebox.showinfo('Information Tile','The table has been successfully exported', parent=xt)

def deldat(i):
    global q
    global l1
    global nz,idz,sz,dz
    ad=tk.Tk()
    ad.title('Delete Values')
    ad.geometry('1000x400')
    z=0
    a=i-1
    print(a)
    q=l1[a]
    print(q)
    for x in q:
        e=Label(ad,text=x,width=25,borderwidth=2, relief='ridge',anchor='w')
        e.grid(row=0,column=z)
        z+=1
    sub=Button(ad,text='Delete',command=lambda:[listy3(),ad.destroy(),destroy_window()])
    sub.place(x=40,y=250)
    ad.mainloop()

def listy3():
    global db
    global q
    print(q[0])
    cur=db.cursor()
    o="delete from employee where EMP_NO={}".format(q[0])
    cur.execute(o)
    db.commit()
    print('Row has been successfully deleted.')

def adddat():
    global z
    global n1,id1,s1,d1
    ed=tk.Tk()
    ed.title('Add Values')
    ed.geometry('1000x500')
    n=Label(ed,text='Enter name:').place(x=40,y=50)
    n1=Entry(ed,width=30)
    n1.place(x=200,y=50)
    id0=Label(ed,text='Enter id:').place(x=40,y=100)
    id1=Entry(ed,width=30)
    id1.place(x=200,y=100)
    s=Label(ed,text='Enter salary:').place(x=40,y=150)
    s1=Entry(ed,width=30)
    s1.place(x=200,y=150)
    d=Label(ed,text='Enter department:').place(x=40,y=200)
    d1=Entry(ed,width=30)
    d1.place(x=200,y=200)
    sub=Button(ed,text='Add',command=lambda: [valget(),ed.destroy(),destroy_window()])
    sub.place(x=40,y=250)
    ed.mainloop()

def valget():
    global t
    import random
    n2=n1.get()
    id2=id1.get()
    s2=s1.get()
    d2=d1.get()
    if len(n2)==0:
        n2='NULL'
        print(n2)
    if len(id2)==0:
        id2=random.randint(1000,10000)
        print(id2)
    if len(s2)==0:
        s2='NULL'
        print(s2)
    if len(d2)==0:
        d2='NULL'
        print(d2)
    t=(id2,n2,d2,s2)
    print(t)
    listy()   

def listy():
    global t
    global db
    cur=db.cursor()
    q='insert into employee(EMP_NO,Name,Department,Salary) values({},"{}","{}",{})'.format(t[0],t[1],t[2],t[3])
    cur.execute(q)
    db.commit()
    print('data entered successfully!!')

def destroy_window():
    global win
    win.destroy()
    refresh()
    
def editdat(i):
    global q
    global l1
    global nt,idt,st,dt
    ad=tk.Tk()
    ad.title('Edit Values')
    ad.geometry('1000x400')
    z=0
    a=i-1
    print(a)
    q=l1[a]
    print(q)
    for x in q:
        e=Label(ad,text=x,width=25,borderwidth=2, relief='ridge',anchor='w')
        e.grid(row=0,column=z)
        z+=1
    n=Label(ad,text='Change name:').place(x=40,y=50)
    nt=Entry(ad,width=30)
    nt.place(x=200,y=50)
    id0=Label(ad,text='Change id:').place(x=40,y=100)
    idt=Entry(ad,width=30)
    idt.place(x=200,y=100)
    s=Label(ad,text='Change salary:').place(x=40,y=150)
    st=Entry(ad,width=30)
    st.place(x=200,y=150)
    d=Label(ad,text='Change department:').place(x=40,y=200)
    dt=Entry(ad,width=30)
    dt.place(x=200,y=200)
    sub=Button(ad,text='Edit',command=lambda:[valget2(),ad.destroy(),destroy_window()])
    sub.place(x=40,y=250)
    ad.mainloop()

def valget2():
    global q
    global p1
    n2=nt.get()
    id2=idt.get()
    s2=st.get()
    d2=dt.get()
    if len(n2)==0:
        n2=q[1]
        print(n2)
    if len(id2)==0:
        id2=q[0]
        print(id2)
    if len(s2)==0:
        s2=q[3]
        print(s2)
    if len(d2)==0:
        d2=q[2]
        print(d2)
    p1=(id2,n2,d2,s2)
    print(p1)
    listy2()

def listy2():
    global db
    global p
    global q
    print(q[0])
    cur=db.cursor()
    o="update employee set EMP_NO={},Name='{}',Department='{}',Salary={} where EMP_NO={}".format(p1[0],p1[1],p1[2],p1[3],q[0])
    cur.execute(o)
    db.commit()
    print('Row has been successfully updated.')
        
root=tk.Tk()
root.title('FRR-Employee Management System')
root.geometry('500x500')
u1=Label(root,text='username').place(x=40,y=60)
p1=Label(root,text='password').place(x=40,y=100)
submit=Button(root,text='submit',command=submit)
submit.place(x=40,y=130)
uname=Entry(root,width=30)
uname.place(x=110,y=60)
pname=Entry(root,width=30)
pname.place(x=110,y=100)

root.mainloop()
