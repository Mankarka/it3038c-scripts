from msvcrt import kbhit
import time
start_time = time.time()


print('What is your name?')
myName = input()
print ('Hello, ' + myName + ' . That is a good name. How old are you?')
myAge = input()
programAge = int(time.time() - start_time)
print('%s? that"s funny, i"m only %s seconds old.' % (myAge, programAge ))
print('i wish i was %s years old' %(myAge *2))

time.sleep(3)
print('I"m tired. I go sleep sleep now'
