### bar chart
cmd_plot bar --data 10,20,30 --labels A,B,C
cmd_plot bar --data 5,15,25,10 --labels Apple,Banana,Cherry,Date --width 40

### line chart
cmd_plot line --x 1,2,3,4,5 --y 2,4,6,8,10
cmd_plot line --x 0,1,2,3,4,5,6 --y 0,0.84,0.91,0.14,-0.76,-0.96,-0.28 --height 15 --width 70
cmd_plot line --x 0,2,4,6,8,10 --y 5,10,5,10,5,10 --height 25 --width 60

### scatter chart
cmd_plot scatter --x 1,2,3,4,5 --y 3,1,4,2,5
cmd_plot scatter --x 1,3,5,7,9 --y 2,4,1,5,3 --height 20 --width 70

### pie chart
cmd_plot pie --data 30,50,20 --labels A,B,C
cmd_plot pie --data 10,15,20,25,30 --labels Red,Blue,Green,Yellow,Black --size 25
cmd_plot pie --data 90,5,5 --labels Majority,Minority1,Minority2 --size 30
