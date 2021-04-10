import smtplib
import speech_recognition as SRG 
import time
print("*~*~*~*~*~*|~|*|WELCOME TO SPEAKMAIL|*|~|*~*~*~*~*~*")
passphrase=SRG.Recognizer()
with SRG.Microphone() as p:
     
    print("Speakout your passphrase...")
     
    audio_input = passphrase.record(p, duration=3)
    
    
    try:
        text_output_p=passphrase.recognize_google(audio_input)
        
        
        
 
        
    except:
           print("Couldn't process the audio input.")
passphrase=text_output_p
print("THE PASSPHRASE SPOKEN OUT IS ",passphrase)
if (passphrase=="easy mail"):
    print("Access Granted...!!!")
    print("Welcome Back")
    import smtplib 
    gmailaddress = "dineshprabhu0705@gmail.com"
    gmailpassword = "Nhce2019"
    mailto = SRG.Recognizer()
    with SRG.Microphone() as m:
        print("~~~***|RECIPIENT LIST|***~~~")
        print("Choose the recipient")
        print("1)Rohit")
        print("2)Dinesh")
     
        audio_input = mailto.record(m, duration=3)
    
    
        try:
            text_output_m = mailto.recognize_google(audio_input)
        
            print("THE RECIPIENT SELECTED IS ",text_output_m)
        
 
        
        except:
            print("Couldn't process the audio input.")
    mailto=text_output_m
    
    if (mailto=="Surya"):
        mailto=("surya47sara@gmail.com")
    elif(mailto=="Dinesh"):
        mailto=("dineshprabhu0705@yahoo.com")
    else:
        print("Recipient not found")
    msg =SRG.Recognizer()
    with SRG.Microphone() as s:
        print("Speakout the message")
     
        audio_input = msg.record(s, duration=7)
        
    
        try:
            text_output_s = msg.recognize_google(audio_input)
            
            print(text_output_s)
            
 
            
        except:
           print("Couldn't process the audio input.")
    msg=(text_output_s)
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto, msg)
    print(" \n Sent!")
    mailServer.quit()
       
    
else:
    print("Wrong Passphrase.....Access Denied....!!!")





