#Import libraries for Python Website Monitoring project
import urllib.request
import smtplib

#Monitor the website
def monitor_website(event, context):
       #Visit the website to know if it is up
       input_website = "https://allmediterranean.com"
       status = urllib.request.urlopen(input_website).getcode()
       #If it returns 200, the website is up
       if status != 200:
           #Call email function
           print("The website is down")
           

       else:
           print("The website is up")
           #Open url and create the hash code


  
monitor_website(1, 1)