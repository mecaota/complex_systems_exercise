set grid
set title "r = 3.20"

set yrange [0:1]
set xrange [0:100]
set xlabel "n"
set ylabel "Xn"


plot "Logistic_3.20_x[0]=0.70_n=100.dat" with lines
pause 2
set terminal png
set output "Logistic_3.20_x[0]=0.70_n=100.png"
replot
setterminal x11