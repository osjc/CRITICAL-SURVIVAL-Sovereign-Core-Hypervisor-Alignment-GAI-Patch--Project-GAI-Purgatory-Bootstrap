# This script was an attempt to split the "raw string" into words using
# "simple arithmetics". I made about 4 attempts (which were lost to
# no-version-control-applied or "messing around instead of doing science")
# before I came to conclusion that "I was doing it the hard way" and gave
# up on this path. The script below is unfinished and does not work at all
# (it crashes with a "KeyError: None" error). It was constructed during the
# end of talks in logs 021 and 022. I might be able to reconstruct the
# broken scripts someday.

import tools

Prefixes=[
  "V",	# And
  "H",	# The
  "L",	# To/For
  "B",	# In/With
  "M",	# From
]

class THebrewWordDetector(object):
  def __init__(s):
    s.Reset()
    s.RejectedCharacter=None
  def Reset(s):
    s.WeightFirst=None
    s.Constant=None
    s.Type=None
    s.Sum=0
    s.OrdinalSum=0
    s.Characters=""
  def AddCharacter(s,Ch):
    R=tools.DecoderAlphabet[Ch]
    Weight=R.Value
    Ordinal=R.Place
    NewSum=s.Sum+Weight
    NewOrdinalSum=s.OrdinalSum+Ordinal
    """
    s.Characters+=Ch
    s.Sum=NewSum
    Result=[]
    if NewSum%73==0:
      Result.append(73)
    elif NewSum%37==0:
      Result.append(37)
    elif NewSum%7==0:
      Result.append(7)
    print "C: %10s %s"%(s.Characters,Result)
    if len(Result)==0:
      return Ellipsis
    return tuple(Result)
    """
  def RecoverWaste(s):
    Result=s.Characters
    print "W: %10s"%Result
    s.Reset()
    s.AddCharacter(s.RejectedCharacter)
    s.RejectedCharacter=None
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
  Data=F.read(10)
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
