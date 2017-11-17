import pyautogui
import time

print("裝忙開始, Press Ctrl+C to exit.\n\n1分鐘後移動滑鼠\n")

total = 0

try:
	while True:
		time.sleep(60)
		total += 1
		pyautogui.moveTo(100, 100, duration=0.25)
		print("1分鐘後移動滑鼠\n")
		
		time.sleep(60)
		total += 1
		pyautogui.moveTo(200, 100, duration=0.25)
		print("1分鐘後移動滑鼠\n")
		
		time.sleep(60)
		total += 1
		pyautogui.moveTo(200, 200, duration=0.25)
		print("1分鐘後移動滑鼠\n")
		
		time.sleep(60)
		total += 1
		pyautogui.moveTo(100, 200, duration=0.25)
		
except KeyboardInterrupt:
	print("裝忙結束, 你一共摸魚了"+str(total)+"分鐘\n")
	print("3...\n")
	time.sleep(1)
	print("2..\n")
	time.sleep(1)
	print("1.\n")
	print("Bye\n")
	time.sleep(1)