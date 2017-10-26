import re

#Tanker:
#1: Meny foerst om man vil legge til nytt ord i lista eller oversette
#2: Fikse muligheten til aa skrive inn enda en setning uten aa maatte gaa gjennom startup-tekst
#3: Muligheten til aa lagre tekst i en .txt-fil som opprettes

def sentenceInput(): #done
  text = raw_input("Tast ind setningen I wiil ofuersette: ")

  return re.sub(r'[^\w\s]','',text.lower()).rsplit() #Remove punctuation, lowercase, split into list

def convertFileToDict():
  d = {}
  with open("ordliste.txt") as f:
    for line in f:
      #print repr(line)
      (key, val) = line.split()
      d[key] = val
  f.close
  return d  

def translateSentence(dictionary, textToTranslate):
  translated = []
  for word in range(0,len(textToTranslate)):
    tempword = textToTranslate[word]
    try:
      tempword = dictionary[tempword]
      translated.append(tempword)
    except KeyError:
      translated.append(tempword)
      continue

  print 'Teksten ble oversatt til foelgende'
  print ' '.join(translated)

def main():
  
  print 'I hafuer naa entret ofuersetteren phra hedensk tiil kancelli.'
  print 'Det ere svaert viktig att I ey skrifuer ind nordiske bokstafuer,'
  print 'samt att I skrifuer kun en setning af gangen.'
  print ' '
  raw_input('Press en knast phor att phortsette...')  

  innSkriviTekst = sentenceInput()
  dictionary = convertFileToDict()
  translateSentence(dictionary, innSkriviTekst)

main()