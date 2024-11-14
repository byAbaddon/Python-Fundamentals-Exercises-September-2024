from datetime import timedelta

hour, m, sec = [int(x) for x in input().split(':')]
step = int(input())
step_sec = int(input())

all_step = step * step_sec

initial_time = timedelta(hours=hour, minutes=m, seconds=sec)
time_to_add = timedelta(seconds=all_step % (24 * 3600))

new_time = initial_time + time_to_add

new_hour = new_time.seconds // 3600
new_minute = (new_time.seconds % 3600) // 60
new_second = new_time.seconds % 60

print(f'Time Arrival: {new_hour:02}:{new_minute:02}:{new_second:02}')


'''
12:30:30
90
1
'''