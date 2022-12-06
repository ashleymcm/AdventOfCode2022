import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

def isMarker(chars):
  chars = "".join(set(chars))
  if len(chars) == 4:
    return True
  return False

def getFirstCharacterAfterMarker(signal):
  for i in range(len(signal))[4::]:
    if isMarker(signal[i-4:i]):
      return i
  #should never get here

with open(os.path.join(dirname, "input.txt")) as signal_data:
  signal = signal_data.read()
  print(getFirstCharacterAfterMarker(signal))