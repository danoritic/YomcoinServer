from blockcypher import get_wallet_addresses
import blockcypher as b

if __name__=="__main__":
    # btc
    ADDRESS={'private': '48815632f75852500420c14e9fe026a64e3e63b3ab2debb598226d5e752380fd',
              'public': '03db92171c173cb86d24fecd6bd73ffe0853e4f76c366990282cb8269e2a4380c2',
              'address': '1Ma44h6LR6LfD4DD3SjacLHzh2gnzDdCRE', 'wif': 'Kyeek6KbzmzmEf3xkSvpE7PJ2hy5W5w4FQFAXMUfjhJKBUead3An'}
    addresses={"btc":"1Ma44h6LR6LfD4DD3SjacLHzh2gnzDdCRE",
               "eth":"1de355aab5d986056e1356f15a813eff6e82c13a",
               "ltc":"DLEap1TCAnA9qkSrgXo8vaC7faJc77a5Q6",
               "doge":"Xev4grSyuy2KhrcRoyYxQxeoW79BRQe1Mk"}
    
    # eth
    ADDRESS= {'private': '9126bb1ec9a94bf5fbb72e7aeff4a21dfadb27075c40d27a30524121fd5abbdf',
               'public': '04bc973b17a24d0c47019c031c286011c530e87a537de95b9a591ce20b20706240132ab6f096279458009b9031cebc3db7b3b61f61fdd829a36040da46ab115094', 
                'address': '1de355aab5d986056e1356f15a813eff6e82c13a'}

    # b.generate_new_address(api_key="45c9c4021cae4b0c9c1d6616070260ef",coin_symbol="eth")
    
    ADDRESS= {'private': '02d767167941d4fa2822702e6f28c2a39a001578b4c0c041fc5895861222da27',
               'public': '03bad6fe7c1dd12519eec49d6f5fd30f277dc449faf5a1265797714c559ed1c4d0', 
              'address': 'DLEap1TCAnA9qkSrgXo8vaC7faJc77a5Q6', 'wif': 'QNi9h2QRQL4bgKvWiKuY2tHdN4BR3udX75FAF3FH9EuqiNgoAuTF'}
    # b.generate_new_address(api_key="45c9c4021cae4b0c9c1d6616070260ef",coin_symbol="ltc")
    
    ADDRESS= {'private': '730ebc6cafb5b326c300ba3dddd74838a85862d28170f8f2faeca8ebe4c620c4',
               'public': '03b563b36c9fab15ce14379817298d9124093a46b16851465cd3b34f2cd4efbdce',
               'address': 'Xev4grSyuy2KhrcRoyYxQxeoW79BRQe1Mk', 'wif': 'XF9Hjd5kktuoNra8DQBzbPoRJ25uUz2dancZMQVzwAAVaXXA3cYi'}

    # b.generate_new_address(api_key="45c9c4021cae4b0c9c1d6616070260ef",coin_symbol="doge")
    
    ADDRESS= {'private': '730ebc6cafb5b326c300ba3dddd74838a85862d28170f8f2faeca8ebe4c620c4', 
              'public': '03b563b36c9fab15ce14379817298d9124093a46b16851465cd3b34f2cd4efbdce', 
              'address': 'Xev4grSyuy2KhrcRoyYxQxeoW79BRQe1Mk', 'wif': 'XF9Hjd5kktuoNra8DQBzbPoRJ25uUz2dancZMQVzwAAVaXXA3cYi'}

    # b.generate_new_address(api_key="45c9c4021cae4b0c9c1d6616070260ef",coin_symbol="dash")
    
    
    
    
    print("120"*120)
    print(get_wallet_addresses(wallet_name='yomcoin01@gmail.com', api_key='45c9c4021cae4b0c9c1d6616070260ef'))
