set grid
set title "r = 0.0000"
set xrange [0:1.6]
set yrange [-1.5:1.5]
plot "r=0.0000HenonCascade.dat" with points pt 0.5 ps 0.2
pause 2
set terminal png
set output "r=0.0000HenonCascade.png"
replot
set terminal x11