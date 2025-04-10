import data
import sender_stand_request


def get_kit_body(name):
   current_body = data.kit_body.copy()
   current_body["name"] = name
   return current_body

def positive_assert(response,kit_name):
   assert response.status_code == 201
   assert response.json()['name']==kit_name

def negative_assert_code_400(kit_body):
   assert kit_body.status_code == 400

def test_symbol_1():
   name="a"
   auth_token=sender_stand_request.get_new_user_token()
   request=get_kit_body(name)
   response=sender_stand_request.post_new_client_kit(request,auth_token)
   positive_assert(response,name)

def test_symbol_511():
   name="AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
   auth_token=sender_stand_request.get_new_user_token()
   request=get_kit_body(name)
   response=sender_stand_request.post_new_client_kit(request,auth_token)
   positive_assert(response,name)

