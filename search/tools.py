### Characters, their names and their translations.

Chars=(
  (u"\u05D0",	1,	1,	"aleph",	False,	"A"),
  (u"\u05D1",	2,	2,	"bet",		False,	"B"),
  (u"\u05D2",	3,	3,	"gimel",	False,	"G"),
  (u"\u05D3",	4,	4,	"daleth",	False,	"D"),
  (u"\u05D4",	5,	5,	"he",		False,	"H"),
  (u"\u05D5",	6,	6,	"vav",		False,	"V"),
  (u"\u05D6",	7,	7,	"zayin",	False,	"Z"),
  (u"\u05D7",	8,	8,	"het",		False,	"E"),
  (u"\u05D8",	9,	9,	"tet",		False,	"T"),
  (u"\u05D9",	10,	10,	"yod",		False,	"Y"),
  (u"\u05DA",	20,	11,	"kaf",		True,	"k"),
  (u"\u05DB",	20,	11,	"kaf",		False,	"K"),
  (u"\u05DC",	30,	12,	"lamed",	False,	"L"),
  (u"\u05DD",	40,	13,	"mem",		True,	"m"),
  (u"\u05DE",	40,	13,	"mem",		False,	"M"),
  (u"\u05DF",	50,	14,	"nun",		True,	"n"),
  (u"\u05E0",	50,	14,	"nun",		False,	"N"),
  (u"\u05E1",	60,	15,	"samekh",	False,	"S"),
  (u"\u05E2",	70,	16,	"ayin",		False,	"I"),
  (u"\u05E3",	80,	17,	"pe",		True,	"p"),
  (u"\u05E4",	80,	17,	"pe",		False,	"P"),
  (u"\u05E5",	90,	18,	"tsadi",	True,	"c"),
  (u"\u05E6",	90,	18,	"tsadi",	False,	"C"),
  (u"\u05E7",	100,	19,	"qof",		False,	"Q"),
  (u"\u05E8",	200,	20,	"resh",		False,	"R"),
  (u"\u05E9",	300,	21,	"shin",		False,	"J"),
  (u"\u05EA",	400,	22,	"tav",		False,	"W"),
)

class TRecord(object):
  def __init__(s):
    s.Value=None
    s.Place=None
    s.Name=None
    s.EndsWord=None
    s.Latin=None

def Decode():
  global Alphabet,DecoderAlphabet,Punct
  Alphabet={}
  DecoderAlphabet={}
  Punct={}
  for I in Chars:
    R=TRecord()
    Ch,R.Value,R.Place,R.Name,R.EndsWord,R.Latin=I
    if R.Value!=0:
      Alphabet[Ch]=R
      if R.Latin in DecoderAlphabet:
        raise RuntimeError("Error in source table")
      DecoderAlphabet[R.Latin]=R
    else:
      Punct[Ch]=(Name,Type)

Decode()
del Chars
del Decode

### Reading the data files

class TInputTextReader(object):
  def __init__(s,F):
    F.seek(0,2)
    s.TotalSize=F.tell()
    F.seek(0)
    s.ReadSize=0
    s.F=F
    s.Buffer=""
  def read(s,Size):
    Data=[]
    Input=s.Buffer
    Pos=0
    while len(Data)<Size:
      if len(Input)<=Pos:
        Pos=0
        Input=s.F.readline()
        if Input=="":
          break
        s.ReadSize+=len(Input)
        Input=Input.decode("utf8")
      Ch=Input[Pos]
      Pos+=1
      if Ch in Alphabet:
        I=Alphabet[Ch]
        Latin=I.Latin
        Data.append(Latin)
    s.Buffer=Input[Pos:]
    return "".join(Data)

  def close(s):
    s.F.close()

def RawOpenHebrewText(Number):
  FileSpec="data/ht%03d.dat"%Number
  return open(FileSpec)

def OpenHebrewText(Number):
  F=RawOpenHebrewText(Number)
  return TInputTextReader(F)
