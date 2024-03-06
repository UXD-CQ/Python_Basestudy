# 一年内的总天数
total_days = 365

# 计算一年内的进步
progress = 0
for day in range(1, total_days + 1):
    if day % 3 == 0:  # 每三天进步百分之一
        progress += 0.02

# 计算一年内的退步
regress = 0
for day in range(1, total_days + 1):
    if day % 2 == 0:  # 每两天退步千分之五
        regress += 0.005

# 计算一年内的净进步
net_progress = progress - regress

print("一年内的进步：", round(progress, 3))
print("一年内的退步：", round(regress, 3))
print("一年内的净进步：", round(net_progress, 3))
