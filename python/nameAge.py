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

      
      
 if myAge < 13:
  print("Learning young, that's good")

elif myAge == 13:
  print("You're a teenager now... that's cool, I guess")

elif myAge > 13 and myAge < 30:
  print("Still young, still learning…")

elif myAge >= 30 and myAge < 65:
  print("Now you're adulting.")

else:
  print("... you've lived a long time?")     
      
      
 while True:
  print('Please type your name.')
  name = input()

  if name == 'Kiro':
    break

print('Thank You')
      
