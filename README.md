# video-adder
Hey guys. This repo is a video adder which is my work-around for the current state of mods (videos not playing at the end unless there's a video block in keyframes.cfg). Not sure if this has already been made by someone or not. Read this to learn how to use it. It's pretty simple. Mods still don't always finish correctly, but if there's a .ogv file in the video directory, then it'll play at the end like it was supposed to. If you have suggestions for fixes, create an issue.

## I RECOMMEND BACKING UP YOUR MODS FOLDER BEFORE DOING THIS. IF A FIX COMES OUT AND MAKES THIS OBSELETE, THEN THE CHANGES MAY HARM YOU INSTEAD OF HELP YOU.

## update_keyframes.py
This file can be used to update an individual mod. You must put this outside of your mods folder (so in the app_userdata folder).
However, all it looks for is a folder called "mods", so you could put it somewhere else to test it first (like on your desktop or something, in a structure like C:\users\you\Desktop\test\mods. In this case, you'd put it in the test folder).
To change which mod it's updating, just change the "Mod_Name" variable at the top to whatever mod you want to update. 

## update_all_keyframes.py
This file will update all of the mods in the mods folder that it's outside of.
Same rules as above apply, other than the "Mod_Name" obviously.
