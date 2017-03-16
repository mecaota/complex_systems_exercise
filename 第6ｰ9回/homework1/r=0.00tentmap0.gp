set grid
set title "r = 0.00"
set xrange [0:1]
set yrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"
plot "r=0.00tentmap0.dat" with lines,x with lines
pause 2
set terminal png
set output "r=0.00tentmap0.png"
replot
set terminal x11