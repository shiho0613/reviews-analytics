data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0: # %求餘數
			print(len(data))
print(len(data))


sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均長度是', sum_len/len(data))

new = [] # 製作新清單
for d in data: #for ? in ！ 叫出！的東西
	if len(d) < 100:
		new.append(d) # 將資料夾進新清單
print('一共有', len(new),'筆留言小於100字')