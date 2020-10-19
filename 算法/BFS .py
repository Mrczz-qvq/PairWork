import numpy as np
import random
import requests
import json
import os
import base64
from Image import function
from pin import get_matrix

class Generator:

    def __init__(self, map, deep, fin_map):

        self.n=3  #棋盘阶数
        self.N=self.n*self.n  #棋盘中棋子个数（包含空格）
        self.dict={}  #用于判重 and 保存状态（key：状态， value：步数）
        self.dict_path={} #保存路径（key：状态，value：路径）
        self.que_qi=[]  #用于广度优先搜索中，辅助队列(存储棋盘)
        self.que_bk=[]  #用于广度优先搜索中，辅助队列（存储空格）
        self.que_lv=[]  #用于广度优先搜索中，辅助队列（存储层数）
        self.que_path = [] 
        self.orig_bk = 0
        self.end = 0
        self.ans = ''
        self.fin_map = ''
        self.deep=deep  #遍历深度
        self.directions = ['a', 'w', 's', 'd']
        self.qi_init=""  #初始棋盘布局

        for list in map:
            for num in list:
                self.qi_init += str(num)
        for list in fin_map:
            for num in list:
                self.fin_map += str(num)
        for index in range(0, 9):
            if self.qi_init[index] == '0':
                self.orig_bk = index
                break
    

    def move(self,qi,blank,dire,level, path):

        add = 0
        if dire == 'a':
            add = -1
        elif dire == 'w':
            add = -(self.n)
        elif dire == 's':
            add = self.n
        elif dire == 'd':
            add = 1
         
        x = blank + add

        if x<0 or x>=self.N or blank==x:
            return False

        if abs(blank%self.n-x%self.n)>1:
            return False
        if blank<x:
            temp=qi[:blank]+qi[x]+qi[blank+1:x]+qi[blank]+qi[x+1:]
        else:
            temp=qi[:x]+qi[blank]+qi[x+1:blank]+qi[x]+qi[blank+1:]
        if temp in self.dict:
            return False

        self.dict[temp]=level+1
        self.dict_path[temp] = path + dire
        self.que_qi=[temp]+self.que_qi
        self.que_bk=[x]+self.que_bk
        self.que_lv=[level+1]+self.que_lv
        self.que_path=['{0}{1}'.format(path, dire)]+self.que_path

        if temp == self.fin_map:
            self.end = 1
            self.ans = '{0}{1}'.format(path, dire)
        return True

    def bfs(self):  #广度优先搜索

        self.que_qi=[self.qi_init]+self.que_qi
        self.que_bk=[self.orig_bk]+self.que_bk
        self.que_lv=[0]+self.que_lv
        self.que_path =[''] + self.que_path
        self.dict[self.qi_init]=0
        self.dict_path[self.qi_init]=''

        lv=0

        while lv<self.deep and self.que_qi!=[]:
            qi=self.que_qi.pop()
            bk=self.que_bk.pop()
            lv=self.que_lv.pop()
            path = self.que_path.pop()
            for direction in self.directions:
                self.move(qi, bk, direction, lv, path)    
            if self.end == 1:
                break    
                      
def getreVersNum(num_list):
        sum=0
        for i in range(0,len(num_list)):
            if(num_list[i]==0):
                continue
            else:
                for j in range(0,i):
                    if(num_list[j]>num_list[i]):
                        sum+=1
        return sum

def judge(target, origate):
    targetVer=getreVersNum(target)
    orinateVer=getreVersNum(origate)
    if(targetVer%2!=orinateVer%2):
        return False
    else:
        return True

def random_exc(vec1, vec2):
    for i in range(0, 9):
        for j in range(i+1, 9):
            a = vec1[i]
            b = vec1[j]
            vec1[i] = b
            vec1[j] = a
            if judge(vec1, vec2):
                return [i, j]
            else:
                vec1[i] = a
                vec1[j] = b
    return [0, 0]

#网路接口：获取赛题数据
json_url = 'http://47.102.118.1:8089/api/challenge/start/e9d5727c-57fa-4182-a1fd-24b43fd392ce'
data = json.dumps({
    "teamid": 48,
    "token": "396e1989-984d-4777-98fa-1907fd2072bf"
})
r=requests.post(json_url, data=data, headers={'Content-Type': 'application/json'})
file_requests = r.json()
with open('data.json', 'w') as f_obj:
    json.dump(file_requests, f_obj)

#原图片分割
imgstr = (file_requests['data'])['img']
imgdata = base64.b64decode(imgstr)
with open('1.jpg', 'wb') as f_obj:
    f_obj.write(imgdata) 
function('1.jpg')

#初始数据生成
orig_map = get_matrix()
step = (file_requests['data'])['step']
swap = (file_requests['data'])['swap']
swap_free = []
fin_ans = ''

num_record = []
for List in orig_map:
    for num in List:
        num_record.append(num)
fin_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for index in range(0, 9):
    if index+1 in num_record:
        fin_map[index//3][index%3] = index+1

#算法核心
gen = Generator(orig_map, step, fin_map)
gen.bfs()

if gen.end == 1:
    fin_ans = gen.ans

else:
    path_dict = {}
    for key, value in gen.dict.items():
        if value == step:
            Map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for index in range(0, 9):
                Map[index//3][index%3] = int(key[index])
            ax = (swap[0]-1)//3
            ay = (swap[0]-1)%3
            bx = (swap[1]-1)//3
            by = (swap[1]-1)%3
            temp = Map[ax][ay]
            Map[ax][ay] = Map[bx][by]
            Map[bx][by] = temp
            map_str = ''
            for list in Map:
                for num in list:
                    map_str += str(num)
            path_dict[map_str] = gen.dict_path[key]
    
    dict_have = {}
    dict_none = {}
    for key, value in path_dict.items():        
        vec1 = []
        for letter in key:
            vec1.append(int(letter))
        vec2 = []
        for num_list in fin_map:
            for num in num_list:
                vec2.append(num)

        if judge(vec1, vec2):
            dict_have[key] = value

        else:
            dict_none[key] = value

    if len(dict_have) != 0:
        for key, value in dict_have.items():
            vec1 = []
            for letter in key:
                vec1.append(int(letter))
            vec2 = []
            for num_list in fin_map:
                for num in num_list:
                    vec2.append(num)
            Map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for index in range(0, 9):
                Map[index//3][index%3] = vec1[index]
            hen=Generator(Map, 50, fin_map)
            hen.bfs()
            fin_ans = '{0}{1}'.format(value, hen.ans)
            break
    else:
        for key, value in dict_none.items():
            vec1 = []
            for letter in key:
                vec1.append(int(letter))
            vec2 = []
            for num_list in fin_map:
                for num in num_list:
                    vec2.append(num)
            temp_swap = random_exc(vec1, vec2)
            if temp_swap[0] == temp_swap[1]:
                continue
            else:
                Map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                for index in range(0, 9):
                    Map[index//3][index%3] = vec1[index]
                hen=Generator(Map, 100, fin_map)
                hen.bfs()
                swap_free = [temp_swap[0]+1, temp_swap[1]+1]
                fin_ans = '{0}{1}'.format(value, hen.ans)
                break

print(fin_ans)
print(swap_free)

#网路接口：提交答案        
json_url2 = 'http://47.102.118.1:8089/api/challenge/submit'
data2 = json.dumps({
    "uuid": file_requests['uuid'],
    "teamid": 48,
    "token": "396e1989-984d-4777-98fa-1907fd2072bf",
    "answer": {
        "operations": fin_ans,
        "swap": swap_free
    }
})
r=requests.post(json_url2, data=data2, headers={'Content-Type': 'application/json'})
file_requests2 = r.json()
with open('return.json', 'w') as f_obj:
    json.dump(file_requests2, f_obj)            
