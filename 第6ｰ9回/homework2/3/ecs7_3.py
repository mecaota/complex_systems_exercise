# -*- coding: utf-8 -*-
import datetime
import os
import random
from sympy import *
import math

 #自動スクリプター
def gpout(label, xlabel, ylabel, name1, name2):
    fgp = fileopen(name1, ".gp") #スクリプトファイル
    #スクリプト生成処理
    str = "set grid" + "\n"
    str += "set title " + strpack(label) + "\n"
    str += "set xrange [0:1]" + "\n"
    str += "set yrange [0:1]" + "\n"
    str += "set xlabel " + strpack(xlabel) + "\n"
    str += "set ylabel " + strpack(ylabel) + "\n"
    #プロット(改行なし)
    str += "plot " + strpack(settype(name2, ".dat"))
    str += " with points pt 0.5 ps 0.2"
    str += "," + strpack(settype(name1, ".dat"))
    str += " with lines"
    str += "," + "x"
    str += " with lines"

    str += "\n" + "pause 2" + "\n"
    str += "set terminal png" + "\n"
    str +="set output " + strpack(settype(name1, ".png")) + "\n"
    str += "replot" + "\n"
    str += "set terminal x11"
    fgp.writelines(str)
    fgp.close()

#ロジスティック計算処理関数
def calnext(x, r):
    for i in range(3):
        x = r*x*(1 - x)
    result = x
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
    str = "{0:.6f}{1}{2:.6f}{3}".format(x, " ", nx, "\n") #データ整形
    return str

if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    x0 = random.random() #初期値
    n = 20000 #計算回数
    r = float(input('r = ')) #増加率r
    #r = 0;

    #ファイル名の設定
    name2 = "{0}{1:.4f}".format("r=", r) + "RetLogistic3"
    name1 = "{0}{1:.4f}".format("r=", r) + "ReturnMap3"

    #ファイルオープン
    f1 = fileopen(name1, ".dat") #n-Xnグラフ用出力ファイル
    f2 = fileopen(name2, ".dat") #n-Xnグラフ用出力ファイル
    gpout("{0}{1:.4f}".format("r = ", r,), "Xn", "X(n+1)", name1, name2)

    #計算
    x = xn = x0 #計算用初期値
    for j in range(n):
        xn = calnext(x, r) #与式兼n+1項の値
        if(250<=j and j<=500):
            f1.write(plotout(x, xn))  #Xn-X(n+1)グラフ用プロットデータ
            f1.write(plotout(xn, xn))  #Xn-X(n+1)グラフ用プロットデータ
        f2.write(plotout(x, xn))  #Xn-X(n+1)グラフ用プロットデータ
        x = xn #リターンマップ用プロットデータ入力のための処理

    #ファイルクローズ
    f1.close()
    f2.close()
