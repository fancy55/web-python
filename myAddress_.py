import tkinter
import MySQLdb as db

dbs = db.connect('localhost', '用户名', '密码', '数据库', charset='utf8')
cursor = dbs.cursor()

def goBack1(win,con):
    con.destroy()
    win.deiconify()

def goBack2(win,con):
    win.destroy()
    con.destroy()
    win_ = tkinter.Tk()
    default(win_)

def modify(win,con,name,newName,newPhone):  # 修改联系人信息（原名字，新名字，新电话号码）
    insert_update_delete("update user set phone = '%s' where name = '%s'" % (newPhone, name))
    goBack2(win,con)

def delete(win,con,name):
    insert_update_delete("delete from user where name = '%s'" % (name))
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

def saveContact(win,con,name,phone,body):
    newName = name.get()
    newPhone = phone.get()
    # print(newName, newPhone, "====")
    insert_update_delete("insert into user(name,phone) values ('%s', '%s')" % (newName, newPhone))
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
    l = select("select * from user")
    if l != None:
        for k, v in l.items():
            print(k,v)
            mylist(win, k, body)

def select(sql):
    dict_ = {}
    try:
       cursor.execute(sql)
       results = cursor.fetchall()
       for row in results:
           name = row[1]
           phone = row[2]
           dict_[name] = phone
           print("name= %s ,phone= %s " % (name, phone))
    except:
       print("select err")
       dbs.rollback()
    return dict_

def insert_update_delete(sql):
    try:
        cursor.execute(sql)
        dbs.commit()
    except:
        print("err")
        dbs.rollback()

def main():
    win = tkinter.Tk()
    default(win)

if __name__ == '__main__':
    main()