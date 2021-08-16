#what is new
#you can ask 'jarvis do you know  coding anna' or 'what is 1+1' like maths and science question
#updated to a text news for you guys.
#it is made Bhuvanesh.dev and made in a mobile
#THIS OUR TEXT ASSISTANT
#IMPORT's
import psutil 
import wolframalpha
import random
import webbrowser
import datetime
import wikipedia
from gnewsclient import gnewsclient 

#______________________________________  

print('          		VERSION:(1.2.5)\n')
#it say goodmorning ,ect.

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 6 and currentH < 12:
        print('  	jarvis:Hi Sir,Good Morning!')

    if currentH >= 12 and currentH < 16:
        print('	jarvis:Hi Sir,Good Afternoon!')

    if currentH >= 16 and currentH !=24:
        print('	jarvis:Hi Sir,Good Evening!')

#show's time
greetMe()
print('	The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))
#jarvis
print('	I am your assistant, jarvis.')
#input 


while True: 
    q= input("___________________________________________________________\n user:"	).lower() 
    word='jarvis'
    query= q.replace(word, "")   
    word3='who is'
    query =query.replace(word3,'')
    
    
    if q==word and query=='':
    	print('	jarvis:yes sir tell me')
#says hello
    elif  'hi' == query or  'hello' in query:
       print('	jarvis:HELLO,SIR ')	
#______________________________________       
    
#______________________________________
 #says time          
    elif 'time' in query:
    	       print('	jarvis: The current time is '+(str(datetime.datetime.now().strftime('%I:%M %p'))))   
#______________________________________
#tells i love you												
    elif "i love you" in query:
       print ('	jarvis:I LOVE YOU TOO...') #______________________________________ 
#says bye to us				    
    
#show's wikipedia
    
#______________________________________
#'open google	 	    	    	   	  	     
    elif 'open google' in query:
            print('	opening google....')
            webbrowser.open('https://www.google.com/search?gs_ssp=eJzj4tVP1zc0', new=2)
#______________________________________
#open youtube 
    elif 'open youtube' in query:
            print('	jarvis:opening youtube....')
            webbrowser.open('https://www.youtube.com/', new=2)
#show's weather
#______________________________________    
#show's news      
    
    elif 'search on google' in query or 'QUESTION' in query :
           x=input('	jarvis:WHAT IS YOUR QUESTIONS: ')
           webbrowser.open('https://www.google.com/search?q='+x)
#______________________________________
#search on youtube           
    elif 'search on youtube' in query:  
              y=input('	jarvis:Enter your query to search in youtube: ')
              webbrowser.open('https://m.youtube.com/results?search_query='+y)
#______________________________________
    #open's amazon
    elif 'amazon' in query:
    	            print ('	jarvis:opening amazon....')
    	            webbrowser.open('https://www.amazon.in/') 
#______________________________________
    #say's date	 
    elif 'date' in query:
             d = datetime.datetime.today()
             print('	jarvis:'+d.strftime("%d %B %Y"))
#______________________________________
    
    elif "what\'s up" in query or "how are you" in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        print('	jarvis:'+random.choice(stMsgs))
#______________________________________        
    elif "where is" in query:
        location = query.replace('where is ','')
        print("Hold on   I will show you where " + location + " is.")
        webbrowser.open("http://maps.google.com/?q=" + location)
#______________________________________    
    elif 'where i am ' in query:
    	webbrowser.open("https://www.google.com/maps/place/" + 'where iam')
#______________________________________ 
    elif 'who are you' in query or 'what is your name' in query :
    	print('	sir Iam your assistant ,JARVIS.')
#______________________________________
    elif 'say' in query:
    	word1='say'
    	say= query.replace(word1, "")
    	print('	jarvis:'+say)
    elif 'wikipedia' in query:
            	    				print('	jarvis:Searching Wikipedia...')            	
            	    				query = query.replace("wikipedia", "")
            	    				results = wikipedia.summary(query, sentences=2)
            	    				print("		According to Wikipedia")
            	    			
            	    				print(results)
#______________________________________
    elif 'are you ok' in query :
    	print('	jarvis:yes Iam ok')
#______________________________________
    elif 'super' in query or 'great' in query or 'welldone' in query or 'good job' in query :
    	thanks=['Thanks',"it's my pleasure",'Iam always your assistant sir']
    	print('	jarvis:'+random.choice(thanks))
#______________________________________
    elif "news" in query:
     try:		    
			    print('	jarvis: Yes sir loading')
			    client = gnewsclient.NewsClient(language='tamil',  

                                location='india',  

                                topic='tamil nadu',  

                                max_results=3)
                                
			    news_list = client.get_news()
			    for item in news_list:
			    	print('____________________________________________________________')
			    	print("Headlines: ", item['title']+'\n')
			    	print("Link : ", item['link']) 
			    	print('____________________________________________________________') 		    
     except:
      	print ('			An error occured')
      	webbrowser.open('https://youtu.be/yKMT5aJl7yI')
      	
    elif 'battery' in query :
    	battery = psutil.sensors_battery()
    	print("	jarvis:Battery percentage : ", battery.percent,'%')    
    	
    elif 'bye' in query or 'quit' in query or 'close' in query or 'exit' in query:
    	               print ('	jarvis:bye sir')
    	               exit()
    	
 #______________________________________   	         
    
    else:
     
      		try:
        
        			print('	jarvis:searching....')
        			app_id = 'Your app id'
        			client = wolframalpha.Client(app_id) 
        			res = client.query(query)
        			answer = next(res.results).text
        			print('	Got it sir')
        			print('	jarvis:'+answer)
        
      		
      		except:
       			print ("	jarvis: Iam showing google")
       			webbrowser.open('https://www.google.com/search?q='+query)     		
