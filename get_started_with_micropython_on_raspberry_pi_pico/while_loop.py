import utime

print('loop started!')
count = 0
while True:
    print('loop count running: ',count)
    utime.sleep(1)
    if count>5:
        break
    count = count + 1
print('loop finished!')