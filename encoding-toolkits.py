import base64
import binascii

selection = input("select the encoding you want to encode or decod (b64_encode, b64_decode, hex_encode, hex_decode): ").lower()
data = input("put text/encoding you want to encode/decode here: ")

if selection == "b64_encode":
    b64_data = base64.b64encode(data.encode("utf-8"))
    print("Encoded B64: ",b64_data.decode("utf-8")) 
    pass
elif selection == "b64_decode":
    b64_data = base64.b64decode(data.encode("utf-8"))
    print("Decoded B64: ", b64_data.decode("utf-8")) 
    pass
elif selection == "hex_encode":
    hexdata = data.encode("utf-8").hex()
    print("Encoded hex: ", hexdata)
    pass
elif selection == "hex_decode":
    hexdata = bytes.fromhex(data).decode("latin-1")
    print("Decoded hex: ", hexdata)
    pass
else:
    print("please select a valid choice...")