M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

import platform
if platform.system() != 'Linux':
	print('Only runs on the linux platform!')
else:
	pass
	
try:
	import requests, random, sys, os
	from requests.exceptions import ConnectionError
	tes = requests.get('http://google.com')
	os.system('clear')
	
	def banner():
		print(''+C+'''\t
  ____                                ___ ____  
 |  _ \ _____   _____ _ __ ___  ___  |_ _|  _ \ 
 | |_) / _ \ \ / / _ \ '__/ __|/ _ \  | || |_) |
 |  _ <  __/\ V /  __/ |  \__ \  __/  | ||  __/ 
 |_| \_\___| \_/ \___|_|  |___/\___| |___|_|    
                                                
'''+W+'\t\tReverse IP Lookup\n\t\tCreator : ./Fukur0\n')

	banner()
	print
	print(C+'\t['+W+'1'+C+']'+W+' SOLO TARGET')
	print(C+'\t['+W+'2'+C+']'+W+' LIST TARGET')
	print
	pilih = raw_input(C+'\t['+W+'+'+C+']'+W+' Pilih Tool -> '+C+'')
	
	if pilih == '1':
		os.system('clear')
		banner()
		print
		url = raw_input(C+'Url'+U+' ('+H+' Ex : '+W+'google.com'+U+' )'+W+' : ')
		print
		print(C+'   -------------- '+W+'Starting'+C+' --------------')
		if 'http' in url:
			print
			print(W+'-----'+M+' No HTTP !'+W+' -----')
			sys.exit()
		else:
			pass
		print
		a = True
		while a:
			try:
				proxy = {'https' : 'https://' + random.choice(open('proxy', 'r').readlines()).replace('\r\n', '')}
				api = 'http://api.hackertarget.com/reverseiplookup/?q=' + url
				to = requests.get(api, proxies = proxy)
				if to.status_code != 200:
					continue
				else:
					a = False
					name = url.split('.')[0] + '.txt'
					print(W+'- '+C+str(url)+W+' : '+C+str(name)+H+' Saved'+W+' !')
					save = open(name, 'w').write(to.text);save.close()
					
			except:
				continue
				
	elif pilih == '2':
		os.system('clear')
		banner()
		print
		list = raw_input(C+'Url'+U+' ('+H+' Ex : '+W+'list.txt'+U+' )'+W+' : ')
		print
		print(C+'   -------------- '+W+'Starting'+C+' --------------')
		print
		for url in open(list).read().strip().split('\n'):
			if 'http' in url:
				print
				print(W+'-----'+M+' No HTTP !'+W+' -----')
				sys.exit()
			else:
				pass
			try:
				proxy = {'https' : 'https://' + random.choice(open('proxy', 'r').readlines()).replace('\r\n', '')}
				api = 'http://api.hackertarget.com/reverseiplookup/?q=' + url
				to = requests.get(api, proxies = proxy)
				if to.status_code != 200:
					continue
				else:
					name = url.split('.')[0] + '.txt'
					print(W+'- '+C+str(url)+W+' : '+C+str(name)+H+' Saved'+W+' !')
					save = open(name, 'w').write(to.text);save.close()
						
			except:
				continue
				
	else:
		print
		print(W+'-----'+M+' Incorrect Choice'+W+' -----')

except ConnectionError:
	print
	print(W+'-----'+M+' Connection Error'+W+' -----')

except ImportError:
	os.system('pip2 install requests')
	os.system('python2 ' + __file__)

except IOError:
	print
	print(W+'-----'+M+' No Such File'+W+' -----')