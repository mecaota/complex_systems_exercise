set grid
set title "r = 2.60"

set yrange [0:1]
set xrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"


plot "Return_2.60_x[0]=0.70_n=100.dat" with lines, "Logistic_2.60_x[0]=0.70_n=100.dat" with lines, x with lines
pause 2
set terminal png
set output "Return_2.60_x[0]=0.70_n=100.png"
replot
setterminal x11