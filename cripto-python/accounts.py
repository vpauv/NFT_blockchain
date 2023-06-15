from algosdk import account

def generate_keypair(num_accts, accts):
    for _ in range(num_accts):
        acct = account.generate_account()
        accts.append(acct)
        print(f"address: {acct.address}")
        print(f"private key: {acct.private_key}")
        #print(f"mnemonic: {mnemonic.from_private_key(account.private_key)}")
        print(f"mnemonic: {acct.secret_key_to_mnemonic(acct.sk)}")

    return accts

def get_info_account(algod_client, addr):
    account_info = algod_client.account_info(addr).do()
    print("Account information:", account_info)
    return account_info




