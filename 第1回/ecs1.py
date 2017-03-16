# -*- coding: utf-8 -*-
import datetime
import os
import numpy

def strout(x, nx):
    str = "{0:.3f}{1}{2:.3f}{3}".format(x, " ", nx, "\n") #データ整形
    return str

def gpout(x, y, r, xmax, ymax, namedat, namepng):
    sd = '"'
    #人海戦術式自動スクリプター（実装失敗のため未利用）
    str = "set grid\n"
    str += "set title "
    str += sd
    str += "r = "
  #  str += r
    str += sd
    str += "\nset xrange [0:"
    str += str(xmax)
    str += "]\n"
    str += "set yrange [0:"
    str += str(ymax)
    str += "]\n"
    str += "set xlabel "
    str += sd
    str += str(x)
    str += sd
    str += "\n"
    str += sd
    str += str(y)
    str += sd
    str += "plot "
    str += sd
    str += namedat
    str += sd
    str += "with lines\n"
    str += "pause 2\n"
    str += "set terminal png\n"
    str += "set output "
    str += sd
    str += namepng
    str += sd
    str += "\nreplot\n"
    str += "setterminal x11"
    return str

if __name__ == "__main__":
    ###プロットデータ生成###
    #入力受付
    r = float(input('r = ')) #グラフ変数r
    x = float(input('x[0] = ')) #初期値
    n = int(input('Calculate times? : ')) #計算回数
    max = 1 #最大値格納変数

    #ファイル名の設定
    name = "{0:.2f}{1}{2:.2f}{3}{4:d}".format(r, "_x[0]=", x, "_n=", n) #ファイル名の原型
    name1 = "{0}{1}{2}".format("Logistic_",name, ".dat") #ロジスティック用プロットデータファイル名
    name1g = "{0}{1}{2}".format("Logistic_",name, ".gp") #ロジスティック用gpファイル名
    name2 = "{0}{1}{2}".format("Return_",name, ".dat") #リターンマップ用プロットデータファイル名
    name2g = "{0}{1}{2}".format("Return_",name, ".gp") #リターンマップ用gpファイル名


    #ファイルオープン
    f1 = open(name1, 'w', encoding="UTF-8") #ロジスティック用出力ファイル
    f2 = open(name2, 'w', encoding="UTF-8") #リターンマップ用出力ファイル
    print(name) #出力ファイル名

    #計算
    #logistic用プロットデータ(初期値の場合)
    f1.write(strout(0, x))
    for i in range(n):
        nx = r * (1 - x) * x #与式兼n+1項の値
        #logistic用プロットデータ
        f1.write(strout(i+1, nx))
        #Returnmap用プロットデータ
        f2.write(strout(x, nx))
        x = nx #リターンマップ用プロットデータ入力のための処理
        f2.write(strout(x, nx))
        if(nx > max):
            max = nx
    #ファイルクローズ
    f1.close()
    f2.close()