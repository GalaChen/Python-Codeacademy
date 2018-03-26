count = 0

while True:


  print count
  count += 1
  if count >= 10:
    break
# break的用法


count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
# while也可以接else
# 当while的条件为FALSE，则执行else

choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item
#enumerate可以计数index，每当传递了一个factor之后，index自动加一

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
  print max(a,b)
# zip可以同时传递2个或者多个list，从而是loop可以有相应的参数个数

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
   
  print 'A', f
else:
  print 'A fine selection of fruits!'
  
#for循环也可以有else
#for循环的else只有在for循环正常终止后才能执行
#如果for循环运行过程中被break打断，则for循环不会执行else