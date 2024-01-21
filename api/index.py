from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'OK'


@app.route('/join', methods=['POST'])
def join():
      json_data = request.json
      roomCode  = json_data.get('roomCode')

      if not roomCode:
         return jsonify({"done": False, "error": "please specify all valeus"})
          
      try:
            endpoint = "https://jklm.fun/api/joinRoom"

            # Construct json data
            data = {'roomCode': roomCode}
          
            r = requests.post(url=endpoint, json=data)
            joinURL = r.json()['url']
          
            return jsonify({"done": True, "url": joinURL})
      except Exception as e:
             return jsonify({"done": False, "error": e})
          

@app.route('/create', methods=['POST']) # Create a room using requests
def create_room():
      json_data = request.json
    
      token  = json_data.get('creatorUserToken')
      public = json_data.get('isPublic')
      name   = json_data.get('name')
      gameId = json_data.get('gameId')

      if token is not None and public is not None and name is not None and gameId is not None:
    
          endpoint_create = "https://jklm.fun/api/startRoom"
          
          # Construct json data
          data = {'creatorUserToken' : token,
                            'isPublic' : public,
                            'name' : name,
                            'gameId' : gameId}
          
          res = requests.post(url = endpoint_create, json = create_data)
          
          if res.status_code != 200: 
              return jsonify({"done": False, "error": res.status_code})
              
          code = res.json()['roomCode']
          return jsonify({"done": True, "code": code})
          
      else:
             return jsonify({"done": False, "error": "please specify all valeus"})
