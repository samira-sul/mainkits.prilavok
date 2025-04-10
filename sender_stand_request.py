import configuration
import requests
import data 

def post_new_client_kit(kit_body,auth_token):
   headers=data.headers.copy()
   headers["Authorization"]="Bearer " + auth_token
   response=requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=data.kit_body.copy(),
                         headers=data.headers)
   return response

def get_new_user_token():
   user_response=requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body.copy(),
                         headers=data.headers)
   assert user_response.status_code == 201
   assert user_response.json()["authToken"] != ""
   return user_response.json()["authToken"]
