import requests
import json
import pprint

def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "get_terms",
        "params": [{1:['agreed',
 'idiotic chris coons referring iran key ally leftist dem completely lost tiny '
 'little marbles shout death america amp democrats defend brink war approached '
 'wimpy president give trump',
 'line trump rally tonight',
 'absolute empty suit coward career political whore lying swamp creature',
 'president obama pennsylvania lost manufacturing jobs president returns pa '
 'tonight amidst economic transformation nothing short extraordinary pa '
 'booming thanks',
 'everybody wants take credit revived economy changed many disastrous obama '
 'policies hindered american economic growth',
 'may god bless president trump vice president pence today work america keep '
 'safe lord',
 'sheepdog trump says favors abortion exceptions cases rape incest mother life '
 '#maga ifb via',
 'quandary #nevertrumpers side mitt romney justin amash enjoy show #nevertrump '
 'civil war justin amash calls trump impeachment mitt romney counters case'] }],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    pprint.pprint(sorted(response["result"][0]["topWords"]))


if __name__ == "__main__":
    main()