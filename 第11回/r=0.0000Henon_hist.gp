set grid
set title "r = 0.0000"
set xrange [0:2]
set yrange [0:10000]
set xlabel "r"
set ylabel "h"
plot "r=0.0000Henon_hist.dat" using 1:2 with impulses
pause 2
set terminal png
set output "r=0.0000Henon_hist.png"
replot
set terminal x11