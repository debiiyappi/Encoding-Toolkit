import base64
import binascii


while True:
    selection = input("""
===========================
 Encoding Toolkit v0.0.1
      by debiiyapp
===========================

Available commands:
  b64-encode
  b64-decode
  hex-encode
  hex-decode

Type "exit" to quit.
ish>
"""
 ).lower()

    if selection == "exit":
        break

    data = input("ish|text> ")


    if selection == "b64-encode":
        b64_data = base64.b64encode(data.encode("utf-8"))
        print("ish|output> ",b64_data.decode("utf-8")) 
        
    elif selection == "b64-decode":
        b64_data = base64.b64decode(data.encode("utf-8"))
        print("ish|output> ", b64_data.decode("utf-8")) 
       
    elif selection == "hex-encode":
        hexdata = data.encode("utf-8").hex()
        print("ish|output> ", hexdata)
        
    elif selection == "hex-decode":
        hexdata = bytes.fromhex(data).decode("utf-8")
        print("ish|output> ", hexdata)
        
    else:
        print("ish|error> invalid choice!")