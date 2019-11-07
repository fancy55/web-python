import tkinter
from tkinter import messagebox as msg

cnt = 0

def goBack1(win,con):
    con.destroy()
    win.deiconify()

def goBack2(win,con):
    win.destroy()
    con.destroy()
    win_ = tkinter.Tk()
    default(win_)

def modify(win,con,name,newName,newPhone):  # 修改联系人信息（原名字，新名字，新电话号码）
    tp = 0
    r = open("card.txt", "r")
    lines = r.readlines()
    w = open("card.txt", "w")
    for line in lines:
        if 0 < tp < 2:
            tp = 0
            continue
        if line == name:
            tp += 1
            continue
        w.write(line)
    w.close()
    r.close()
    saveToTxt(newName,newPhone)
    goBack2(win,con)

def delete(win,con,name):
    tp = 0
    r = open("card.txt", "r")
    lines = r.readlines()
    w = open("card.txt", "w")
    for line in lines:
        if 0 < tp < 2:
            tp = 0
            continue
        if line == name:
            tp += 1
            continue
        w.write(line)
    w.close()
    r.close()
    goBack2(win,con)

def look(win,name):       # 查看信息
    win.withdraw()
    con = tkinter.Tk()
    con.title("联系人"+name)
    con.geometry("280x600")
    names, phones = newList(con)
    tkinter.Button(con, text="修改", width=40, command=lambda: modify(win,con,name,names.get(),phones.get())).place(x=0, y=60)
    tkinter.Button(con, text="删除", width=40, command=lambda: delete(win,con, name)).place(x=0,y=90)
    tkinter.Button(con, text="返回", width=40, command=lambda:goBack1(win,con)).place(x = 0, y = 120)

def mylist(win,name,body):    # 显示到主界面
    bt1 = tkinter.Button(body, text=name, width=40, command=lambda:look(win,name))
    bt1.grid()

def saveToTxt(name,phone):  # 存储到.txt
    f = open("card.txt", "a+")
    f.write(name + "\n")
    f.write(phone + "\n")
    f.close()

def saveContact(win,con,name,phone,body):
    newName = name.get()
    newPhone = phone.get()
    # print(newName, newPhone, "====")
    saveToTxt(newName, newPhone)
    con.destroy()
    win.deiconify()
    mylist(win,newName,body)

def newList(con): # 新增或修改显示的联系人页面
    tkinter.Label(con, text="name", width=10).place(x=1, y=0)
    name = tkinter.Entry(con, width=20)
    name.place(x=60, y=0)
    tkinter.Label(con, text="phone", width=10).place(x=1, y=30)
    phone = tkinter.Entry(con, width=20)
    phone.place(x=60, y=30)
    return name,phone

def addToList(win,body):
    global cnt
    cnt += 1
    win.withdraw()
    con = tkinter.Tk()
    name, phone = tkinter.StringVar(), tkinter.StringVar()
    con.title("新建联系人")
    con.geometry("280x600")
    name,phone = newList(con)
    tkinter.Button(con, text="新建", width=40, command=lambda:saveContact(win,con,name,phone,body)).place(x = 0, y = 60)
    tkinter.Button(con, text="返回", width=40, command=lambda: goBack1(win,con)).place(x=0, y=90)
    con.mainloop()

def default(win):
    win.title("通讯录")
    win.geometry("280x600")
    head = tkinter.Frame(height=30, width=280)
    body = tkinter.Frame(height=550, width=280)
    head.grid(row=0, column=0)
    body.grid(row=1, column=0)
    label = tkinter.Label(head, text="通讯录", width=10)
    show(win,body)
    add = tkinter.Button(head, text="+", width=5, command=lambda:addToList(win,body))
    label.grid(row=0, column=0)
    add.grid(row=0, column=1)
    win.mainloop()

def show(win,body):             #  先显示出文件中的联系人
    rs = open("card.txt","r")
    j = 0
    lines = rs.readlines()
    for line in lines:
        if j%2 == 0:
            mylist(win,line,body)
        j += 1
    rs.close()

def main():
    cnt = 0
    win = tkinter.Tk()
    default(win)


if __name__ == '__main__':
    main()