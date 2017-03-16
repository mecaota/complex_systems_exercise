set grid
set title "r = 1.50"
set xrange [0:1]
set yrange [0:1]
set xlabel "X0"
set ylabel "150<Xn<200"
plot "Initial number plot_r=1.50.dat"with points pt 5 ps 0.2
pause 2
set terminal png
set output "Initial number plot_r=1.50.png"
replot
set terminal x11