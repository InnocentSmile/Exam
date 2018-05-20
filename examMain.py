from tkinter import *
from tkinter import messagebox

from W6D2.connectRedis import connectredis
from W6D2.examMysql import pdao


class peopletest:
    def __init__(self):
        self.m=True
        self.index=0
        self.pcon =connectredis()
        self.pdao=pdao()
        self.klist = []
        self.vlist = []
        self.useranswer=[]
        self.gettimu()
        print(self.klist)
        print(self.vlist)
        self.window = Tk()
        self.F1()

    #准备试题的
    def gettimu(self):
        m,n=self.pcon.findExamAll()
        if m==None:
            self.klist,self.vlist=self.pdao.findAllExam()
            for i,j in zip(self.klist,self.vlist):
                self.pcon.addExamQ(i,j)
        else:
            self.klist, self.vlist=m,n

    def F1(self):

        self.window.title("考试系统登陆")
        self.frame1=Frame(self.window)
        self.frame1.pack()

        self.peoplename=StringVar()
        Label(self.frame1,text="用户名",width=10).grid(row=1,column=1)
        Entry(self.frame1,textvariable=self.peoplename).grid(row=1,column=2)

        self.peoplepassword=StringVar()
        Label(self.frame1,text="密码",width=10).grid(row=2,column=1)
        Entry(self.frame1,textvariable=self.peoplepassword,show='*').grid(row=2, column=2)

        Button(self.frame1,text="登陆",width=17,command=self.login).grid(row=3,column=1)
        Button(self.frame1,text="注册",width=19,command=self.register).grid(row=3,column=2)
        self.window.mainloop()
    def F2(self):


        self.window.title("注册界面")
        self.frame2 = Frame(self.window)
        self.frame2.pack()

        self.zhucename=StringVar()
        Label(self.frame2,text="请输入用户名").grid(row=1, column=1)
        Entry(self.frame2,textvariable=self.zhucename).grid(row=1, column=2)

        self.zhucpassword = StringVar()
        Label(self.frame2,text="请设置密码").grid(row=2,column=1)
        Entry(self.frame2,textvariable=self.zhucpassword,show='*').grid(row=2, column=2)

        self.zhucpassword2 = StringVar()
        Label(self.frame2,text="请重复密码").grid(row=3, column=1)
        Entry(self.frame2,textvariable=self.zhucpassword2,show='*').grid(row=3, column=2)

        Button(self.frame2,text="确定",width=15,command=self.confirm).grid(row=4,column=1)
        Button(self.frame2,text="返回",width=15,command=self.back).grid(row=4,column=2)
    def F3(self):

        self.window.title("考试界面")
        self.frame3 = Frame(self.window)
        self.frame3.pack()

        self.labelquestion=Label(self.frame3,width=60,height=10)
        self.labelquestion.grid(row=1,column=3)

        #******************************************垃圾代码区
        Label(self.frame3, text="").grid(row=2, column=3)
        Label(self.frame3, text="").grid(row=3, column=3)
        Label(self.frame3, text="").grid(row=4, column=3)
        Label(self.frame3, text="").grid(row=6, column=3)
        Label(self.frame3, text="").grid(row=7, column=3)
        Label(self.frame3, text="").grid(row=8, column=3)
        Label(self.frame3, text="").grid(row=9, column=3)
        # ************************************************

        self.startB=Button(self.frame3,text="下一题",width=10,command=self.next)
        self.startB.grid(row=5, column=6)

        Button(self.frame3, text="上一题",width=10,command=self.last).grid(row=5, column=1)

        self.labelquestion["text"] = self.klist[self.index]
        self.answer=StringVar()
        self.entry1 = Entry(self.frame3, width=20,textvariable=self.answer)
        self.entry1.grid(row=10, column=3)



    #下一个
    def next(self):
        # self.switchControls()
        if self.index<len(self.klist)-1:
            self.index+=1
            self.labelquestion["text"]=self.klist[self.index]

            if self.m==False:
                self.useranswer[self.index-1]=self.answer.get()
                self.answer.set("")
                self.m=True
                print("修改", self.useranswer)
            else:

                self.useranswer.append(self.answer.get())
                self.answer.set("")
                print("追加" ,self.useranswer)


        elif self.index==len(self.klist)-1:
            self.useranswer.append(self.answer.get())
            self.answer.set("")
            print("追加", self.useranswer)
            Button(self.frame3, text="交卷", width=10, command=self.submit).grid(row=11, column=6)

        print(self.index)
    #上一个
    def last(self):
        print(self.useranswer)
        self.m=False
        if self.index >0:
            self.index -= 1
            self.labelquestion["text"] = self.klist[self.index]
            self.answer.set(self.useranswer[self.index])
        print(self.index)


    #交卷算分逻辑
    def submit(self):

        print(self.useranswer)
        Count=0
        for i,j in zip(self.vlist,self.useranswer):
            if i==j:
                Count+=1
        Labelscore=Label(self.frame3,foreground="red",font=("黑体", 30, "bold"))
        Labelscore.grid(row=0, column=3)
        strscore=str(Count*10)
        Labelscore["text"]=strscore+"分"


    # def likecolor(self):
    #     colorStr = ""
    #     if self.v.get() == 1:
    #         colorStr = "A"
    #     elif self.v.get() == 2:
    #         colorStr = "B"
    #     elif self.v.get() == 3:
    #         colorStr = "C"
    #     elif self.v.get() == 4:
    #         colorStr = "D"
    #     return colorStr
    #
    # #根据答案来判断题型，显示不同的答题控件
    # def switchControls(self):
    #     if self.vlist[self.index] in ["A","B","C","D"]:
    #
    #         self.v = IntVar()
    #         self.rb3 = Radiobutton(self.frame3, text="A", variable=self.v, value=1, command=self.likecolor)
    #         self.rb4 = Radiobutton(self.frame3, text="B",  variable=self.v, value=2, command=self.likecolor)
    #         self.rb5 = Radiobutton(self.frame3, text="C",  variable=self.v, value=3, command=self.likecolor)
    #         self.rb6 = Radiobutton(self.frame3, text="D",  variable=self.v, value=4, command=self.likecolor)
    #
    #         self.rb3.grid(self.frame3,row=10, column=2)
    #         self.rb4.grid(self.frame3,row=10, column=3)
    #         self.rb5.grid(self.frame3,row=10, column=4)
    #         self.rb6.grid(self.frame3,row=10, column=5)
    #     else:
    #
    #
    #         self.entry1=Entry(self.frame3, width=20)
    #         self.entry1.grid(row=10, column=3)







    # 登录逻辑


    def login(self):
        name=self.peoplename.get()
        password=self.peoplepassword.get()
        rets=self.pcon.findUser(name)
        print(rets)
        if rets==None:
            rets2=self.pdao.findone(name)
            print(rets)
            if rets2==():
                messagebox.showinfo("提示信息", "登陆失败，用户不存在")
            else:
                if password == rets2[0][2]:
                    messagebox.showinfo("提示信息", "登陆成功，正跳转至考试界面")
                    self.pcon.addUser(name,password)
                    self.frame1.destroy()
                    self.F3()
                else:
                    messagebox.showinfo("提示信息", "密码错误")
        else:
            if rets==password:
                messagebox.showinfo("提示信息", "登陆成功，正跳转至考试界面")
                self.frame1.destroy()
                self.F3()
            else:
                messagebox.showinfo("提示信息", "密码错误")

    def back(self):
        self.frame2.destroy()
        self.F1()
    def register(self):
        self.frame1.destroy()
        self.F2()
    #注册逻辑
    def confirm(self):
        name=self.zhucename.get()
        password1=self.zhucpassword.get()
        password2=self.zhucpassword2.get()


        if name=="":
            messagebox.showinfo("提示信息", "用户名不能为空")
        else:
            # rets = self.pdao.findone(name)
            rets2=self.pcon.findUser(name)
            if  rets2 or self.pdao.findone(name)!=():
                messagebox.showinfo("提示信息", "用户名已存在")
            else:
                if password1=="" or password2=="":
                    messagebox.showinfo("提示信息", "密码为空，请输入密码")
                else:
                    if password1!=password2:
                        messagebox.showinfo("提示信息", "密码不一致")
                    else:
                        messagebox.showinfo("提示信息", "注册成功,跳转回考试界面")
                        self.pdao.addstudent(name,password1)
                        self.pcon.addUser(name,password1)
                        self.frame2.destroy()
                        self.F3()


if __name__ == '__main__':
    peopletest()