######################################
############    String    ############
######################################

#对于字符串中有引号的，需要在前面加上“\”
'There's a snake in my boot!'
'There\'s a snake in my boot!'

#string中的每一个字母都是list中的独立元素
#其index的起始数字为0
'MONTY'[4]

#字符串函数
len('Norwegian Blue') #这类函数不仅仅只用于字符串类型的数据
"Ryan".lower() #这类函数只用于字符串，所以采用字符串+".函数"的方式
parrot.upper() 
str(2) #将非字符串转换为字符串

#字符串运算
print "Life " + "of " + "Brian"    #字符串加法
print "I have " + str(2) + " coconuts!"     #结合字符串函数

#变量在字符串中的输出
name = "Mike"
print "Hello %s" % (name)

day = 6
print "03 - %s - 2019" %  (day)
#output 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
#output 03 - 06 - 2019

string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#字符串需要输入变量时，在字符串内用%s表示变量，字符串结尾引号后用%(variable_name)表示
#%02d表示变量为整数，占据2个字符的位置，不足两位的在前面用0填充。0只能放在d之前
#当存在两个变量时，在需要填充变量的位置放置%s即可。注意保持前面的%s与后面的变量数量相同 

