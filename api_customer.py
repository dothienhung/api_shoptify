from os import system
import requests

base_url ="https://ecoomerce-lite.myshopify.com/"
api_key ="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"

def get(base_url =base_url,api ='',params =''):
    headers ={
        'Content-Type' : 'application/json',
        'X-Shopify-Access-Token' :api_key
    }
    url =base_url +api
    print("\n Excuting Get '%s'\n"%url)
    try:
        response =requests.get(url ,headers =headers,params =params)
        return response
    except :
        print("Lay api that bai",api)
        system.exit()

    

