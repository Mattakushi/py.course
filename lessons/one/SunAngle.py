import time

real_time = input("Input time here: ")

cvt_time = time.strptime(real_time, "%H:%M")
hours = cvt_time[3]
minutes = cvt_time[4]
all_minutes = hours * 60 + minutes

if all_minutes < 360 or all_minutes > 1080:
    ready_angle = 'I cannot see the sun!'
else:
    ready_angle = (all_minutes - 360) * 0.25

print(ready_angle)
