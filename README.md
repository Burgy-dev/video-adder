# video-adder
Hey guys. This repo contains video adders which is my work-around for the current state of mods (videos not playing at the end unless there's a video block in keyframes.cfg). Not sure if this has already been made by someone or not. Read this to learn how to use it. It's pretty simple. Mods still don't always finish correctly, but if there's a .ogv file in the video directory, then it'll play at the end like it was supposed to. If you have suggestions for fixes, create an issue. I wasn't able to figure out how to get the mods to end if the song was still playing after the climax video finished, so that bugs out and doesn't allow the mod to finish and give you your score. If you know how to fix this, please lmk.

### ⚠️ Warning
  I RECOMMEND BACKING UP YOUR MODS FOLDER BEFORE DOING THIS. IF A FIX COMES OUT AND MAKES THIS OBSOLETE, THEN THE CHANGES MAY HARM YOU INSTEAD OF HELP YOU.

### 🔔 Note
  You need to have python installed for these to work. Should be pretty easy if you don't have it installed already.

## check_for_video.py
- This can be used to check if any of your mods already have a video block in your keyframes.cfg file. If it does, it'll print out the mod name. You'll want to exclude those by including them in the exclude list at the top of the update_all_keyframes.py file.

## update_keyframes.py
- This file can be used to update an individual mod. You must put this outside of your mods folder (so in the app_userdata folder).
- However, all it looks for is a folder called "mods", so you could put it somewhere else to test it first (like on your desktop or something, in a structure like ~\Desktop\test\mods. In this case, you'd put it in the test folder).
- To change which mod it's updating, just change the "Mod_Name" variable at the top to whatever mod you want to update. 

## update_all_keyframes.py
- This file will update all of the mods in the mods folder that it's outside of.
- Same rules as above apply, other than the "Mod_Name" obviously.
- Only difference is there is an exclude list at the top that you can add mods to that you have either already fixed, or mods that already had video blocks in the keyframes.cfg file.

## Error printing
Both python scripts have pretty verbose error printing. Not all mods will have videos, and some mods don't have .ogv's and instead have .webm's or something. You'll need to convert these yourself, as the scripts look for .ogv files. Converters are easy to find.
