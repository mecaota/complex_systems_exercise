set grid
set title "r = 3.8284"
set xrange [0.9561:0.9565]
set yrange [0.956:0.9565]
set xlabel "Xn"
set ylabel "X(n+3)"
plot "r=3.8284RetLogistic3s.dat" with points pt 0.5 ps 0.2,"r=3.8284ReturnMap3s.dat" with lines,x with lines
pause 2
set terminal png
set output "r=3.8284ReturnMap3s.png"
replot
set terminal x11