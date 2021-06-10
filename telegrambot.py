import requests as rq
import json
import configparser as cfg

BASE_URL = "https://api.telegram.org/"
parser = cfg.ConfigParser()
parser.read("config.cfg")
bot_token = parser.get('cred','token')

# print(json_data)

def download(url):
    try:
        file_resp = rq.get(url)
        open('audio_files/audio.oga','wb').write(file_resp.content)
        return True
    except:
        return False

def simplesend(resp,chat_id="CHAT_ID"):
    url = f"{BASE_URL}{bot_token}/sendMessage?chat_id={chat_id}&text={resp}"
    rq.get(url)

def write_json(data, filename='history.json'):
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)

def fetchAudio():
    # try:
        # print(BASE_URL+str(bot_token)+"/getUpdates")
        resp = rq.get(BASE_URL+str(bot_token)+"/getUpdates")
        # print(BASE_URL+str(bot_token)+"/getUpdates")
        json_data = resp.json()['result'][-1]
        if json_data["message"].get("voice",False):

            file_id = json_data["message"].get("voice").get("file_id")
            # print(file_id)
            with open('history.json') as json_file:
                data = json.load(json_file)
                if file_id!=data['file_id']:
                    file_url = f"https://api.telegram.org/{bot_token}/getFile?file_id={file_id}"
                    file_resp = rq.get(file_url)
                    file_json_data = file_resp.json()
                    file_path = file_json_data['result'].get("file_path")
                    # print(file_path)
                    file_download_url = f"https://api.telegram.org/file/{bot_token}/{file_path}"
                    # print(file_download_url)
                    if download(file_download_url):
                        print("[ Download Successful ]")
                        data['file_id'] = file_id
                        write_json(data)
                        return True, file_path.split("/")[-1]
                    else:
                        raise ValueError('Some Error Occured.')
                        return False,None
                else:
                    return False,None

    # except:
    #     print("Some Error Occured.")

# fetchAudio()
