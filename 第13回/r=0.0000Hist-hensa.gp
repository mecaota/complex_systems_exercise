set grid
set title "r = 0.0000"
set xrange [-10:-4.5]
set yrange [8:14]
set xlabel "Log r"
set ylabel "Log C"
plot "r=0.0000Hist-hensa.dat", "r=0.0000Hist_sumlog.dat" with points notitle pointtype 13
pause 2
set terminal png
set output "r=0.0000Hist-hensa.png"
replot
set terminal x11