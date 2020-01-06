import sqlite3 as sq
import math as mt
import random as rd
import os

#识别目标的每个位置先采集进去，采集时手机放在原点

def cal(string):
    count = 0
    index = 0
    num = 0
    while (index < len(va1)):
        if ((string + str(int(h_v_dis / 10))) not in va1[index][3]):
            # print(string + str(int(h_v_dis / 10)))
            index = index + 1
            continue
        num = num + 1
        x = float(va1[index][0])
        y = float(va1[index][1])
        z = float(va1[index][2])
        pitch = rd.random() * mt.pi * 2
        roll = rd.random() * mt.pi * 2
        yaw = rd.random() * mt.pi * 2
        e_x = ((-mt.cos(yaw)) * mt.sin(roll) - mt.cos(roll) * mt.sin(pitch) * mt.sin(yaw)) * error
        e_y = (mt.cos(roll) * mt.cos(yaw) * mt.sin(pitch) - mt.sin(roll) * mt.sin(yaw)) * error
        e_z = (mt.cos(pitch) * mt.cos(roll)) * error
        if (string == "L" or string == "U"):
            hvdis = -h_v_dis
        else:
            hvdis = h_v_dis
        f_x = x + dis_o * mt.cos(mt.atan2(y, x) + h_v * mt.atan2(hvdis, dis)) + e_x * e_p
        f_y = y + dis_o * mt.sin(mt.atan2(y, x) + h_v * mt.atan2(hvdis, dis)) + e_y * e_p
        f_z = z + 0 + e_z * e_p
        # print(mt.atan2(y,x)*180/mt.pi + mt.atan2(h_dis,dis)*180/mt.pi)
        dis_a = pow(f_x - a, 2) + pow(f_y - b, 2) + pow(f_z - c, 2)
        dis_b = pow(f_x - q, 2) + pow(f_y - w, 2) + pow(f_z - e, 2)
        # print(string,mt.sqrt(dis_a)/10, mt.sqrt(dis_b)/10)

        if (dis_a < dis_b and (string == "L" or string == "U")):
            if (dis_a > pow(threshold, 2)):
                if (log == 1):
                    print(string, "out of search space", mt.sqrt(dis_a) / 10)
                index = index + 1
                continue
            count = count + 1
        elif (dis_a > dis_b and (string == "R" or string == "D")):
            if (dis_b > pow(threshold, 2)):
                if (log == 1):
                    print(string, "out of search space", mt.sqrt(dis_b) / 10)
                index = index + 1
                continue
            count = count + 1
        else:
            if (log == 1):
                print(string, "wrong object", mt.sqrt(dis_a) / 10, mt.sqrt(dis_b) / 10)
        index = index + 1
    return (float)((count - 1) / (num - 1))

#配置变量
r_th = 1000#识别率相差阈值
off_l = 0#偏移量
off_r = 0
#组合开始位置
l = 0
r = 0
l_f = l + off_l
r_f = r + off_r
h_v = 1#水平实验为1，垂直为0
hv_dis = 300#水平或者垂直距离，单位mm
e_p = 1#是否带入随机误差
lock_e = 0#是否在有误差时遍历
loop_e = (e_p == 1)*lock_e
lock = 1#是否遍历组合
loop = (loop_e == 0)*lock#是否遍历每种组合
loop_total = loop == 0 and e_p == 1 and loop_e == 1
log = 0#打印错误信息
error = 100#5cm长度随机方向误差
threshold = 335.3+error#搜索空间半径
#threshold = mt.sqrt(mt.pow(18+error, 2) + mt.pow(20+error, 2) + mt.pow(20+error, 2))
h_v_dis = hv_dis/2
dis_c = 0#是否带入距离
dis = 800#设备和识别目标的距离
dis_o = (1200 - dis) * dis_c#设备和原点的距离
#h_v=0,h_dis=5,dis=700
#上述值解释为水平实验，物体相距5*2cm，设备和识别目标连线中点垂直距离为700

os.chdir("C:\\Users\\70894\\Desktop\\recognize\\")

if(h_v == 1):
    path = str(dis) + "_h.db"
else:
    path = str(dis) + "_v.db"
#print(path)

conn1 = sq.connect(path)
cursor1 = conn1.cursor()
cursor1.execute('select world_x, world_y, world_z, ID from table1')
va1 = cursor1.fetchall()
cursor1.close()
'''
id = 0
while(id < len(va1)):
    s = va1[id][3]
    s_n = s[0:1]+s[2:len(s)]
    print(s_n)
    cursor2.execute("update table1 set ID = '%s' where ID='%s'" % (s_n, s))
    conn2.commit()
    id = id + 1
'''

#while("Test" not in va[i][3]):
#    i = i + 1
#fix_cor = [va[i][0], va[i][1], va[i][2]]
'''
原坐标有微小误差，原坐标的原点和识别目标的连线与标线不平行，但是难以修正，因为实验的时候手机是随即转动的，难以测量真实值
'''

if(h_v == 1):
    str1 = "L"
    str2 = "R"
else:
    str1 = "U"
    str2 = "D"
str3 = str1 + str(int(h_v_dis/10))
str4 = str2 + str(int(h_v_dis/10))
j = 0
k = 0
while (str3 not in va1[j][3]):
    j = j + 1
while (str4 not in va1[k][3]):
    k = k + 1
total = 0
sum = 0
flag_l = 1
flag_r = 1
while(flag_l == 1):
    while(flag_r == 1):
        while(1):
            while (1):
                if(j + l_f >= len(va1)):
                    flag_l = 0
                    flag_r = 0
                    break
                if (str3 not in va1[j + l_f][3]):
                    l_f = l_f + 1
                    off_l = off_l + 1
                    continue
                while(1):
                    if(k + r_f >= len(va1)):
                        flag_r = 0
                        break
                    #qw = i
                    if (str4 not in va1[k + r_f][3]):
                        r_f = r_f + 1
                        off_r = off_r + 1
                        continue
                    obj1 = [va1[j + l_f][0], va1[j + l_f][1], va1[j + l_f][2]]
                    obj2 = [va1[k + r_f][0], va1[k + r_f][1], va1[k + r_f][2]]
                    #er = i
                    a = float(obj1[0])
                    b = float(obj1[1])
                    c = float(obj1[2])
                    q = float(obj2[0])
                    w = float(obj2[1])
                    e = float(obj2[2])

                    r_l = round(cal(str1),2)
                    r_r = round(cal(str2),2)
                    avg = round((r_l+r_r)/2,2)
                    sum = sum + avg
                    if((l_f - off_l == r_f - off_r) and loop_total == 0):
                    #if(1 == 1 and loop_total == 0):
                    #if(loop_total == 0):
                        print(str1 + ":" + str(r_l) + " \t" + str2 + ":" + str(r_r) + " \tAvg:" + str(avg) + " \t", l_f - off_l, r_f - off_r)
                    if(loop == 0):
                        break
                    else:
                        r_f = r_f + 1
                if(loop == 0):
                    break
                else:
                    l_f = l_f + 1
                    off_r = 0
                    r_f = 0
            if(loop_e == 0 or total > 1000):
                break
            else:
                total = total + 1
                off_r = 0
                r_f = r
        if (loop_e == 1 and flag_r == 1):
            if(round(sum / total, 2) == 0.0):
                print()
            print("Avg:", round(sum / total, 2), l_f - off_l, r_f - off_r)
            total = 0
            sum = 0
            off_r = 0
        r = r + 1
        r_f = r
        if (loop_total == 0):
            break
    l = l + 1
    l_f = l
    r_f = 0
    r = 0
    off_r = 0
    flag_r = 1
    total = 0
    if(loop_total == 0):
        break

print("Horizontal\t" * h_v + "Vertical\t" * (h_v == 0), "Distance:" + str(dis/10) + "cm\t", "Dis_btw_obj:" + str(h_v_dis*2/10) + "cm\t", "Error:" + str(error*e_p/10) + "cm")