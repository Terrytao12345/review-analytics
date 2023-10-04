#review analytics
# class 55-56 
#edit test in github


data =[]
count = 0
with open ('reviews.txt', 'r') as a :
	for review in a :
		#print(review) 
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


new=[]

for d in data :
	if len(d) < 100 :
		new.append(d)
print('總共有', len(new), '筆資料小於長度100')


good = []
for s in data :
	if 'good' in s : #有多少good str in s 這虛擬清單 # ex: print('a' in 'abc's) = true
		good.append(s)

print('總共有', len(good), '筆資料擁有good的字串')
print('a' in 'abc')

#class 58 list 快寫法 

#line 34~40

good = [ s for s in data if 'good' in d ] # == line 34~37 # s 也可取代其他東西(1/true/sth)
bad = ['bad' in s for s in data ] # 確認bad 有沒有在 s 裡（從data 掉出的s 放入good清單）true/false

print(bad)