set grid
set title "r = 0.0000"
set xrange [-2:2]
set yrange [-0.5:0.5]
set xlabel "Xn"
set ylabel "X(n+1)"
plot "r=0.0000Henon.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=0.0000Henon.png"
replot
set terminal x11