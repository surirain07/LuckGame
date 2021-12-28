#이 게임은 한국인이 만든 운빨게임입니다.
#만약 정답이 나올 경우 밑에 댓글을 달아 주세요
import random
import time
import webbrowser
import os
print("선택할 언어를 입력해 주세요(ex. 한국어)\n")
language=input("(English / 한국어): ")
print("당신이 선택한 언어: ", language)

if language == "한국어":
	num=random.randrange(1,101)
	print(" ", num)
	ans=int(input("1~100 중의 숫자 중 1개를 입력하십시오: "))
	if ans == num:
		print("1%의 확률로 정답을 맞히셨습니다!\n")
		time.sleep(1)
		print("깃허브의 댓글로 다른 유저들에게 자랑해보세요!")
		time.sleep(0.5)
		site=input("깃허브 사이트 URL 바로가기 (y/n): ")
		if site == 'y':
			webbrowser.open("https://github.com/surirain07/LuckGame/commit/8651dddc5bf36270cf3cd97a7bc9f7ddcf795666")
		if site == 'n':
			os._exit(1)
	else:
		print("아쉽게도 오답입니다.\n")
		time.sleep(1)
		print("정답은 ", num , "이었습니다.")

if language == "English":
		num=random.randrange(1,101)
		print(" ", num)
		ans=int(input("Input the number between 1~100: "))
		if ans == num:
			print("Congratulations! You got the answer with a 1% chance!\n")
			time.sleep(1)
			print("Show off to other users through Github's comments!")
			site = input("Would you like to use the Github site shortcut? (y/n)")
			if site == 'y':
				webbrowser.open("https://github.com/surirain07/LuckGame/commit/8651dddc5bf36270cf3cd97a7bc9f7ddcf795666")
			if site == 'n':
				os._exit(1)
		else:
			print("Unfortunately, it's wrong.\n")
			time.sleep(1)
			print("The answer was ", num)
