#!/usr/bin/python3

from papirus import PapirusTextPos
from papirus import Papirus
import time
import requests
from datetime import datetime


from bscscan import BscScan
bsc = BscScan("YOUR BSCSCAN API KEY")
bonfire_contract = "0x5e90253fbae4dab78aa351f4e6fed08a64ab5590" # BONFIRE contract address
tokenholder = "YOUR WALLET ADDRESS"


text=PapirusTextPos(False, rotation = 180)


text.AddText("1", 85,0 , Id="date", size =15)
text.AddText("BONFIRE", 55,15 , Id="name", size =24)
text.AddText("1", 0,40 ,Id="bfire_usd", size =17)
text.AddText("1", 0,60 ,Id="wallet", size =17)
text.AddText("1", 0,80 ,Id="balance", size =17)


def update():


    ##Get current time
    
    now = datetime.now()
    current_time = now.strftime("%d.%m. %H:%M")
    text.UpdateText("date", current_time)
 
 
    ## Get Bonfire price from Pancakeswap
    
    price = requests.get('https://api.pancakeswap.info/api/tokens/%s' % (bonfire_contract))
    price_dict=price.json()
    price= ("%.10f" % float(price_dict['data']['price']))
    print (price)
    text.UpdateText("bfire_usd","%s USD" % str(price))
    
    ## Get Wallet amount from BSCSCAN
    
    w=bsc.get_acc_balance_by_token_contract_address(bonfire_contract,tokenholder)
    w= float(w)/1000000000
    text.UpdateText("wallet", "Wallet: %s" % str(int((w))))
    
    ## Multiply price with wallet balance got get wallet price in USD
    balance = round((float(w)*float(price)),2)
    text.UpdateText("balance", "Value: %s USD" % str(balance))
    text.WriteAll()

    return 

data=update()

