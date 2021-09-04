#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import copy
import sys



dictInterestCate ={
    "寵物" : ["娛樂", "生活"],
    "球類運動" : ["體育"],
    "健身健康" : ["體育", "生活"],
    "教育" : ["教育"],
    "心靈成長" : ["教育", "情感"],
    "音樂" : ["藝文", "娛樂"],
    "美食" : ["生活"],
    "旅遊遊記" : ["生活"],
    "電子遊戲" : ["ACG"],
    "桌上/實境遊戲" : ["ACG"],
    "動畫/漫畫/cosplay/二次元相關" : ["ACG"],
    "Youtuber/網紅/實況主/Vtuber" : ["娛樂"],
    "好書推薦" : ["生活", "藝文"],
    "理財投資" : ["財經"],
    "電影" : ["娛樂"],
    "影集戲劇" : ["娛樂"],
    "國際政經" : ["財經", "時事"],
    "時事評論" : ["議題", "時事"],
    "娛樂八卦" : ["娛樂"],
    "行銷/管理" : ["科技", "教育"],
    "科技趨勢" : ["科技"],
    "創新創業" : ["教育", "職場"],
    "職場關係" : ["職場"],
    "情感關係" : ["情感"],
    "生活/人文" : ["生活", "藝文"],
    "表演展覽" : ["生活", "藝文"],
    "美妝穿搭" : ["娛樂"],
    "手工藝" : ["藝文", "娛樂"],
    "神秘占卜" : ["藝文"],
    "法律" : ["時事"]
}


dictIntestMap={
    0: '影集戲劇', 
    1: '國際政經', 
    2: '時事評論', 
    3: '娛樂八卦', 
    4: '行銷/管理', 
    5: '科技趨勢', 
    6: '創新創業', 
    7: '職場關係', 
    8: '情感關係', 
    9: '生活/人文', 
    10: '表演展覽', 
    11: '美妝穿搭', 
    12: '手工藝', 
    13: '神秘占卜', 
    14: '法律', 
    15: '寵物', 
    16: '球類運動', 
    17: '健身健康', 
    18: '教育', 
    19: '心靈成長', 
    20: '音樂', 
    21: '美食', 
    22: '旅遊遊記', 
    23: '電子遊戲', 
    24: '桌上/實境遊戲', 
    25: '動畫/漫畫/cosplay/二次元相關', 
    26: 'Youtuber/網紅/實況主/Vtuber', 
    27: '好書推薦', 
    28: '理財投資', 
    29: '電影'
    }



def getTtlCateCount (dictInterestCate):
    dictTtlCateCount = {}
    for interest in dictInterestCate:
        for cate in dictInterestCate[interest]:
            if cate not in dictTtlCateCount:
                dictTtlCateCount[cate] =1
            else:
                dictTtlCateCount[cate] +=1
    return dictTtlCateCount
                



def getIniUserCateCnt(dictTtlCateCount):
    dictIniUserCate = {}
    for cate, count in dictTtlCateCount.items():
        dictIniUserCate[cate] =0
    return dictIniUserCate  

def getIniUserCateScore(dictTtlCateCount):
    dictIniUserCate = {}
    for cate, count in dictTtlCateCount.items():
        dictIniUserCate[cate] =0
    return dictIniUserCate  
            


def getUserCate(userInterestArray, dictInterestCate, dictIntestMap, dictIniUserCate):
    for interestNo in userInterestArray:
        interest = dictIntestMap[interestNo]
        for cate in dictInterestCate[interest]:
            dictIniUserCate[cate]+=1             
    return  dictIniUserCate


def getUserScore(dictUserCateCnt, dictTtlCateCount, dictIniUserCateScore):
    listCates = dictUserCateCnt.keys()
    for cate in listCates :
        dictIniUserCateScore[cate] = round(dictUserCateCnt[cate]/dictTtlCateCount[cate]*7)
       
    return dictIniUserCateScore


def main(argv):
    userInterestArray = []
    for i in range(1,len(argv)):
        userInterestArray.append(int(argv[i]))
    print("userInterestArray: ", userInterestArray)
    
    dictTtlCateCount = getTtlCateCount(dictInterestCate)  
             
    dictIniUserCateCnt = getIniUserCateCnt(dictTtlCateCount) 
    
    
    dictIniUserCateScore = getIniUserCateScore(dictTtlCateCount)  
    dictUserCateCnt = getUserCate(userInterestArray, dictInterestCate, dictIntestMap, dictIniUserCateCnt)
    dictUserScore = getUserScore(dictUserCateCnt, dictTtlCateCount, dictIniUserCateScore)
    print("dictUserScore: ", dictUserScore)
    return dictUserScore


if __name__ == '__main__':
    main(sys.argv)








