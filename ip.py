import os
import urllib. request as urllib2
import json

print()
print("                        .      ..                 ")       
print("     ...     ..        %8P    5888R     ")         
print("  :~""888h.:^"888:      .     '888R        .u   ") 
print(" 8X   `8888X  8888>   .@88u    888R     ud8888.  ")
print(" X888n. 8888X  ?888>  ''888E`   888R   :888'8888. ")
print(" '88888 8888X   ?**h.   888E    888R   d888 '88%" ")
print("  `*88 8888~ x88x.     888E    888R   8888.+"    ")
print("  .<"  88*`  88888X    888E    888R   8888L   ")   
print("    ..XC.    `*8888k   888&   .888B . '8888c. .+  ")
print("  :888888H.    `%88>   R888"  ^*888%   "88888%   ")
print(" <  `"888888:    X"     ""      "%       "YP'    ")
print("       %888888x.-`      ")                         
print("         ""**""     ")                             
print("                      Made By @Oxycrime        ")                              
print()                          
                                                 


while True:
ip = input("What is your target IP: ")
url = "http://ip-api.com/json/"
response = urllib2.urlopen(url + ip)
data = response.read()
values = json. loads(data)
print("IP: " + values ["query"])
print("City: " + values ["city"])
print("ISP: " + values["isp"])
print("Country: " + values ["country"])
print("Region: " + values ["region"])
print("Timezone:" + values ["timezone" ])
break
