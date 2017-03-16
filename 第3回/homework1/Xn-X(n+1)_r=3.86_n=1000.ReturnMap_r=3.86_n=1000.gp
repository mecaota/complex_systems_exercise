set grid
set title "r = 3.86"
set xrange [0:1]
set yrange [0:1]
set xlabel "Xn"
set ylabel "Xn+1"
plot "Xn-X(n+1)_r=3.86_n=1000.dat" with points ps 0.2, "ReturnMap_r=3.86_n=1000.dat" with lines ps 0.2,x  with lines
pause 2
set terminal png
set output "Xn-X(n+1)_r=3.86_n=1000.png"
replot
set terminal x11