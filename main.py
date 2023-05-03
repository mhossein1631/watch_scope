import json
import requests
from discordwebhook import Discord
import sys

def check_datas(file1:str, file2:str, platform:str):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = set(f1.readlines())
        file2_lines = set(f2.readlines())
    if len(file1_lines) == len(file2_lines):
        print(f"{platform}:")
        print("No edit \n")
    else:
        print(f"{platform}: \n")
        extra_lines = file2_lines.difference(file1_lines)
        for line in extra_lines:
            print(line.strip())
            f = open(file1, "a")
            f.write(f"{line.strip()}\n")
            f.close()
            discord_data(platform)
            discord_data(line.strip())
def get_response_hackerone():
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/hackerone.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for obj in data:
            for scope in obj['relationships']['structured_scopes']['data']:
                if scope['attributes']['asset_type'] == 'URL' and scope['attributes']['eligible_for_bounty'] == True and \
                        scope['attributes']['eligible_for_submission'] == True:
                    f = open("temp-ho.txt", "a")
                    f.write(f"{scope['attributes']['asset_identifier']}\n")
                    f.close()
#get_response_hackerone()
#check_datas('platforms/hackerone.txt', 'platforms/temp-ho.txt', "Hackerone")

def get_response_bugcrowd():
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/bugcrowd.json"
    f = open("temp-bg.txt", "w")
    f.write("")
    f.close()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for target in data:
            for target1 in target['target_groups']:
                for scope in target1['targets']:
                    if scope['uri'] != None and scope['uri'] != '' and (scope['category'] == 'website' or scope['category'] == 'api') :
                        final = scope['uri'].encode('utf8')
                        final2 = str(final).replace('\'', '')
                        if final2.startswith("b"):
                            final2 = final2[1:]
                        f = open("temp-bg.txt", "a")
                        f.write(f"{final2}\n")
                        f.close()
    else:
            print(f"Error retrieving data: {response.status_code} - {response.reason}")

#get_response_bugcrowd()
#check_datas('bugcrowd.txt', 'temp-bg.txt', "Bugcrowd")

def get_response_intigrity():
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/intigriti.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for obj in data:
            for scope in obj['domains']:
                if scope['type'] == 1:
                    f = open("temp-in.txt", "a")
                    f.write(f"{scope['endpoint']}\n")
                    f.close()
#get_response_intigrity()
#check_datas('intigrity.txt', 'temp-in.txt', 'Intigrity')
def get_response_yeswehack():
    url = "https://raw.githubusercontent.com/Osb0rn3/bugbounty-targets/main/programs/yeswehack.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for obj in data:
            for scope in obj['scopes']:
                if scope['scope_type'] == 'web-application':
                    f = open("temp-ywh.txt", "a")
                    f.write(f"{scope['scope']}\n")
                    f.close()
#get_response_yeswehack()
#check_datas('yeswehack.txt', 'temp-ywh.txt', 'Yeswehack')

def discord_data(data):
    discord = Discord(url=sys.argv[1])
    discord.post(content=data)


get_response_hackerone()
check_datas('platforms/hackerone.txt', 'platforms/temp-ho.txt', "Hackerone")
get_response_bugcrowd()
check_datas('platforms/bugcrowd.txt', 'platforms/temp-bg.txt', "Bugcrowd")
get_response_intigrity()
check_datas('platforms/intigrity.txt', 'platforms/temp-in.txt', 'Intigrity')
get_response_yeswehack()
check_datas('platforms/yeswehack.txt', 'platforms/temp-ywh.txt', 'Yeswehack')