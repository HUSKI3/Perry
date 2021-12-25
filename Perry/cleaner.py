import os, re, os.path

def clean(_Path: 'location to clean'):
  for root, dirs, files in os.walk(_Path):
    for file in files:
        os.remove(os.path.join(root, file))