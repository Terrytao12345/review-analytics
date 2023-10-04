#review analytics
# class 55-56 
#edit test in github


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

print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data :
	sum_len = sum_len + len(d) 

print('總平均長度', sum_len/len(data))	


