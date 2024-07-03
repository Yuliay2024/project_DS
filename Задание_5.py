sq_1 = ['watch new movies', 'coffee near me', 'how to find the determinant', 'python',  
		'data science jobs in UK', 'courses for data science', 'taxi', 'google', 'yandex',  
		'bing','foreign exchange rates USD/BYN', 'Netflix movies watch online free',    
		'Statistics courses online from top universities']           
		
sq_2 = [] 
for i in range(len(sq_1)):     
	k = sq_1[i].split()     
	sq_2.append(k) 
	sq_3=list(map(lambda k: len(k), sq_2)) 

print('1 слово :', (round((sq_3.count(int(1))/len(sq_1))*100)),'%')
print('3 слова :', (round((sq_3.count(int(3))/len(sq_1))*100)),'%') 
print('4 слова :', (round((sq_3.count(int(4))/len(sq_1))*100)),'%') 
print('5 слов :', (round((sq_3.count(int(5))/len(sq_1))*100)),'%') 
print('6 слов :', (round((sq_3.count(int(6))/len(sq_1))*100)),'%')