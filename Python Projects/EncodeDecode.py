while True:
    ZWNJ = "‌"
    totalStr = "~!@#$%^&*()_+\tQWERTYUIOP{}|ASDFGHJKL:\"\nZXCVBNM<>? `1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./👻"
    # print(totalStr.find('\n'))
    encodeOrDecode = ' '
    while not(encodeOrDecode[0].lower() in ['e','d']):
        encodeOrDecode = input('Encode or Decode (e, d)\n')
    encodeOrDecode = encodeOrDecode == 'e'
    listOfText = []
    text = input('Text (enter an empty Line to stop):\n')
    while True:
        if(text == ''):
            break
        listOfText.append(text)
        text = input()
    # text = ('\n'.join(listOfText)).strip()
    text = ('\n'.join(listOfText))
    # print(text)
    if(encodeOrDecode):
        chars = []
        for char in text:
            chars.append(char)
        encoded = []
        for char in chars:
            ind = str(totalStr.find(char))
            if(ind == '-1'):
                ind = '97'
            encoded.append(ind)
        encodeText = ZWNJ.join(encoded)
        print(encodeText)
    else:
        try:
            decode = []
            nums = text.split(ZWNJ)
            for i in nums:
                decode.append(totalStr[int(i)])
            print(''.join(decode))
        except:
            print('Invalid Encoded String')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')