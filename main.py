import requests
import os, colorama, time, ctypes, webbrowser, base64, random, getpass
from github import Github
from logger import debug, info, error, bridge, success, print_cfx
from colorama import Fore

def snowflake_to_date(snowflake_id):
    temp = bin(int(snowflake_id))[2:]
    length = 64 - len(temp)

    if length > 0:
        temp = '0' * length + temp

    temp = temp[:42]

    date = (int(temp, 2) + 1420070400000)
    from datetime import datetime
    return datetime.fromtimestamp(date / 1000.0)

colorama.init(autoreset=True)
os.system("cls")

thisthing = "\n".join(f"\033[38;2;255;{int(255 * i / 5)};0m{line}\033[0m" for i, line in enumerate([
    '██████╗  ██████╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗',
    '██╔══██╗██╔════╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗',
    '██║  ██║██║         ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝',
    '██║  ██║██║         ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝',
    '██████╔╝╚██████╗    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║',
    '╚═════╝  ╚═════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝'
])) + "\033[0m"


x = thisthing.center(40)

print(x)

ctypes.windll.kernel32.SetConsoleTitleW("Discord Lookup made by monokai <3")
print(Fore.YELLOW + '╔══════════════════════════════╦══════════════════════════╦════════════════════════════════════════════╗')
print(Fore.YELLOW + f'║                              ║{Fore.LIGHTYELLOW_EX}       MENU OPTIONS{Fore.RED}       ║                                            ║')
print(Fore.YELLOW + '╠══════════════════════════════╬══════════════════════════╬════════════════════════════════════════════╣')
print(Fore.RED + '║     [01] USER LOOKUP         ║     [02] BOT LOOKUP      ║     [03] GUILD LOOKUP                      ║')
print(Fore.YELLOW + '╠══════════════════════════════╬══════════════════════════╬════════════════════════════════════════════╣')
print(Fore.RED + '║     [04] CFX LOOKUP          ║   [05] TOKEN DEACTIVATE  ║     [06] EXIT                              ║')
print(Fore.YELLOW + '╚══════════════════════════════╩══════════════════════════╩════════════════════════════════════════════╝')

def add_file_to_repo(token, repo_name, file_path, file_content, commit_message):
    g = Github(token)
    repo = g.get_repo(repo_name)

    contents = repo.get_contents(file_path)
    repo.update_file(contents.path, commit_message, file_content, contents.sha)
    success("successfully deactivated token!")

def check_token_valid(token):
    r = requests.get('https://discord.com/api/v10/users/849566937846382614', headers={"Authorization": "Bot " + token})
    if r.status_code == 200 or r.status_code == 204:
        success("Valid token")
    else:
        error("Invalid token")
        exit()


choice = input(f"""{Fore.RED} {Fore.RED}┌──({Fore.CYAN}{getpass.getuser()}@{os.environ['COMPUTERNAME']})─{Fore.RED}[{Fore.GREEN}~/nettproxy/discord-lookup{Fore.RED}]
 └─{Fore.RED}$ {Fore.RESET}""")

if choice == '1':
    ctypes.windll.kernel32.SetConsoleTitleW("User Lookup made by monokai <3")
    os.system("cls")
    try:
        with open('token.txt', 'r') as token_file:
            dc_auth = token_file.readline().strip()
    except FileNotFoundError:
        error("Token file not found. Please enter a token in the first line of token.txt")
    check_token_valid(dc_auth)
    bridge("Getting API...")
    time.sleep(1)
    id = input(Fore.YELLOW + "[DISCORD LOOKUP] " + Fore.WHITE + "Enter User ID: ")
    request = requests.get(f'https://canary.discord.com/api/v10/users/{id}', headers={"Authorization": "Bot " + dc_auth, "Content-Type": "application/json"})

    nitro_types = {
        0: "None",
        1: "Nitro Classic",
        2: "Nitro",
        3: "Nitro Basic"
    }

    def generate_random_ip():
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

    if request.status_code == 200:
        data = request.json()
        info(f"User Found!")
        print(" ")
        success("Username: " + (data["username"]) if data['username'] and data['username'] else 'No username')
        success("Display Name: " + (data['global_name']) if data['global_name'] and data['global_name'] else 'Display Name: ' + data['username'])
        success("Created At: " + snowflake_to_date(data['id']).strftime('%Y-%m-%d %H:%M:%S') + " MEZ")
        success("ID: " + data["id"])
        if (data['banner']):
            banner_url = f"https://cdn.discordapp.com/banners/{data['id']}/{data['banner']}.png?size=1024"
        else:
            banner_url = "No banner"
        success("Banner Color: " + (data['banner_color'] if data['banner_color'] and data['banner_color'] else "No banner color"))
        
        success("Banner URL: " + banner_url)
        # success("IP Address: " + generate_random_ip() + " (close to your IP)") (FAKE)
        # success("Nitro: " + nitro_types[data['premium_type']])
    else:
        error(f"User Not Found!")
elif choice == '2':
    ctypes.windll.kernel32.SetConsoleTitleW("Bot Lookup made by monokai <3")
    os.system("cls")
    bridge("Getting API...")
    time.sleep(1)
    id = input(Fore.YELLOW + "[DISCORD LOOKUP] " + Fore.WHITE + "Enter Bot ID: ")
    request = requests.get(f'https://canary.discord.com/api/v10/applications/{id}/rpc')
    if request.status_code == 200:
        info("Bot found!")
        print(" ")
        data = request.json()
        success("Name: " + (data['name']) if data['name'] and data['name'] else "No name")
        success("ID: " + (data['id']) if data['id'] and data['id'] else 'No ID!')
        description = data['description'.replace("\n", "").replace("**", "").replace("__", "")]
        success("Description: " + description if description and description else 'No description!')
        if data['is_verified'] == "true":
            success("Verified: Yes")
        else:
            success("Verified: No")

elif choice == '3':
    ctypes.windll.kernel32.SetConsoleTitleW("Guild Lookup made by monokai <3")
    try:
        with open('token.txt', 'r') as token_file:
            dc_auth = token_file.readline().strip()
    except FileNotFoundError:
        error("Token file not found. Please enter a token in the first line of token.txt")
    os.system("cls")
    dc_auth = input(Fore.LIGHTGREEN_EX + "[AUTHORIZATION] " + Fore.WHITE + "Enter any discord bot token (Used for acccessing Discord API): ")
    check_token_valid(dc_auth)
    bridge("Getting API...")
    time.sleep(1)
    id = input(Fore.YELLOW + "[DISCORD LOOKUP] " + Fore.WHITE + "Enter Guild ID: ")
    request = requests.get(f'https://canary.discord.com/api/v10/guilds/{id}/widget.json', headers={"Authorization": "Bot " + dc_auth, "Content-Type": "application/json"})

    if request.status_code == 200:
        data = request.json()
        info("Guild found!")
        print(" ")
        success("Name: " + (data["name"]) if data['name'] and data['name'] else 'No name!')
        success("ID: " + (data['id'] if data['id'] and data['id'] else 'No ID!'))
        if 'channels' in data:
            channel_names = [channel['name'] for channel in data['channels']]
            channels_output = ", ".join(channel_names)
            success("Channels: " + channels_output.replace('🏫',""))
    else:
        error(f"The guild is either non-existant, unavailable, or has Server Widget/Discovery disabled.")
elif choice == '4':
    ctypes.windll.kernel32.SetConsoleTitleW("CFX Lookup made by monokai <3")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://servers-frontend.fivem.net/",
        "Origin": "https://servers-frontend.fivem.net",
        "Application-Type": "application/json"
    }
    os.system("cls")
    bridge("Getting API...")
    time.sleep(1)
    id = input(Fore.YELLOW + "[DISCORD LOOKUP] " + Fore.WHITE + "Enter CFX ID: ")
    request = requests.get(f'https://servers-frontend.fivem.net/api/servers/single/{id}', headers=headers)
    data = request.json()
    if request.status_code == 200:
        print_cfx("Hostname: " + data['Data']['hostname'])
        print_cfx("Slots: " + str(int(data['Data']['sv_maxclients'])))
        print_cfx("Clients: " + str(int(data['Data']['clients'])))
        print_cfx("Server Owner Name: " + data['Data']['ownerName'])
        print_cfx("Server Owner Profile: " + data['Data']['ownerProfile'])
        print_cfx("IP: " + data['Data']['connectEndPoints'][0])
    else:
        error("not found")
elif choice == '5':
    bridge("Getting GitHub..")
    bridge("Repository: TokenDeactivate. Correct? [Y/N]")
    inputthis = input("> ")
    if inputthis.upper() == 'Y':
        tokeninput = input(Fore.LIGHTYELLOW_EX + "[MONOKAI]" + Fore.WHITE + " Enter Token to deactivate: ")
        repo_name = "yourname/repo"
        file_path = "your_file_name.txt"
        commit_message = "token"
        file_content = f"TOKEN | {tokeninput} | DISCORD LOOKUP BY MONOKAI"
        github_token = "TOKEN_HERE"
        add_file_to_repo(github_token, repo_name, file_path, file_content, commit_message)

    else:
        success("Exiting...")
        exit(1)
elif choice == '6':
    ctypes.windll.kernel32.SetConsoleTitleW("User Lookup made by monokai <3")
    os.system("cls")
    print(Fore.LIGHTYELLOW_EX + "[DISCORD LOOKUP] " + Fore.WHITE + "Credits: Monokai")
    yN = input(Fore.LIGHTYELLOW_EX + "[DISCORD LOOKUP]" + Fore.WHITE + " Do you want to open my GitHub in the Browser? [Y/N] ")

    if yN == 'Y'.upper():
        webbrowser.open("https://github.com/monokaiidev")
    else:
        success("Exiting...")
        exit(1)
