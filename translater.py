import re

#Tekst som dukker opp i starten av programmet
def programStartUp():
  print 'I hafuer naa entret ofuersetteren phra hedensk tiil kancelli.'
  print 'Det ere svaert viktig att I ey skrifuer ind nordiske bokstafuer,'
  print 'samt att I skrifuer kun en setning af gangen.'
  print ' '
  raw_input('Press enter phor att phortsette...')   

#Input av tekst fra bruker, samt fjerning av uppercases, komma, punktum, osv. 
#Splitter til ogsaa setningen inn i et array med hvert ord som ett element 
def sentenceInput(): 
  text = raw_input("Tast ind setningen I wiil ofuersette: ")

  return re.sub(r'[^\w\s]','',text.lower()).rsplit() #Remove punctuation, lowercase, split into list

#Leser filen med ordboka og putter dette inn i et dictionary. 
#Kaster exception hvis ordboka ikke finnes
def convertFileToDict():
  d = {}
  try:
    with open("ordliste.txt") as file:
      for line in file:
      #print repr(line)
        (key, val) = line.split()
        d[key] = val
    file.close
    return d  
  except IOError:
    print 'Wii magter ey att finne philen med ordboken, och kan af denne grunn ey ofuersette noen tekst'
    raise SystemExit(0)

#Oversetter fra norsk til kancelli og printer ut teksten
def translate(dictionary, textToTranslate):
  translated = []
  for word in range(0,len(textToTranslate)):
    tempword = textToTranslate[word]
    try:
      tempword = dictionary[tempword]
      translated.append(tempword)
    except KeyError:
      translated.append(tempword)
      continue

  print 'Teksten ble ofuersatt til foelgende'
  print ' '.join(translated)

#Sekvensen oversettelsen skal foregaa i til bruk av flere setninger
def translateSequence(dictionary):
  inputText = sentenceInput()
  translate(dictionary, inputText)

def main():
  programStartUp()
  dictionary = convertFileToDict()
  translateSequence(dictionary)
  

main()