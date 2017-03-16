# -*- coding: utf-8 -*-
import datetime
import os
import random

 #自動スクリプター
def gpout(label, xlabel, ylabel, name1, name2):
    fgp = fileopen(name1+ "." + name2, ".gp") #スクリプトファイル
    #スクリプト生成処理
    str = "set grid" + "\n"
    str += "set title " + strpack(label) + "\n"
    str += "set xrange [0:1]" + "\n"
    str += "set yrange [0:1]" + "\n"
    str += "set xlabel " + strpack(xlabel) + "\n"
    str += "set ylabel " + strpack(ylabel) + "\n"
    #プロット(改行なし)
    str += "plot " + strpack(settype(name1, ".dat"))
    str += " with points ps 0.2"
    str += ", " + strpack(settype(name2, ".dat"))
    str += " with lines ps 0.2"
    str += "," + "x "
    str += " with lines"

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
    str = "{0:.3f}{1}{2:.3f}{3}".format(x, " ", nx, "\n") #データ整形
    return str


if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    r = float(input('r = ')) #グラフ変数r
    x0 = random.random() #初期値
    n = int(input("Calculate times:"))#計算回数
    p = int(input("Pass initial calculate times:"))#計算から省く回数
    if(n < p):
        print("ERROR:Calculate times is less than pass count")

    #ファイル名の設定
    name1 = "{0}{1:.2f}{2}{3}".format("Xn-X(n+1)_r=", r, "_n=", n)
    name2 = "{0}{1:.2f}{2}{3}".format("ReturnMap_r=", r, "_n=", n)

    #ファイルオープン
    f1 = fileopen(name1, ".dat") #n-Xnグラフ用出力ファイル
    f2 = fileopen(name2, ".dat") #n-Xnグラフ用出力ファイル
    gpout("{0}{1:.2f}".format ("r = ", r,), "Xn", "Xn+1", name1, name2)

    #計算
    nx = x = x0 #計算用初期値
    for i in range(n+1):
        if(i != 0):
            nx = r * (1 - x) * x #与式兼n+1項の値
        if(i > p):
            f1.write(plotout(x, nx))  #Xn-X(n+1)グラフ用プロットデータ
            f2.write(plotout(x, nx)) #リターンマップ用プロットデータ
        x = nx #リターンマップ用プロットデータ入力のための処理
        if(i > p):
            f2.write(plotout(x, nx))

    #ファイルクローズ
    f1.close()
    f2.close()