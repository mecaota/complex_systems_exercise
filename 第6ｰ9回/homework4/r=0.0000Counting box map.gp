set grid
set title "r = 0.0000"
set xrange [0:100]
set yrange [0:800]
set xlabel "N"
set ylabel "m(N)"
plot "r=0.0000Counting box map.dat" with points pt 1 ps 0.2
pause 2
set terminal png
set output "r=0.0000Counting box map.png"
replot
set terminal x11