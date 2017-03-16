set grid
set title "r = 3.8285"
set xrange [0:1]
set yrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"
plot "r=3.8285RetLogistic.dat" with points pt 0.5 ps 0.2,"r=3.8285ReturnMap.dat" with lines,x with lines
pause 2
set terminal png
set output "r=3.8285ReturnMap.png"
replot
set terminal x11