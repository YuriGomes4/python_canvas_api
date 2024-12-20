import json
from time import sleep
import requests

class auth():

    def __init__(self, dominio, access_token="", print_error=True):
        self.access_token = access_token
        self.base_url = f"https://{dominio}"
        self.print_error = print_error

    def request(self, method="GET", url="", headers=None, params=None, data=None):

        req_params = params if params != None else {}
        req_headers = headers if headers != None else {}
        req_data = data if data != None else {}

        while True:

            match method:
                case "GET":
                    response = requests.get(url=url, params=req_params, headers=req_headers, data=req_data)
                case "PUT":
                    response = requests.put(url=url, params=req_params, headers=req_headers, data=req_data)
                case "POST":
                    response = requests.post(url=url, params=req_params, headers=req_headers, data=req_data)
                case "DELETE":
                    response = requests.delete(url=url, params=req_params, headers=req_headers, data=req_data)
                case "HEAD":
                    response = requests.head(url=url, params=req_params, headers=req_headers, data=req_data)
                case "OPTIONS":
                    response = requests.options(url=url, params=req_params, headers=req_headers, data=req_data)

            if response.status_code == 200 or response.status_code == 201:
                return response
            elif response.status_code != 429:
                if self.print_error:
                    print(f"""Erro no retorno da API do Canvas
Mensagem: {response.json()['message'] if 'message' in response.json() else ""}
URL: {url}
Metodo: {method}
Parametros: {req_params}
Headers: {req_headers}
Data: {req_data}
Resposta JSON: {response.json()}""")
                break
            else:
                sleep(5)

class accounts(auth):

    def delete_a_user_from_the_root_account(self, account_id, user_id, **kwargs) -> dict:
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/api/v1/accounts/{account_id}/users/{user_id}"

        params = {}

        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }

        arg_dict = {}

        if 'arg_dict' in kwargs:
            arg_dict = kwargs['arg_dict']

        if kwargs != {}:
            for key, value in kwargs.items():
                if key != 'arg_dict':
                    if key in arg_dict:
                        params[arg_dict[key]] = value
                    else:
                        params[key] = value

        response = self.request("DELETE", url=url, headers=headers)

        if response:

            return response.json()
        
        else:
            return {}
        
class users(auth):

    def list_users_in_account(self, account_id, **kwargs) -> dict:
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return []

        url = self.base_url+f"/api/v1/accounts/{account_id}/users"

        params = {}

        headers = {
            'Authorization': f'Bearer {self.access_token}',
        }

        arg_dict = {}

        if 'arg_dict' in kwargs:
            arg_dict = kwargs['arg_dict']

        if kwargs != {}:
            for key, value in kwargs.items():
                if key != 'arg_dict':
                    if key in arg_dict:
                        params[arg_dict[key]] = value
                    else:
                        params[key] = value

        response = self.request("GET", url=url, headers=headers)

        if response:

            return response.json()
        
        else:
            return {}