set grid
set title "r = 3.8250"
set xrange [3.825:3.86]
set yrange [-1:0.4]
set xlabel "r"
set ylabel "lyspunov exponent"
plot "r=3.83Lyspunov.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=3.83Lyspunov.png"
replot
set terminal x11