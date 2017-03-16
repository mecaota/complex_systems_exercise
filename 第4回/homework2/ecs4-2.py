# -*- coding: utf-8 -*-
import datetime
import os
import random
from sympy import *
import math

 #自動スクリプター
def gpout(label, xlabel, ylabel, name1):
    fgp = fileopen(name1, ".gp") #スクリプトファイル
    #スクリプト生成処理
    str = "set grid" + "\n"
    str += "set title " + strpack(label) + "\n"
    str += "set xrange [3.825:3.86]" + "\n"
    str += "set yrange [-1:0.4]" + "\n"
    str += "set xlabel " + strpack(xlabel) + "\n"
    str += "set ylabel " + strpack(ylabel) + "\n"
    #プロット(改行なし)
    str += "plot " + strpack(settype(name1, ".dat"))
    str += " with points pt 0.5 ps 0.2"

    str += "\n" + "pause 2" + "\n"
    str += "set terminal png" + "\n"
    str +="set output " + strpack(settype(name1, ".png")) + "\n"
    str += "replot" + "\n"
    str += "set terminal x11"
    fgp.writelines(str)
    fgp.close()

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
    str = "{0:.5f}{1}{2:.5f}{3}".format(x, " ", nx, "\n") #データ整形
    return str

if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    r = 3.825 #増加率r
    x0 = random.random() #初期値
    x = Symbol('x')
    n = 1000 #計算回数
    rmd = 0

    #ファイル名の設定
    name1 = "{0}{1:.2f}".format("r=", r) + "Lyspunov"

    #ファイルオープン
    f1 = fileopen(name1, ".dat") #n-Xnグラフ用出力ファイル
    gpout("{0}{1:.4f}".format("r = ", r,), "r", "lyspunov exponent", name1)

    #計算
    while(r <= 3.86):
        nx = x = x0 #計算用初期値
        sum = 0;
        for j in range(n):
            if(j != 0):
                nx = r * (1 - x) * x #与式兼n+1項の値
            if(j > n * 0.1):
                rmd = rmd + math.log(math.fabs(r*(-2*x+1)))/n
            x = nx #リターンマップ用プロットデータ入力のための処理
        f1.write(plotout(r, rmd))  #Xn-X(n+1)グラフ用プロットデータ
        rmd = 0
        r += 0.00001 #rに足していく為の処理

    #ファイルクローズ
    f1.close()