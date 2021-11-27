import logging


def getError(res):
    if res.status_code != 200:
        print(res.headers)
        res = res.json()
        logging.error(f"{res['code']} | {res['message']}")

        
