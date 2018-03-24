#############################################
############    Date and Time    ############
#############################################

from datetime import datetime
now = datetime.now()
print '%02d/%02d/%04d' % (now.month, now.day, now.year)
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

#datetime模块能够提取系统时间
#datetime.now()能够提取当前系统时间的所有内容：年、月、日、时、分、秒
#.hour()等能够提取相应的时间信息
#结合变量在string显示的方法，从而显示希望获得的时间格式
 