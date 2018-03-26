def remove_duplicates(x):
  ans = []
  for i in x:
    if i not in ans:
      ans.append(i)
  return ans
  
def censor(text,word):
  aim = text.split()
  for i in range(len(aim)):
    if aim[i] == word:
      aim[i] = "".join("*"*len(word))
     # aim[i] = ("*"*len(word))
  return aim

print censor("this hack is wack hack", "hack")

d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
#.items()以无序形式显示所有的内容
#.keys()和.values()可以无序显示相应内容

new_list = [x for x in range(1, 6)]
# => [1, 2, 3, 4, 5]
#构建list的另一种方式

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
even_squares = [x**2 for x in range(1,12) if x%2 == 0]
#这种方式，for循环构建list范围，其后可跟x的筛选方式，其前为最终展现的x方式

[start:end:stride]
#list截取方法
#start包含其内，end不包含其内，stride是步进长度
l = [i ** 2 for i in range(1, 11)]
print l
print l[2:9:2]


to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']
##########################start，end，stride可以省略，系统会自动默认

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
#stride的负数表示方向


my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
lambda x: x % 3 == 0 
#这个式子等同于
 def by_three(x):
  return x % 3 == 0
#lambda 传递的相当于定义函数时所用的形式参数
#中间是函数的内容
#最后是实际传递给函数的数据