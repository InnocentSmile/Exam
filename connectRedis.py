import redis


class connectredis():
    def __init__(self):
        self.client = redis.StrictRedis(
            host='localhost', port=6379, db=1,

        )


    def findUser(self,name):

        hget=self.client.hget("pUser",name)

        if hget:
            return hget.decode("utf-8")
        else:
            return None

    def addUser(self,name,pwd):

        pipe = self.client.pipeline(transaction=True)
        ret=pipe.hset("pUser",name,pwd)
        pipe.execute()
        return ret
    def addExamQ(self,Q,A):
        pipe = self.client.pipeline(transaction=True)
        ret=pipe.hset("pExam",Q,A)
        pipe.execute()
        return ret
    def findExamAll(self):

        examdict = self.client.hgetall("pExam")
        klist=[]
        vlist=[]
        print(examdict)
        if examdict=={}:
            return None, None
        else:
            for k,v in examdict.items():
                klist.append(k.decode("utf-8"))
                vlist.append(v.decode("utf-8"))
            return klist,vlist

if __name__ == '__main__':
    mycon=connectredis()
    print(mycon.findUser("pzl"))
    # print(mycon.addUser("pzl","123456"))
    klist,vlist=mycon.findExamAll()
    print(klist)
    print(vlist)




































