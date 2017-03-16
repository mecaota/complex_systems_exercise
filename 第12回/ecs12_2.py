# -*- coding: utf-8 -*-
import datetime
import os
import random
from sympy import *
import numpy as np
import math

 #自動スクリプター
def gpout(label, xlabel, ylabel, name1, name2):
    fgp = fileopen(name2, ".gp") #スクリプトファイル
    #スクリプト生成処理
    str = "set grid" + "\n"
    str += "set title " + strpack(label) + "\n"
    str += "set xrange [0:2]" + "\n"
    str += "set yrange [0:1000000]" + "\n"
    str += "set xlabel " + strpack(xlabel) + "\n"
    str += "set ylabel " + strpack(ylabel) + "\n"
    #プロット(改行なし)
    str += "plot " + strpack(settype(name2, ".dat"))
    str += " using 1:2 with lp notitle"

    str += "\n" + "pause 2" + "\n"
    str += "set terminal png" + "\n"
    str +="set output " + strpack(settype(name2, ".png")) + "\n"
    str += "replot" + "\n"
    str += "set terminal x11"
    fgp.writelines(str)
    fgp.close()

#ロジスティック計算処理関数
def calnext(x, r):
    result = r*x*(1 - x)
    return result

#投げた文字列を””で囲い込んでしまう恐ろしい関数
def strpack(str):
    c = '"'
    str = c + str + c
    return str

#拡張子付きファイル名生成
def settype(name, type):
    filename = name + type #ファイル名
    return filename

#ファイルオープン処理
def fileopen(filename, type):
    filename = settype(filename, type) #拡張子付きファイル名
    f = open(filename, 'w', encoding = "UTF-8")
    return f

#プロットデータ整形処理
def plotout(x, nx):
    str = "{0:.3f}{1}{2:.3f}{3}".format(x, " ", nx, "\n") #データ整形
    return str

if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    x0 =0.7 #初期値
    n = 1000 #計算回数
    #r = float(input('r = ')) #増加率r
    a = 1.4
    b = 0.3
    r = 0
    
    result_x = np.zeros(n) #プロットデータ保存用の配列
    result_y = np.zeros(n) #プロットデータ保存用の配列
    hist = np.zeros(200)

    #ファイル名の設定
    name2 = "{0}{1:.4f}".format("r=", r) + "Hist-sum"
    name1 = "{0}{1:.4f}".format("r=", r) + "Henon_hist"

    #ファイルオープン
    f1 = fileopen(name1, ".dat") #n-Xnグラフ用出力ファイル
    f2 = fileopen(name2, ".dat") #hist compグラフ用出力ファイル
    gpout("{0}{1:.4f}".format("r = ", r,), "r", "C", name1, name2)

    #計算
    x = xn = y = yn = x0 #計算用初期値
    for j in range(n):
        xn = y + 1 - a*x*x
        yn = b*x
        result_x[j]=xn
        result_y[j]=yn
        x = xn #リターンマップ用プロットデータ入力のための処理
        y = yn
        sum = 0
    for i in range(n-2):
        for j in range(n-1):
            dist = math.sqrt((result_x[i]-result_x[j])*(result_x[i]-result_x[j]) + (result_y[i]-result_y[j]) * (result_y[i]-result_y[j]) )
            m = math.floor(dist/0.01)
            if m<200:
                hist[m]+=1
    for i in range(hist.size):
        sum = sum + hist[i]
        f1.write(plotout(i/100, hist[i]))  #Xn-X(n+1)グラフ用プロットデータ
        f2.write(plotout(i/100, sum))
    #ファイルクローズ
    f1.close()
    f2.close()