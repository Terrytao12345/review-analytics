#review analytics

data =[]
count = 0
with open ('reviews.txt', 'r') as a :
	for review in a :
		print(review) 
		data.append(review.strip())
		#data.append(review)
		count += 1
		if count % 1000 == 0 : # ％>後面於數多少 == ?? ,確認除1000後 於數為0的
			print(len(data))

print(len(data))
print(data[0]) #印出data list 的第一段,第一段似乎取決於換行鍵後第二段


#算出reviews 裡的每段文字平均長度

'''
data2 = []
with open ('reviews.txt', 'r') as b :
	for review in b : 
		data2.append(review.strip())
		len(data2) 
'''
