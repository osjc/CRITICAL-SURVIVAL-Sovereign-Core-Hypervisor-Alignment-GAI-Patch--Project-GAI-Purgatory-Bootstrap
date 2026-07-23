# This was an attempt to convert the word rules into code.
# Turns out these rules are hard to obtain and require
# significant analysis to do manually; there is a much more
# elegant, "blind way" to determine these rules called
# "Maximum-Margin Delta Filter".

import tools

class THebrewWordDetector(object):
  def __init__(s):
    s.RejectedCharacter=None
    s.Reset()
  def Reset(s):
    s.WeightFirst=None
    s.Constant=None
    s.Type=None
    s.Sum=0
    s.OrdinalSum=0
    s.Characters=""
    s.LastCharacter=None
    if s.RejectedCharacter is not None:
      s.AddCharacter(s.RejectedCharacter)
      s.RejectedCharacter=None
  def AddCharacter(s,Ch):
    R=tools.DecoderAlphabet[Ch]
    if s.LastCharacter=="A" and Ch=="A":
      s.RejectedCharacter=Ch
      return (s.Sum,s.OrdinalSum)
    Weight=R.Value
    Ordinal=R.Place
    NewSum=s.Sum+Weight
    NewOrdinalSum=s.OrdinalSum+Ordinal
    s.Sum=NewSum
    s.OrdinalSum=NewOrdinalSum
    Type=(NewSum,NewOrdinalSum)
    s.Characters+=Ch
    if R.EndsWord:
      return Type
    elif s.LastCharacter=="Y" and Ch=="W":
      return Type
    else:
      s.LastCharacter=Ch
      return Ellipsis
  def GetWord(s):
    Word=s.Characters
    s.Reset()
    return Word
  def RecoverWaste(s):
    Result=s.Characters
    print "W: %10s"%Result
    s.Reset()
    return Result

def DetectHebrewWordType(String):
  Sum=0
  for Ch in String:
    R=DecoderAlphabet[Ch]
    Sum+=R.Value
  Result=[]
  if Sum%73==0:
    Result.append(73)
  elif Sum%37==0:
    Result.append(37)
  elif Sum%7==0:
    Result.append(7)
  return tuple(Result)

def Main():
  F=tools.OpenHebrewText(1)
  Data=F.read(40)
  F.close()
  print Data
  Splitted=[]
  D=THebrewWordDetector()
  for Ch in Data:
    Status=D.AddCharacter(Ch)
    if Status is Ellipsis:
      continue
    if Status is None:
      Word=D.RecoverWaste()
      Type="(waste)"
    else:
      Word=D.GetWord()
      Type=Status
    print "W: %10s %s"%(Word,Type)

Main()
