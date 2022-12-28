from flask import Flask, request, jsonify, json
import json



api = Flask(__name__)

@api.route('/1', methods=['OPTIONS'],endpoint='1')
def get_companies():
    headers = request.headers
    auth = headers.get("Access-Control-Request-Headers")
    if auth == 'isen':
        decrease=False
        PATH="prix.json"
        with open(PATH, 'r') as outfile:
            prix=json.load(outfile)
        if (prix[1]["price"]<=0 or prix[2]["price"]<=0):
            decrease=True
        if decrease==False:
            bierre1()
        return "ok"

    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

@api.route('/2', methods=['OPTIONS'],endpoint='2')
def get_companies():
    headers = request.headers
    auth = headers.get("Access-Control-Request-Headers")
    if auth == 'isen':
        decrease=False
        PATH="prix.json"
        with open(PATH, 'r') as outfile:
            prix=json.load(outfile)   
        if (prix[0]["price"]<=0 or prix[2]["price"]<=0):
                decrease=True
        if decrease==False:
            bierre2()
        return "ok"

    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

@api.route('/3', methods=['OPTIONS'],endpoint='3')
def get_companies():
    headers = request.headers
    auth = headers.get("Access-Control-Request-Headers")
    if auth == 'isen':
        decrease=False
        PATH="prix.json"
        with open(PATH, 'r') as outfile:
            prix=json.load(outfile)
        if (prix[0]["price"]<=0 or prix[1]["price"]<=0):
            decrease=True
        if decrease==False:
            bierre3()
        return "ok"

    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


def bierre1():
    PATH="prix.json"
    with open(PATH, 'r') as outfile:
        prix=json.load(outfile)
    prix[0]["price"]=prix[0]["price"]*1.10
    prix[1]["price"]=prix[1]["price"]*0.90
    prix[2]["price"]=prix[2]["price"]*0.90

    for i in range(3):
        prix[i]["price"]=round(prix[i]["price"],2)


    with open(PATH, 'w') as outfile:
        json.dump(prix, outfile)

def bierre2():
    PATH="prix.json"
    with open(PATH, 'r') as outfile:
        prix=json.load(outfile)
    prix[0]["price"]=prix[0]["price"]*0.90
    prix[1]["price"]=prix[1]["price"]*1.10
    prix[2]["price"]=prix[2]["price"]*0.90


    for i in range(3):
        prix[i]["price"]=round(prix[i]["price"],2)


    with open(PATH, 'w') as outfile:
        json.dump(prix, outfile)

def bierre3():
    PATH="prix.json"
    with open(PATH, 'r') as outfile:
        prix=json.load(outfile)
    prix[0]["price"]=prix[0]["price"]*0.90
    prix[1]["price"]=prix[1]["price"]*0.90
    prix[2]["price"]=prix[2]["price"]*1.10


    for i in range(3):
        prix[i]["price"]=round(prix[i]["price"],2)


    with open(PATH, 'w') as outfile:
        json.dump(prix, outfile)
"""
@api.route('/edit_sheet', methods=['GET'],endpoint='edit')
def get_companies():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    fiche= headers.get("sheet_dir")
    goal=headers.get("data_goal")
    content=headers.get("data_content")
    contentSummary=headers.get("data_contentSummary")
    expectedResults=headers.get("data_expectedResults")
    api_key_user=headers.get("api_key_user")
    if auth == 'asoidewfoef':
        print("ok")
        statut,message=edit_sheet.edit(goal,content,contentSummary,expectedResults,api_key_user,fiche)
        if statut=="ok":
            return json.dumps(message)
        else :
            return jsonify(f'message": ERROR: {message}"'), 401
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


"""
if __name__ == '__main__':
    api.run()