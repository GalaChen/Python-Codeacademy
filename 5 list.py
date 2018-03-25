####################################
############    List    ############
####################################

#list是python里的一种数据类型，它能够在一个变量名下储存一系列不同类型的数据
#例如：字符、数字和布尔运算
#list的构建形式如下
list_name = [item_1, item_2, ...]

#list的index开始于0
#list调用形式为list_name[index]，也可以通过这种方式来为list的内容进行赋值

list_name.append(sth)
#list的长度并不固定，通过上述语句可以随时向list添加内容
list_name.remove(sth)
#删除list中的某些内容

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
#list的分割
#分割中的1:3表示从index=1开始，到index=2结束；即左闭右开
#slice最终的输出结果为['b','c']

my_list[:2]
my_list[3:]
#若包含起始与终止，则相应的数字不用写出

#一个字符串可以看作是一个由字母组成的list
#list的所有规则同样适用于字符串

animals = ["ant", "bat", "cat"]
print animals.index("bat")
animals.insert(1, "dog")
print animals
#.index和.insert分别能获取index或者向list特定位置插入内容

for variable in list_name:
  # Do stuff!
#如果需要调用list中的每个元素，可以用for循环完成
#注意此时的variable是list中的每一个元素，而非index

animals = ["cat", "ant", "bat"]
animals.sort()
#list_name.sort()可以对list内容按照字母顺序或者数字从小到大进行排序

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin']
print residents['Sloth']
print residents['Burmese Python']
#dictionary类似list
#冒号之前的是'key'，冒号之后的为'key'所对应的内容
#获取dictionary的内容采用dictionary_name[key]的方式进行
#key和内容可以是各种数据类型

dict_name[new_key] = new_value
#dictionary赋值
del dict_name[key_name]
#删除dictionary内某个内容

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
  print webster[key]
#dictionary的for循环，通过循环调用key实现对dictionary的操作