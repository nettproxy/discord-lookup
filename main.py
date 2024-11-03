import requests
import os, colorama, time, ctypes
from logger import debug, info, error, bridge, success
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

print("\n".join(f"\033[38;2;255;{int(255 * i / 5)};0m{line}\033[0m" for i, line in enumerate([
    '██████╗  ██████╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗',
    '██╔══██╗██╔════╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗',
    '██║  ██║██║         ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝',
    '██║  ██║██║         ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝',
    '██████╔╝╚██████╗    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║',
    '╚═════╝  ╚═════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝'
])) + "\033[0m")
ctypes.windll.kernel32.SetConsoleTitleW("Discord Lookup made by monokai <3")
print(Fore.YELLOW + '╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╗')
print(Fore.YELLOW + f'║                              ║{Fore.LIGHTYELLOW_EX}       MENU OPTIONS{Fore.RED}       ║                              ║')
print(Fore.YELLOW + '╠══════════════════════════════╬══════════════════════════╬══════════════════════════════╣')
print(Fore.RED + '║     [01] USER LOOKUP         ║     [02] BOT LOOKUP      ║     [03] GUILD LOOKUP        ║')
print(Fore.YELLOW + '╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╝')

def check_token_valid(token):
    r = requests.get('https://discord.com/api/v10/users/849566937846382614', headers={"Authorization": "Bot " + token})
    if r.status_code == 200:
        success("Valid token")
    else:
        error("Invalid token")
        exit()

choice = input(Fore.LIGHTCYAN_EX + "> ")

if choice == '1':
    os.system("cls")
    dc_auth = input(Fore.LIGHTGREEN_EX + "[AUTHORIZATION] " + Fore.WHITE + "Enter any discord bot token (Used for acccessing Discord API): ")
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
    if request.status_code == 200:
        data = request.json()
        info(f"User Found!")
        print(" ")
        success("Username: " + (data["username"]) if data['username'] and data['username'] else 'No username')
        success("Display Name: " + (data["global_name"]) if data['global_name'] and data['global_name'] else 'No display name')
        success("Created At: " + snowflake_to_date(data['id']).strftime('%Y-%m-%d %H:%M:%S'))
        # success("Discriminator: " + str(data["discriminator"]))
        success("ID: " + data["id"])
        # success("Avatar: " + (data['avatar'] if data['avatar'] and data['avatar'] else 'No avatar'))
        # success("Banner: " + (data['banner'] if data['banner'] and data['banner'] else 'No banner'))
        success("Clan Tag: " + (data['clan']['tag'] if data['clan'] and data['clan']['tag'] else 'No clan'))
        success("Clan Guild ID: " + (data['clan']['identity_guild_id'] if data['clan'] and data['clan']['identity_guild_id'] else 'No clan guild ID'))
        # success("Nitro: " + nitro_types[data['premium_type']])
    else:
        error(f"User Not Found!")
elif choice == '2':
    os.system("cls")
    dc_auth = input(Fore.LIGHTGREEN_EX + "[AUTHORIZATION] " + Fore.WHITE + "Enter any discord bot token (Used for acccessing Discord API): ")
    check_token_valid(dc_auth)
    bridge("Getting API...")
    time.sleep(1)
    id = input(Fore.YELLOW + "[DISCORD LOOKUP] " + Fore.WHITE + "Enter Bot ID: ")
    request = requests.get(f'https://canary.discord.com/api/v10/applications/{id}/rpc', headers={"Authorization": "Bot " + dc_auth, "Content-Type": "application/json"})
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
