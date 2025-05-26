#word = 'bananana'

#fss = word.find('na')
#print(fss)


text = "X-DSPAM-Confidence:    0.8475"

start = text.find("   ")

end = text.find("5")

float_string = text[start + 1 : end + 1]

float_int = float(float_string)

print(float_int)

print(len('banana')*7)

