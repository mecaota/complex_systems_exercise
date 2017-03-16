set grid
set title "r = 1.50"

set yrange [0:1]
set xrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"


plot "Return_1.50_x[0]=0.70_n=100.dat" with lines ,x with lines, "Logistic_1.50_x[0]=0.70_n=100.dat" with lines
pause 2
set terminal png
set output "Return_1.50_x[0]=0.70_n=100.png"
replot
setterminal x11