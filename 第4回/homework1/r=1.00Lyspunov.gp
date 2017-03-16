set grid
set title "r = 1.00"
set xrange [1:4]
set yrange [-3:1]
set xlabel "r"
set ylabel "lyspunov exponent"
plot "r=1.00Lyspunov.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=1.00Lyspunov.png"
replot
set terminal x11