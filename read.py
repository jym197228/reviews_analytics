data = []
count = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %為求餘數的功能
			print(len(data))

print('檔案總共有', len(data), '筆資料')

# 計算每筆留言的平均長度

# 我的作法 去除空格
length = 0
for d in data:
     length = length + len(d.split())
print(length / count)

#老師的作法

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100個字母')
print(new[0])