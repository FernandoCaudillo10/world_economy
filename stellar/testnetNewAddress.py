from stellar_base.keypair import Keypair
import requests
from stellar_base.address import Address

kp = Keypair.random()
publickey = kp.address().decode()
r = requests.get('https://friendbot.stellar.org/?addr=' + publickey)

print(publickey)
print(r)
print(kp)

#publickey = 'GDVDKQFP665JAO7A2LSHNLQIUNYNAAIGJ6FYJVMG4DT3YJQQJSRBLQDG'
address = Address(address=publickey) # address = Address(address=publickey,network='public') for livenet
address.get() # get the updated information

print("Balances: {}".format(address.balances))
print("Sequence Number: {}".format(address.sequence))
print("Flags: {}".format(address.flags))
print("Signers: {}".format(address.signers))
print("Data: {}".format(address.data))
