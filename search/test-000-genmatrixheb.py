# This was my first attempt to obtain the 

import sys
import time
import tools

Write=sys.stdout.write
Flush=sys.stdout.flush

def Main():
  # Initialize.
  Counts={}
  # To avoid special cases, we add one count of "BA" to the counters.
  # This addition should sink into the noise.
  Data="A"
  # The main loop. Open the data file, process it, then close it.
  # I use the "Modern Hebrew" bible until I find a better data source.
  CurTime=0
  F=tools.OpenHebrewText(1)
  Write("%20d\r"%F.TotalSize)
  Flush()
  while True:
    Time=time.time()
    if Time-CurTime>0.015625:
      CurTime=Time
      Write("%10d\r"%F.ReadSize)
      Flush()
    New=F.read(40)
    if New=="":
      break
    Data+=New
    for Index in range(len(Data)-1):
      Pair=Data[Index]+Data[Index+1]
      if Pair in Counts:
        Counts[Pair]+=1
      else:
        Counts[Pair]=1
    Data=Data[-1]
    #if F.ReadSize>10000:
    #  break
  F.close()
  # Produce the raw matrix output.
  OutF=open("matrix.dat","w")
  List=Counts.items()
  List.sort()
  for Pair,Count in List:
    OutF.write(Pair)
    OutF.write(" ")
    OutF.write(str(Count))
    OutF.write("\n")

Main()
