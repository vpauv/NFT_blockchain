#from algosdk import AlgodClient
from algosdk.v2client import algod
import accounts, assets, transfer, contract, utils
from pyteal import Mode, compileTeal
import sys

#Creacion de cuentas
def create_account(num_accts, accts):
    accts = accounts.generate_keypair(num_accts, accts)

#Creacion de NFT sin contrato
def create_NFT_no_contract(accts):
    nft_id = assets.create_NFT(accts[0], metadata)

#Ver saldo de la cuenta
def account_balance(accts):
    account_info: Dict[str, Any] = algod_client.account_info(accts[0][1])
    print(f"Account balance: {account_info.get('amount')} microAlgos")


#Detalles de la transacción para transferencia de nft sin contrato
def NFT_transfer(accts):
    sender_acct = accts[0]
    receiver_acct = accts[1]
    txid = transfer.transfer_nft(sender_acct,receiver_acct,nft_id)
    print("Transaction sent. No contract NFT transfer transaction ID:", txid)

#Eliminacion del NFT sin contrato
def NFT_delete(accts):
    acct_delete = accts[0]
    txid = assets.delete_nft(acct_delete, nft_id)
    print("Transaction sent. No contract NFT delete transaction ID:", txid)

def create_client():
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_server = "http://localhost"
    algod_port = 4001
    algod_client = algod.AlgodClient(algod_token, algod_server, algod_port)

    return algod_client

#Creamos un cliente para conectarnos con la red de prueba (Tesnet) de Algorand
#y asi poder realizar operaciones
algod_client = create_client()

accts = []
num_accts = 2

# Construir el diccionario de metadata
metadata = {
    "name": "My Artwork",
    "description": "A beautiful artwork created by me",
    "image": "https://drive.google.com/file/d/1zVCb4mK7JugKOGQjOTz5cphbHgPeup7E/view?usp=drive_link",
    "creator": "John Doe",
    "year": 2022
}


action = 1

while action == 1:
    
    print("")
    print("1. Create an account")
    print("2. Create NFT without contract")
    print("3. NFT transfer")
    print("4. Account balance")
    print("5. Delete NFT")
    print("6. Exit")

    action = int(input("Select an action: "))

    print("")

    if action == 1:
        create_account(num_accts, accts)
        action = 1;
    elif action == 2:
        create_NFT_no_contract(accts)
        action = 1;
    elif action == 3:
        NFT_transfer(accts)
        action = 1;
    elif action == 4:
        account_balance(accts)
        action = 1;
    elif action == 5:
        NFT_delete(accts)
        action = 1;
    elif action == 6:
        sys.exit()
        action = 1;
    else:
        print("Invalid option...")
        action = 1;



# now, trying to fetch the asset info should result in an error
try:
    info = algod_client.asset_info(nft_id)
except Exception as e:
    print("Expected Error:", e)



#address: 5X7HTSTGUJTMBG3IV4SRG2NPBNLU3YKMKOI4OMGYG3UYXG4JQE3GV7H57A
#private key: wQdCJj8SpdUS+lFhKT3IYERqZ09HKh5MOAA+8lLupiXt/nnKZqJmwJtoryUTaa8LV03hTFORxzDYNumLm4mBNg== 
#mnemonic: wealth amount nasty catalog enforce rely spatial faint club visa goat ecology stand supply denial clean long thrive abandon catalog planet romance coffee ability noise

