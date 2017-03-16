set grid
set title "r = 0.0000"
set xrange [0:2]
set yrange [0:1000000]
set xlabel "r"
set ylabel "C"
plot "r=0.0000Hist-sum.dat" using 1:2 with lp notitle
pause 2
set terminal png
set output "r=0.0000Hist-sum.png"
replot
set terminal x11