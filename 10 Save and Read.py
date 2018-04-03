###################################################################
##################        Save and Read          ##################
###################################################################
my_file = open('output.txt','r+')
#open()表示打开某个文件
#r+表示以“read and write”的方式打开文件
#w表示以“write-only”的方式打开文件
#r表示以“read-only”的方式打开文件
#a表示以“append”的方式打开文件，这样可以把所获得的数据添加进入文件末尾

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in my_list:
  my_file.write(str(i)+"\n")

my_file.close()
#首先是以write only的方式打开了文件
#对于my_list的每一个内容以.write的形式写入文件中
#.write()只接受string
#文件写入后，记住添加.close()

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()
#读取file内容的方法
#文件读取后也要记住close

my_file = open('text.txt','r')
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()
#readline可以逐行读取内容

with open("text.txt", "w") as textfile:
  textfile.write("Success!")
#采用with 和 as， 可以使Python自动关闭文件

with open("text.txt","w") as my_file:
 my_file.write("test writting") 
 if my_file.closed is True:
    my_file.close()
#my_file.closed可以判断相应文件是否关闭，如果已关闭，则返回True，否则返回FALSE
