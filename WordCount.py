#WordCount.py
#Name: Jacob Kosmicki
#Date: 2/26/2025
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordcount = 0
  lettercount = 0
  
  for line in textFile:
    lineCount += 1
    words = line.split(' ')
    

    for word in words: 
      wordcount = wordcount + 1
  print("Lines:", lineCount)
  print("Words:", wordcount)

if __name__ == '__main__':
  main()
