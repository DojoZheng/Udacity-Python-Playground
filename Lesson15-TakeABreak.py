import webbrowser
# how to open browser in python? 
# https://docs.python.org/2/library/webbrowser.html

import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while (break_count < total_breaks):
	time.sleep(5)
	webbrowser.open("http://www.baidu.com")
	break_count += 1