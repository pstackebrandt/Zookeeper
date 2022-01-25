hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

hours = hours2 - hours1
minutes = minutes2 - minutes1
seconds = seconds2 - seconds1

seconds += ((hours * 60) + minutes) * 60
print(seconds)
