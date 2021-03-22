try:
	import requests
	import os
	from os import system, path
	import re
	import json
	import time
	import random
	system("title " + "Soud Was Here - @8Y - Soud#0737")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

a = requests.session()
if path.exists("proxy.txt"):
	proxyfile = open("proxy.txt", 'r').read().splitlines()
else:
	print("Pls Make proxy.txt file\n")
	input()
	exit()
logo = """
         _______   __
   ____ |  _  \ \ / /
  / __ \ \ V / \ V / 
 / / _` |/ _ \  \ /  
| | (_| | |_| | | |  
 \ \__,_\_____/ \_/  
  \____/             
"""

print(Fore.CYAN+logo)
print(Fore.GREEN+"\n\tInstagram: @8Y\n\tGithub: @Soud69\n\tDiscord: Soud#0737\n\tTelegram: @Soud69"+Fore.RED+"\n\t[Dont Try To Sell It]\n")

mode = int(input("1) Comment Like\n2) Post Views\n3) Story Views\n>> "))

if mode == 1:
	url = "https://sifresiz.instahile.co/comment-likes"
	head = {
		"Host": "sifresiz.instahile.co",
		"Content-Type": "application/x-www-form-urlencoded",
		"Origin": "https://sifresiz.instahile.co",
		"Accept-Encoding": "gzip, deflate, br",
		"Connection": "keep-alive",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
		"Referer": "https://sifresiz.instahile.co/comment-likes",
		"Accept-Language": "en-us"
	}
	url_post = input("\nEnter Post URL: ")
	data = {
		"link": url_post
	}
	get_comment = requests.post(url, data=data, headers=head)
	if "Medya bulunamadı! " in get_comment.text:
		print(Fore.RED+"[-] Your Account Is Private Or Post Not Found\n")
		input()
		exit()
	elif "Şifresiz Yorum Beğeni Gönder" in get_comment.text:
		print(Fore.GREEN+"Post Found Grabbing Comments...\n")
		soud = re.compile('<option value="(.*?)">@(.*?) (.*?)</option>')
		soudd = soud.findall(get_comment.text)
		print(Fore.GREEN+"Copy Your Comment ID, Example: 123|123\n")
		time.sleep(2.5)
		for i in soudd:
			idd = i[0]
			username = i[1]
			comment = i[2]
			print(f"ID: {idd} By: @{username} Comment: {comment}")
		iddd = input("Enter Your Comment ID: ")
		url_likes = "https://sifresiz.instahile.co/c/comment_likes.php"
		data_likes = {
			"comment_id": iddd
		}
		while 1:
			proxydict = []
			proxydict.clear()
			for proxy in proxyfile:
				proxydict.append(proxy)
			randomproxy = str(random.choice(proxydict))
			ipp = randomproxy.split(":")[0]
			pport = randomproxy.split(":")[1]
			try:
				proxyfinal = {
					"https": f"https://{ipp}:{pport}",
					"http": f"http://{ipp}:{pport}"
					}
				likes_send = a.post(url_likes, data=data_likes, headers=head, proxies=proxyfinal, timeout=1.5)
				if '{"sent":' in likes_send.text:
					sent = json.loads(likes_send.text)["sent"]
					print(f"Sent Likes: {sent}")
				else:
					pass
			except:
				pass
					
elif mode == 2:
	head = {
	"Host": "sifresiz.instahile.co",
	"Content-Type": "application/x-www-form-urlencoded",
	"Origin": "https://sifresiz.instahile.co",
	"Accept-Encoding": "gzip, deflate, br",
	"Connection": "keep-alive",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
	"Referer": "https://sifresiz.instahile.co/views",
	"Accept-Language": "en-us"
	}
	post_url = input("Enter Post URL: ")
	data = {
	"link": post_url
	}	
	url = "https://sifresiz.instahile.co/views"
	view_post = requests.post(url, data=data, headers=head)
	if "Video Bulunamadı!" in view_post.text:
		print(Fore.RED+"[-] Your Account Is Private Or Post Not Found\n")
		input()
		exit()
	elif "Görüntülenmeler gönderilmeye hazır!" in view_post.text:
		print(Fore.GREEN+"[+] Found Post Sending Views Now")
		soup = BeautifulSoup(view_post.text, "html.parser")
		media_id = soup.find("input",{"name":"media_id"})["value"]
		count = int(input("[Choose Mode]\n10 Views\n20 Views\n30 Views\n>> "))
		views_head = {
			"Host": "sifresiz.instahile.co",
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"X-Requested-With": "XMLHttpRequest",
			"Accept-Language": "en-us",
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Origin": "https://sifresiz.instahile.co",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
			"Connection": "keep-alive",
			"Referer": "https://sifresiz.instahile.co/views"}
		views_url = "https://sifresiz.instahile.co/c/views.php"
		views_data = {
			"media_id": media_id,
			"quantity": count}
		while 1:
			proxydict = []
			proxydict.clear()
			for proxy in proxyfile:
				proxydict.append(proxy)
			randomproxy = str(random.choice(proxydict))
			ipp = randomproxy.split(":")[0]
			pport = randomproxy.split(":")[1]
			try:
				proxyfinal = {
					"https": f"https://{ipp}:{pport}",
					"http": f"http://{ipp}:{pport}"}
				send_views = a.post(views_url, data=views_data, headers=views_head, proxies=proxyfinal, timeout=1.5)
				if '{"sent":' in send_views.text:
					totalviews = json.loads(send_views.text)["sent"]
					print(f"Done Sent Views: {totalviews}")
				else:
					pass
			except:
				pass
elif mode == 3:
		head = {
			"Host": "sifresiz.instahile.co",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://sifresiz.instahile.co",
			"Accept-Encoding": "gzip, deflate, br",
			"Connection": "keep-alive",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
			"Referer": "https://sifresiz.instahile.co/story-views",
			"Accept-Language": "en-us"}
		usernamee = input("Enter Your Username: ")
		data = {
			"username": usernamee
			}	
		url = "https://sifresiz.instahile.co/story-views"
		view_post = requests.post(url, data=data, headers=head)
		if "Profil bulunamadı!" in view_post.text:
			print(Fore.RED+"[-] Your Account Is Private Or Post Not Found\n")
			input()
			exit()
		elif "Hikaye İzlenmeler gönderilmeye hazır!" in view_post.text:
			print(Fore.GREEN+"[+] Found Story Sending Views Now")
			soup = BeautifulSoup(view_post.text, "html.parser")
			media_id = soup.find("input",{"name":"pk"})["value"]
			views_head = {
				"Host": "sifresiz.instahile.co",
				"Accept": "application/json, text/javascript, */*; q=0.01",
				"X-Requested-With": "XMLHttpRequest",
				"Accept-Language": "en-us",
				"Accept-Encoding": "gzip, deflate, br",
				"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
				"Origin": "https://sifresiz.instahile.co",
				"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
				"Connection": "keep-alive",
				"Referer": "https://sifresiz.instahile.co/c/story_views.php"}
			views_url = "https://sifresiz.instahile.co/c/story_views.php"
			views_data = {
				"pk": media_id
				}
			while 1:
				proxydict = []
				proxydict.clear()
				for proxy in proxyfile:
					proxydict.append(proxy)
				randomproxy = str(random.choice(proxydict))
				ipp = randomproxy.split(":")[0]
				pport = randomproxy.split(":")[1]
				try:
					proxyfinal = {
						"https": f"https://{ipp}:{pport}",
						"http": f"http://{ipp}:{pport}"}
					send_views = a.post(views_url, data=views_data, headers=views_head, proxies=proxyfinal, timeout=1.5)
					if '{"sent":' in send_views.text:
						totalviews = json.loads(send_views.text)["sent"]
						print(f"Done Sent Views: {totalviews}")
					else:
						pass
				except:
					pass
