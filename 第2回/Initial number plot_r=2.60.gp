set grid
set title "r = 2.60"
set xrange [0:1]
set yrange [0:1]
set xlabel "X0"
set ylabel "150<Xn<200"
plot "Initial number plot_r=2.60.dat"with points pt 5 ps 0.2
pause 2
set terminal png
set output "Initial number plot_r=2.60.png"
replot
set terminal x11