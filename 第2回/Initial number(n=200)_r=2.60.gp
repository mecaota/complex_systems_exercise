set grid
set title "r = 2.60"
set xrange [0:1]
set yrange [0:1]
set xlabel "X0"
set ylabel "X200"
plot "Initial number(n=200)_r=2.60.dat"with points pt 5 ps 0.2
pause 2
set terminal png
set output "Initial number(n=200)_r=2.60.png"
replot
set terminal x11