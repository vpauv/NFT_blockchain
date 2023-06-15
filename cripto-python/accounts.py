from algosdk import account

def generate_keypair(num_accts, accts):
    for _ in range(num_accts):
        acct = account.generate_account()
        print(acct)
        accts.append(acct)
        print(f"address: {acct[1]}")
        print(f"private key: {acct[0]}")
        print(f"mnemonic: {mnemonic.from_private_key(acct[0])}")

    return accts

def get_info_account(algod_client, addr):
    account_info = algod_client.account_info(addr).do()
    print("Account information:", account_info)
    return account_info




