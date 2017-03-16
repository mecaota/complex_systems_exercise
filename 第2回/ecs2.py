# -*- coding: utf-8 -*-
import datetime
import os

 #自動スクリプター
def gpout(label, xlabel, ylabel, name):
    fgp = fileopen(name, ".gp") #スクリプトファイル
    #スクリプト生成処理
    str = "set grid" + "\n" 
    str += "set title " + strpack(label) + "\n" 
    str += "set xrange [0:1]" + "\n" 
    str += "set yrange [0:1]" + "\n" 
    str += "set xlabel " + strpack(xlabel) + "\n"
    str += "set ylabel " + strpack(ylabel) + "\n"
    str += "plot " + strpack(settype(name, ".dat")) + "\n"
    str += "with points pt 5 ps 0.2"
    #str += "with lines"
    str += "\n" + "pause 2" + "\n"
    str += "set terminal png" + "\n"
    str +="set output " + strpack(settype(name, ".png")) + "\n"
    str += "replot" + "\n"
    str += "set terminal x11"
    fgp.writelines(str)
    fgp.close()

#投げた文字列を””で囲い込んでしまう恐ろしい関数
def strpack(str):
    c = '"'
    str = c + str + c
    return str

#ファイル名生成
def setname(name, r):
    filename = "{0}{1:.2f}".format(name, r) #ファイル名
    return filename

#拡張子付きファイル名生成
def settype(name, type):
    filename = name + type #ファイル名
    return filename

#ファイルオープン処理
def fileopen(filename, type):
    filename = settype(filename, type) #拡張子付きファイル名
    f = open(filename, 'w', encoding="UTF-8")
    return f

#プロットデータ整形処理
def strout(x, nx):
    str = "{0:.3f}{1}{2:.3f}{3}".format(x, " ", nx, "\n") #データ整形
    return str


if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    r = float(input('r = ')) #グラフ変数r
    x0 = 0 #初期値
    n = 200#計算回数
    max = 1 #最大値格納変数

    #ファイル名の設定
    name1 = setname("Initial number(n=200)_r=", r)
    name2 = setname("Initial number plot_r=", r)

    #ファイルオープン
    f1 = fileopen(name1, ".dat") #初期値グラフ用出力ファイル
    f2 = fileopen(name2, ".dat") #n-Xnグラフ用出力ファイル
    gpout(setname("r = ", r), "X0", "X200", name1)
    gpout(setname("r = ", r), "X0", "150<Xn<200", name2)

    #計算
    while int(x0 * 1000) <= 1000: #double型の誤差を弾くため1000倍してintへキャスト
        x = x0 #計算用初期値
        for i in range(n+1):
            if(i != 0):
                x = r * (1 - x) * x #与式兼n+
            #n-Xnグラフ用プロットデータ
            if(i>150):
                f2.write(strout(x0, x))
        #初期値用プロットデータ
        f1.write(strout(x0, x))
        x0 += 0.001 #初期値変更
    #ファイルクローズ
    f1.close()
    f2.close()