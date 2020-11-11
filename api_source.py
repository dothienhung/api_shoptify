from os import system
import requests
import api_customer
import json
import csv

def get_customers_list():
    response =api_customer.get(api = 'admin/api/2020-10/customers.json')
    cus_list = json.dumps(response.json(),indent =4)
    return cus_list
def main():
    results = get_customers_list()
    if results :
        with open("api.json","w") as apijson :
            json.dump(results,apijson)
        with open("api.csv","w") as apicsv :
            json.dump(results,apicsv,indent =4 ,sort_keys=True)
            
            
        
        
        

main()
            

    