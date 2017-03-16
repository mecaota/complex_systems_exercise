set grid
set title "r = 3.8284"
set xrange [0:1]
set yrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"
plot "r=3.8284RetLogistic3.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=3.82843countLogistic3.png"
replot
set terminal x11