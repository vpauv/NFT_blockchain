from algosdk import transaction, encoding

def transfer_nft(algod_client,acct1,acct2,created_asset):
    sp = algod_client.suggested_params()
    # Create transfer transaction
    xfer_txn = transaction.AssetTransferTxn(
        sender=acct1.address,
        sp=sp,
        receiver=acct2.address,
        amt=1,
        index=created_asset,
    )
    signed_xfer_txn = xfer_txn.sign(acct1.private_key)
    txid = algod_client.send_transaction(signed_xfer_txn)
    print(f"Sent transfer transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

def transfer_nft_wContract(algod_client,contract_address, private_key, sender, receiver):
    params = algod_client.suggested_params()
    txn = transaction.ApplicationCallTxn(
        sender=encoding.decode_address(contract_address),
        sp=params,
        index=1,  # Índice de la función de transferencia en el contrato
        app_args=[encoding.decode_address(sender), encoding.decode_address(receiver)],
        on_complete=transaction.OnComplete.NoOpOC
    )
    signed_txn = txn.sign(private_key)
    txid = algod_client.send_transaction(signed_txn)
    return txid

def create_contract_trans(algod_client,teal_code,acct1):
    # Crea una transacción de creación de contrato
    params = algod_client.suggested_params()
    txn = transaction.ApplicationCreateTxn(
        sender=acct1[0],
        sp=params,
        on_complete=transaction.OnComplete.NoOpOC,
        approval_program=teal_code,
        clear_program=teal_code
    )

    # Firme la transacción con la clave privada de la cuenta
    private_key = acct1[0]
    signed_txn = txn.sign(private_key)

    # Envía la transacción a la red
    txid = algod_client.send_transaction(signed_txn)

    # Espera a que la transacción sea confirmada
    algod_client.status_after_block(txid)

    # Obtén el ID del contrato después de ser desplegado
    contract_id = algod_client.pending_transaction_info(txid)["application-index"]

    print("Contrato desplegado con éxito. ID del contrato:", contract_id)
    
    return contract_id
        
        
