from pyteal import *

def nft_contract():
    on_creation = Seq([
        App.localPut(Int(0), Bytes("owner"), Txn.sender()),
        Return(Int(1))
    ])

    on_transfer = Seq([
        App.localPut(Int(0), Bytes("owner"), Txn.receiver()),
        Return(Int(1))
    ])

    on_update = Seq([
        App.localPut(Int(0), Bytes("metadata"), Txn.application_args[0]),
        Return(Int(1))
    ])

    on_delete = Seq([
        App.localDel(Int(0), Bytes("owner")),
        App.localDel(Int(0), Bytes("metadata")),
        Return(Int(1))
    ])

    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.application_id() != Int(0) & Txn.application_args.length() == Int(0), on_transfer],
        [Txn.application_id() != Int(0) & Txn.application_args.length() > Int(0), on_update],
        [Txn.application_id() != Int(0) & Txn.application_args[0] == Bytes("delete"), on_delete]
    )

    return program

