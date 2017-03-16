set grid
set title "r = 1.00"
set xrange [1:4]
set yrange [0:1]
set xlabel "r"
set ylabel "Xn"
plot "r=1.00_n=1000bifurcation diagram.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=1.00_n=1000bifurcation diagram.png"
replot
set terminal x11