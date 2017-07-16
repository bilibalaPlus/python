'''Part1'''
list

	list comprehension 列表推导式
	[x ** 2 for x in tmp_list if '''条件 and or   e.g. if x % 3 == 0''']
	map       	map(lambda x: x**2 if x%3==0 else x, tmp_list) 
				#比写for循环的效率高,for循环是串行的处理，这样写不用搞多进程多线程，直接帮你搞成并行的了，
				#map做的是分发的事情，一对多，多对多,对元素逐个处理
	

	reduce		#多个聚合到一个，对两个两个元素一起处理
				def my_sum(x, y):
					return x+y
				reduce(my_sum, range(1, 1000)) #此处是python2的写法，python3中生成的是迭代器，需要将其转化为list，reduce这种函数左边都是一个function
											   #python3中需要 import functools


	filter 		#从大量的数据中筛选出符合条件的数据，首先要搞一个True of False 的条件函数function
				def my_func(x):
					if  x % 3 == 0:
						return True
					else:
						return False
				filter(my_func, range(1, 1000)) #记住左边都是function，右边才是你的数据


	sorted		my_list = [4, 6,1 ,7, 11, 5]
				my_list.sort() #这是inplace的
				s = sorted(my_list) #这个不是inplace的，并不是成员函数，只是python的内置函数
				#sorted实用方法，供参考 http://www.cnblogs.com/freemao/p/3869994.html
				my_list = ['aaa', 'BB', 'cc', 'DD']
				sorted(my_list， key=str.lower()， reverse = False) #此处写法有可能是python2.7的， python3版本的事情参考上面的网址
																   #reverse = True是倒叙的
	
	lambda		#匿名函数，可以跟前面的函数配合着来


	zip			#能够把一些东西串在一起
				x = [1, 2, 3]
				y = [4, 5, 6]
				z = [7, 8, 9]
				result = zip(x, y, z) #此处为python2.7写法，python3生成的是迭代器，可以写成 list(zip(x, y, z))
									  #答案是 [(1,4,7),(2,5,8),(3,6,9)]
									  #如果此处x有四个元素，返回的还是原来一样的答案，会以最短的元素长度显示
				new_result = zip(*result) #刚才是用拉链拉起来了，现在会打散，*表示不定长个参数
	

	eval		help(eval) #python内置的解释器 evaluate(condition, action) condition是条件
				tmp_dic = {'para':5, 'test_first':test_first, 'test_second':test_second}
				def test_first():
					return 2
				def test_second(x):
					return x	
				condition = 'para == 5 and test_second(test_first) <3' #这其实是一个字符串，但是用了eval就能解释了
				eval(conditon, tmp_dic)


	slice       #从左往右0开始， 从右往左-1开始



	'''
	对list首选的处理 []  map
	其次 def my_fun():
	对函数有疑问的时候，可以用 help, dir， e.g. help(sklearn.preprocessing) 好的开发人员并不是记忆力有多好，而是会借助工具
	'''
	text = '男' if gender ='male' else '女' #考虑到代码的可读性，不建议实用
	gender == male == '男' #需要比较三个数
	if 18 <= age <= 40:  #链式比较
		print('young man ')


'''part2'''
dict

	dic.get
				tmp_dic = {'dog':4, 'spidier':8}
				tmp_dic['dog']  #如果此处要取cat,但是目前没有，下面有三种解决方法 1.try except 2 if..... 3.dic.get 4.dic.setdefault
				try:
					value = tmp_dic['Cat']
				except Exception, e:
					print e
					print 'no key' 

				if key in word_count:


				tmp_dic.get('cat', 4) #如果有这个key,就取对应的key,如果没有，就取default value

	
	dic.setdefault(key, 0) 
				#上式只能对一个key设置一个默认值
				#e.g.这个key没有出现就得到0的默认值

'''part3'''
generator
				result = (i ** 2 for i in range(1000)) #此处生成的是generator, 可以得到一个游标，指向一个对象，依旧可以用sum(result), 
				listresult = [i ** 2 for i in range(1000)]
				
				#数组可以根据index获得，链表需要不断的next
				#generator并没有一次性把所有东西生成在内存中
















