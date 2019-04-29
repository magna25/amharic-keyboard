import argparse

class AmharicKeyboard(object):
    def __init__(self):
        self.alphabets = {
        'h':['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ','ኋ'],
        'l':['ለ','ሉ','ሊ','ላ','ሌ','ል','ሎ','ሏ'],
        'h2':['ሐ','ሑ','ሒ','ሓ','ሔ','ሕ','ሖ','ሗ'],
        'm':['መ','ሙ','ሚ','ማ','ሜ','ም','ሞ','ሟ'],
        's2':['ሠ','ሡ','ሢ','ሣ','ሤ','ሥ','ሦ','ሧ'],
        'r':['ረ','ሩ','ሪ','ራ','ሬ','ር','ሮ','ሯ'],
        's':['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ','ሷ'],
        'sh':['ሸ','ሹ','ሺ','ሻ','ሼ','ሽ','ሾ','ሿ'],
        'q':['ቀ','ቁ','ቂ','ቃ','ቄ','ቅ','ቆ','ቋ'],
        'b':['በ','ቡ','ቢ','ባ','ቤ','ብ','ቦ','ቧ'],
        'v':['ቨ','ቩ','ቪ','ቫ','ቬ','ቭ','ቮ','ቯ'],
        't':['ተ','ቱ','ቲ','ታ','ቴ','ት','ቶ','ቷ'],
        'ch':['ቸ','ቹ','ቺ','ቻ','ቼ','ች','ቾ','ቿ'],
        'n':['ነ','ኑ','ኒ','ና','ኔ','ን','ኖ','ኗ'],
        'gn':['ኘ','ኙ','ኚ','ኛ','ኜ','ኝ','ኞ','ኟ'],
        'e':['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ','ኧ'],
        'a':['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ','ኧ'],
        'k':['ከ','ኩ','ኪ','ካ','ኬ','ክ','ኮ','ኳ'],
        'w':['ወ','ዉ','ዊ','ዋ','ዌ','ው','ዎ',''],
        'z':['ዘ','ዙ','ዚ','ዛ','ዜ','ዝ','ዞ','ዟ'],
        'zh':['ዠ','ዡ','ዢ','ዣ','ዤ','ዥ','ዦ','ዧ'],
        'y':['የ','ዩ','ዪ','ያ','ዬ','ይ','ዮ','ዯ'],
        'd':['ደ','ዱ','ዲ','ዳ','ዴ','ድ','ዶ','ዷ'],
        'j':['ጀ','ጁ','ጂ','ጃ','ጄ','ጅ','ጆ','ጇ'],
        'g':['ገ','ጉ','ጊ','ጋ','ጌ','ግ','ጎ','ጏ'],
        'x':['ጠ','ጡ','ጢ','ጣ','ጤ','ጥ','ጦ','ጧ'],
        'c':['ጨ','ጩ','ጪ','ጫ','ጬ','ጭ','ጮ','ጯ'],
        'ts2':['ጰ','ጱ','ጲ','ጳ','ጴ','ጵ','ጶ','ጷ'],
        'ph':['ጰ','ጹ','ጺ','ጻ','ጼ','ጽ','ጾ','ጷ'],
        'ts':['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ','ፇ'],
        'f':['ፈ','ፉ','ፊ','ፋ','ፌ','ፍ','ፎ','ፏ'],
        'p':['ፐ','ፑ','ፒ','ፓ','ፔ','ፕ','ፖ','ፗ'],
        ' ':[' ',' ',' ',' ',' ',' ',' ',' '],
        '-':['፡'],
        ',':['፣'],
        '.':['።'],
        ';':['፤'],
        ':':['፥']
        }

    def isVowel(self,char):
        vowels = ['a','e','i','o','u']
        if char in vowels: 
            return True
        return False      

    def doesNeedH(self,char):
        letters = ['s','c','z','p']
        if char in letters: 
            return True
        return False

    def isCh(self,str):
        lts = ['ch', 'sh','zh','ph','gn','ts']
        if str in lts: 
            return True
        return False

    def isPunctuation(self,char):
        allowed_puncs = ['.',',','-',':',';']
        if char in allowed_puncs: 
            return True
        return False

    def getLetter(self,a,b):
        options = {
            'a': self.alphabets[a][3], 
            'e': self.alphabets[a][0],
            'i': self.alphabets[a][2],
            'o': self.alphabets[a][6],
            'u': self.alphabets[a][1]
        }
        if a in self.alphabets and b in options:
            return options[b]
        return ""

    def processSubstring(self,str):
        ln = len(str)
        
        if ln == 1:
            
            if str in self.alphabets:
                if self.isPunctuation(str) or str == 'a':
                    return self.alphabets[str][0]

                return self.alphabets[str][5]

            return str

        elif ln == 2:
            
            if str[0] == ' ' and str[1] == 'e':
                return ' ' + self.alphabets['e'][5]

            if self.isCh(str):
                return self.alphabets[str][5]

            if self.isVowel(str[0]) and self.isVowel(str[1]):
                if str[0] == 'e':
                    return self.getLetter(str[0],str[1])

                if str[0] != 'e' and str[1] != 'e' or str[0] != 'a' and str[1] != 'a':
                    return ""

            if str[1] == 'i':
                return self.alphabets[str[0]][5]

            if str[0] in self.alphabets:
                if str[0] == ' ' and str[1] == 'a':
                    return ' ' + self.alphabets['a'][0]

                return self.getLetter(str[0],str[1])

            return str

        elif ln == 3:
            
            f2 = str[:2]
            l2 = str[-2:]

            if str[0] == ' ' and l2 == "ee":
                return ' ' + self.alphabets['e'][0]

            if self.isCh(f2):
                if str[2] == 'i':
                    return self.alphabets[f2][5]
                return self.getLetter(f2,str[2])
            if str == "eee":
                return self.alphabets[str[0]][4]

            if l2 == "ee":
                return self.alphabets[str[0]][4]

            if l2 == "ua":
                return self.alphabets[str[0]][7]

            if l2 == 'ii':
                if str[0] != 'i':
                    return self.alphabets[str[0]][2]

                return ""
            return "here"
        
        elif ln == 4:
            f2 = str[:2]
            l2 = str[-2:]
            l3 = str[-3:]

            if l3 == "eee" and str[0] == ' ':
                return self.alphabets['e'][4]

            if l2 == "ee":
                if self.isCh(f2):
                    return self.alphabets[f2][4]

                return self.alphabets[str[0]][4]

            if l2 == "ua":
                return self.alphabets[f2][7]

            if l2 == "ii":
                    if self.isCh(f2):
                        return self.alphabets[f2][2]

                    return self.alphabets[str[0]][2]

        else:
            return self.processSubstring(str[:4])

    def transform(self,text):
        text = str(text).strip()
        lenx = len(text)
        substr = ""
        transformed = ""
        i = 0
        
        while(i < lenx):
            if substr == "":
                substr += text[i]
            else:
                if self.doesNeedH(substr[-1]) and text[i] == 'h':
                    substr += text[i]
                elif substr[-1] == 't' and text[i] == 's':
                    substr += text[i]
                elif substr[-1] == 'g' and text[i] == 'n':
                    substr += text[i]

                elif self.isVowel(text[i]):
                    if self.isVowel(substr[-1]) and self.isVowel(text[i]):
                        if text[i] == 'a' and substr[-1] != 'u':
                            transformed += self.processSubstring(substr)
                            substr = text[i]

                        if substr[-1] == 'e' and text[i] == 'e' or substr[-1] == 'u' and text[i] == 'a' or substr[-1] == 'i' and text[i] == 'i':
                            substr += text[i]

                        if lenx == 2 and substr[0] == 'e' and self.isVowel(text[i]):
                            substr += text[i]
                    else:
                        substr += text[i]
                else:
                    transformed += self.processSubstring(substr) 
                    substr = text[i]

                    
            i += 1
        
        transformed += self.processSubstring(substr)
        return transformed.strip()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--text', metavar='str', type=str, 
        help='text to be transfromed')
  

    args = parser.parse_args()
    keyboard = AmharicKeyboard()
    print(keyboard.transform(args.text))
