import pymysql



class pdao:

    def myconnect(self):
        conn = pymysql.connect(
            # 主机和端口
            host="127.0.0.1", port=3306,
            # 用户名和密码
            user="root", password="pzl123456",
            # 数据库和字符集
            database="contact", charset='utf8'
        )

        return conn

    def addstudent(self,name,pwd):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("insert into loginstu(name,pwd) values('%s',%s)" % (name,pwd))
        conn.commit()
        conn.close()


    def findone(self,name):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("select * from loginstu where name='%s'" % (name))
        ret = cursor.fetchall()
        # print(ret)
        conn.close()
        return ret
    def findAllExam(self):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("select * from examQ ")
        ret = cursor.fetchall()
        # print(ret)
        conn.close()
        klist=[]
        vlist=[]
        if ret:
            for i in range(len(ret)):
                klist.append(ret[i][1])
                vlist.append(ret[i][2])
            return klist,vlist
        else:
            return ret

if __name__ == '__main__':

    p=pdao()
    # ret=p.findAllExam()
    # print(ret)
    print(p.findone("shit"))