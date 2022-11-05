'''
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see
<https://www.gnu.org/licenses/>.
'''

import os
from time import sleep

allFilesInDir = os.listdir()
filesInDir = []
audioFiles = ["mp3", "wav", "ogg"]

# Find valid music files
for i in allFilesInDir:
    if((os.path.isfile(i)) and ("." in i)):
        fileNam = i.split(".")
        if((fileNam[1] in audioFiles) and (len(fileNam) == 2)):
            filesInDir.append(i)

# Put backslashes in front of spaces
iindex = 0
for i in filesInDir:
    if(" " in i):
        jindex = 0
        leni = len(i) - 1
        for j in i:
            if(jindex <= leni):
                if(j == " "):
                    filesInDir[iindex] = filesInDir[iindex][:jindex] + "\\" + filesInDir[iindex][jindex:]
                    jindex += 1
            jindex += 1
    iindex += 1

# Sort the playlist alphabetically
filesInDir = sorted(filesInDir)
#print(filesInDir)

# Clear terminal
os.system("clear")

# Display order of sounds
iindex = 1
print("ORDER:")
for i in filesInDir:
    print(str(iindex) + ":", i)
    iindex += 1

print("""\nUse \"l\" to loop, \"s\" to skip to next cue,
\"p\" to return to previous cue. Nothing just plays current.
You can also combine options to loop previous or next cue.
Use \"goto <value>\" to go to a specific file. This option doesn't
automatically play.
Use Ctrl + C during playback to stop, without playback quits.""")

sleep(1)

# Play Interface
try:
    iindex = 0
    while(True):
        print("\nNext,", filesInDir[iindex])
        prevnxtstr = "("
        if((iindex - 1) >= 0):
            prevnxtstr += "Prev: " + filesInDir[iindex-1]
            if((iindex + 1) != len(filesInDir)):
                prevnxtstr += ", "
            else:
                prevnxtstr += ")"
        if((iindex + 1) != len(filesInDir)):
            prevnxtstr += "Skip: " + filesInDir[iindex+1] + ")"
        print(prevnxtstr)

        cmd = "cvlc " + filesInDir[iindex] + " --play-and-exit -q"
        opt = input("Press Enter to Play (with options?)... ")
        if(opt == "p"):
            if((iindex - 1) < 0):
                print("I cannot do that. Playing current.")
            else:
                iindex -= 1
                cmd = "cvlc " + filesInDir[iindex] + " --play-and-exit -q"
                print("Playing", filesInDir[iindex])
        elif(opt == "l"):
            cmd += " -L"
            print("Loop Enabled")
        elif((opt == "pl") or (opt == "lp")):
            if((iindex - 1) < 0):
                print("I cannot do that. Looping current.")
                cmd += " -L"
            else:
                iindex -= 1
                cmd = "cvlc " + filesInDir[iindex] + " --play-and-exit -L -q"
                print("Playing", filesInDir[iindex], "on loop.")
        elif(opt == "s"):
            if((iindex + 1) == len(filesInDir)):
                print("I cannot do that. Playing current.")
            else:
                iindex += 1
                cmd = "cvlc " + filesInDir[iindex] + " --play-and-exit -q"
                print("Playing", filesInDir[iindex])
        elif((opt == "sl") or (opt == "ls")):
            if((iindex + 1) == len(filesInDir)):
                print("I cannot do that. Looping current.")
                cmd += " -L"
            else:
                iindex += 1
                cmd = "cvlc " + filesInDir[iindex] + " --play-and-exit -L -q"
                print("Playing", filesInDir[iindex], "on loop.")
        elif(" " in opt):
            opt = opt.split(" ")
            if(opt[0] == "goto"):
                try:
                    if((int(opt[1]) >= 1) and (int(opt[1]) <= len(filesInDir))):
                        iindex = int(opt[1]) - 1
                        print("OK. Going to file", opt[1] + ":", filesInDir[iindex])
                    else:
                        print("That value doesn't exist.")
                except ValueError:
                    print("That isn't a real value, silly!")
                except IndexError:
                    print("I don't know what to do! You didn't give me a value to goto!")
                continue
        
        os.system(cmd)
        if((iindex + 1) == len(filesInDir)):
            print("That's all. Goodbye!")
            break
        iindex += 1

    exit(0)
except KeyboardInterrupt:
    print("\nGoodbye!")
    exit(0)
