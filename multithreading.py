#!/usr/bin/python3
import threading, time, subprocess, os

def takeANap():
    time.sleep(3)
    print('Wake up!')

print('Start of program.')
thread = threading.Thread(target = takeANap)    # only function name, not a function call - without parentheses
thread.start()                                  # creates new thread and starts executing the targeted function
print('End of program.')

# target function with arguments:
print('Cats', 'Dogs', 'Frogs', sep = ' & ')     # 3 regular, 1 keyword argument
threadPrint = threading.Thread(target = print, args = ['Cats', 'Dogs', 'Frogs'], kwargs = {'sep': ' & '})   # reg args are in list, kw args are in dict!!
threadPrint.start()

# Starting calculator:
PopenObject = subprocess.Popen('/usr/bin/gnome-calculator')
print(PopenObject.poll())   # None if the process is still runing, or integer exit code (0 - OK, else - error) if it has terminated
print(PopenObject.wait())   # block until the launched process has terminated, then returns exit code

# Start program in different process with subprocess:
def foo():
    subprocess.Popen(['/usr/bin/python3', './ws_imFeelingLuckyGoogleSearch.py', 'it works'])
    subprocess.Popen(['see', './done/hello.txt'])
threadSub = threading.Thread(target = foo)
threadSub.start()
print(os.getcwd())
