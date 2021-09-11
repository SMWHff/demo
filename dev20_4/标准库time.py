import time

print("国外格式：", time.asctime())
print("时间戳：", time.time())
print("时间元组：", time.localtime())
time_24h = time.time()-24*60*60
print("24小时前时间元组：", time.localtime(time_24h))
print("格式化时间：", time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime(time_24h)))