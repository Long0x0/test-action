import requests


def send_serverChan_message(text, desp, serverChan_key):
    r = requests.get("https://sc.ftqq.com/" + serverChan_key
                     + ".send?text=" + text + "&desp=" + desp).json()
    return r["errno"] == 0
