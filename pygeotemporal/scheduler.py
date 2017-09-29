# coding: utf-8

"""
    Parser scheduler.
"""

import schedule
import time
import subprocess
import smtplib
from email.mime.text import MIMEText

def job(execution, title, toaddress):
    try:
        # change the file locate and username and password
        # for test
        # print "I'm working..."
        subprocess.check_output(execution, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: 
        now = time.strftime("%c")
        fromaddress = "devnull@ncsa.illinois.edu"
        message = MIMEText("Failed at %s \n-----------------------------------\n %s \n" % (now, e.output))
        message['Subject'] = title
        message['From'] = fromaddress
        message['To'] = toaddress

        server = smtplib.SMTP('smtp.ncsa.illinois.edu', 25)
        server.sendmail(fromaddress, toaddress.split(", "), message.as_string())
        server.quit()

def scheduler(execution, title, toaddress): 
	# https://github.com/dbader/schedule
	# for test
	# scheduler = schedule.every(1).minutes
	scheduler = schedule.every().monday
	kwargs = {"execution": execution, "title": title, "toaddress": toaddress}
	scheduler.do(job, **kwargs)

	while True:
	    schedule.run_pending()
	    time.sleep(1)