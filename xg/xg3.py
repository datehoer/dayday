import wave
import math
import struct
from os.path import exists
music = wave.open("music.wav","w")
music.setframerate(8000)
music.setnchannels(1)
music.setsampwidth(2)
 
# 音阶对应的频率
note = {  "1-":220,"2-":246.94,"3-":227.19,"4-":293.67,"5-":329.67,"6-":329.63,"7-":415.31,
        "1":440,"2":493.88,"3":554.37,"4":587.33,"5":659.33,"6":739.99,"7":830.61,
        "1+":880,"2+":987.76,"3+":1108.74,"4+":1174.66,"5+":1318.66,"6+":1479.98,"7+":1661.22,"0":0
}
 
# 节拍对应的时长
# #   1拍--0.1875   2拍--0.375    3拍--0.5625   4拍--0.75
interal = {
        0:0.02,1:0.1875,2:0.375,3:0.5625,4:0.75,5:0.9375,6:1.125
}
 
# 自定义写入音乐的函数
def wv(t=0,f=0,v=0.5,wf=music,sr=8000):
    '''
    t:写入时长
    f:声音频率
    v：音量
    wf：一个可以写入的音频文件
    sr：采样率
    '''
    tt = 0
    dt = 1.0/sr
    while tt <= t:
        s = math.cos(tt*math.pi*2*f)*v*32768 #采样，调节音量，映射到[-2^15,2^15)
        s = int(s)
        fd = struct.pack("h",s) #转换成8bit二进制数据
        wf.writeframes(fd) #写入音频文件
        tt += dt #时间流逝
if exists('data.txt'):
    with open('data.txt') as f: s = f.read()
    l = s.split()
    scales = []; beats = []
    for data in l:
        tmp = data.split('*')
        scale = tmp[0]
        beat = int(tmp[1])
        scales.append(scale)
        beats.append(beat)
else:
    # 简谱, 对应原来的n
    scales = [
            "6","0","6","0","6","0","6","3","6","7","1+","0","1+","0","1+","0",
            "1+","2+","5","4","3","0","2","0",
            "6","0","6","0","6","0","6","3","6","7","1+","0","1+","0","1+","0",
            "1+","2+","5","0","3","0","4","0","5","0","6","0","7","0",
            "1+","0","1+","0","1+","0","1+","6","1+","3+","0","4+","0","4+","0","4+","0",
            "4+","1+","3+","0","5","7","0","1+","0","2+","0","1+","0","7","0",
            "1+","0","1+","0","1+","0","1+","6","1+","3+","0","4+","0","4+","0","4+","0",
            "5+","0","4+","0","3+","1+","0","5","1+","3+","2+","0","2+","0","2+","0","3+","0","3+","0",
    ]
 
    # 与n数据相对应的节拍, 对应原来的tm
    beats = [
            3,0,1,0,5,0,1,1,1,1,3,0,1,0,5,0,
            2,2,5,4,4,0,6,4,
            3,0,1,0,5,0,1,1,1,1,3,0,1,0,5,0,
            2,2,5,2,2,0,2,0,2,0,5,0,5,0,
            3,0,1,0,5,0,1,1,1,1,0,3,0,1,0,5,0,
            2,2,5,2,2,2,0,2,0,5,0,4,0,4,0,
            3,0,1,0,5,0,1,1,1,1,0,3,0,1,0,5,0,
            2,0,2,0,4,4,2,2,2,2,5,0,1,0,1,0,2,0,5,0,
    ]
 
for i in range(len(scales)):
    wv(interal[beats[i]],note[scales[i]])
music.close()
