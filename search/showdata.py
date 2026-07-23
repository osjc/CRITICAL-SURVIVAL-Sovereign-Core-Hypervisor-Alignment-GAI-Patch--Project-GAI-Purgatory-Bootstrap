# I used this small script to verify that my read-and-filter
# tool works correctly. It reads 10 lines of the text,
# displays them translated to the "Latin Representation" and
# displays them. Then it uses the reading tool to read the
# raw Hebrew text and show it to me. Now I can verify that
# the raw Hebrew text from the reading filter matches the
# Hebrew text in the data file. Verification passed for the
# first line break so I am confident it works.

import tools

def ConvertLine(Line):
  Line=Line.decode("utf8")
  Output=[]
  for Ch in Line:
    if Ch in tools.Alphabet:
      I=tools.Alphabet[Ch]
      Latin=I.Latin
      Output.append("\x1B[1;36m"+Latin+"\x1B[m")
    else:
      Ord=ord(Ch)
      if Ord<32 or Ord>126:
        Ord=ord("?")
      Output.append(chr(Ord))
  return "".join(Output)

def Main():
  F=tools.RawOpenHebrewText(1)
  for i in range(10):
    Line=F.readline()[:-1]
    Line=ConvertLine(Line)
    print Line
  F.close()
  F=tools.OpenHebrewText(1)
  Data=F.read(60)
  F.close()
  print Data

Main()
