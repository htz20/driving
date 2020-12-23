country = input("請問你是哪國人：")
age = input("輸入你的年齡：")
age = int(age)
if country == "台灣" :
	if age >= 18 :
		print("hihi")
	else:
		print ("你還不可以喔")
