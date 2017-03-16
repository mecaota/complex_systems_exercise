set grid
set title "r = 3.8285"
set xrange [250:500]
set yrange [0:1]
set xlabel "Xn"
set ylabel "X(n+1)"
plot "r=3.8285Logistic.dat" with lines,x with lines
pause 2
set terminal png
set output "r=3.8285Logistic.png"
replot
set terminal x11