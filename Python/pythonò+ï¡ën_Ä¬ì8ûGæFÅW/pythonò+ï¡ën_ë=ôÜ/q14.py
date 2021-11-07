import json

emoji_list = []
hex_list = []

for num in range(int(0x1f000), int(0x20000)):
	
	emoji_list.append(chr(num))

	hex_list.append(format(num, '08x'))

#print(emoji_list)
#print(hex_list)

emoji_dict = {key : value for key, value in zip(emoji_list, hex_list)}

#print(emoji_dict)

with open('q14.py_emoji_dict.json', 'w') as w:
    json.dump(emoji_dict, w)

with open('q14.py_emoji_dict.json', 'r') as r:
	read = json.load(r)

print(read)

