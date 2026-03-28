#import pyttsx3
#def sintez_rate():
 #   engine = pyttsx3.init() # object creation
#
 #   # RATE
  #  rate = engine.getProperty('rate')   # getting details of current speaking rate
   # print (rate)                        # printing current voice rate
    #engine.setProperty('rate', 125)     # setting up new voice rate
#
 #   # VOLUME
  #  volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
   # print (volume)                          # printing current volume level
   # engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

    # VOICE
#    voices = engine.getProperty('voices')       # getting details of current voice
 #   #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
  #  print(voices)
   # engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

    #engine.say('привет')
    #engine.say('My current speaking rate is ' + str(rate))   
    #engine.runAndWait()


    # Saving Voice to a file
    # On Linux, make sure that 'espeak-ng' is installed 
#    engine.save_to_file('привет', 'test.mp3')
 #   engine.runAndWait()
  #  engine.stop()
#sintez_rate()

