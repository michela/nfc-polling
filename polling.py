import nxppy
import time
import subprocess

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument("--kiosk")
#driver = webdriver.Chrome(chrome_options=chrome_options)

mifare = nxppy.Mifare()

cards = {
	'043558FA634980':['Michela OPAL','https://en.wikipedia.org/wiki/Opal_card'],
	'04CA09EAFC3880':['Mifare EV1 test','http://www.mifare.net'],
	'FF525A79':['Michela Paypass','https://www.commbank.com.au/']
}
	
# Print card UIDs as they are detected
last = None
while True:
    try:
        uid = mifare.select()
        #print(uid,last)
	if last != uid:
		print(cards[uid][0])
		#driver.get(cards[uid][1])
		cmd = ["sudo","-u","pi","/usr/bin/chromium","--kiosk",cards[uid][1]]
		subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
		last = uid
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)
