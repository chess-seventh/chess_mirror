# Chess Mirror

This project is still under creation and modeling and review...
For my personal fun I will be coding all the project (or at least as much as I can in Python)

## Scope

I will be creating a magic mirror inspired by (http://www.instructables.com/id/How-to-Make-a-Magic-Mirror/) and (https://github.com/MichMich/MagicMirror). The idea is similar, to have a RPi Running a very lightweight system that gathers all the needed info to get prepared in the morning before heading to school / work. Maybe also drop in a couple of headlines from some big newspapers...

## Materials

As mentioned I will be using a RPi 2 B+ to make this project. I am currently using Raspbian Image for the OS but will most likely migrate to ARM Arch in a near future.

I will also use my Arduino's to poll my home temperature and outsides' as well. I am currently waiting a major arrival of components to set up a 'home-made security center'... (still defining it)

## Applications

### Xorg

I have a particular Fancy for Xmonad and it's simplicity as well as some of the Conky that we can put in the background and keep updating. I will be using xmonad, conky and some python applications as well as crontab to make my whole project run.

### Conky

Will be running my scripts on the wallpaper of the Xmonad's.


### My Scripts

#### Weather Poller

Current API's I have found and under testing is :
http://openweathermap.org/API
I have inspired myself from a python project existing already, but have been bringing some modifications to it.

#### Sms Sender

Still working on this part of the project as I would like to send an automated message to my GF's and Myself for rainy days or very cold days... Also why not an sms if the weather is good ? =)


#### TPG Poller

This year in class some of my mates had to work with the Transports here in GVA and create an app that can poll the information for some bus stations. I would like to show the next 3 - 5 buses and their expected time of arrival.


#### Calendar

Thinking about implementing this as well. A common calendar for me and my lady to have all events in one place. As well the upcoming TV Shows and when to see them... =)


#### News / RSS Feed

Well you know.


#### Twitter recent posts