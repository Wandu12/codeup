# 1027  
year, month, day = input().split(".")
print("%02d" % int(day), end="-")
print("%02d" % int(month), end="-")
print("%04d" % int(year))
