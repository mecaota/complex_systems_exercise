set grid
set title "r = 0.0000"
set xrange [-10:-4.5]
set yrange [8:14]
set xlabel "Log r"
set ylabel "Log C"
plot "r=0.0000Hist-sumlog.dat" using 1:2 with points notitle pointtype 13
pause 2
set terminal png
set output "r=0.0000Hist-sumlog.png"
replot
set terminal x11