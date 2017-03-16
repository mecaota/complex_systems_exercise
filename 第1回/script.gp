set grid #グリッド表示
set title "r = 3.5" #タイトル
set yrange [0:1] #y軸の描画範囲
set xrange [0:100] #x軸の描画範囲
set xlabel "n" #x軸ラベル（リターンマップの際は”Xn”となる）
set ylabel "Xn" #y軸ラベル(リターンマップの際は”X(n+1)”となる)
plot "Logistic_XXX_x[0]=XXX_n=XXX.dat" with lines #XXXにはそれぞれのファイル名が入る
#ファイル出力に関する処理
pause 2
set terminal png
set output "Logistic_XXX_x[0]=XXX_n=XXX.png" #XXXにはそれぞれのファイル名が入る
replot
setterminal x11