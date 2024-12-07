import zipfile
with zipfile.ZipFile(r'c:\Users\KRISH\Desktop\Spotify analysis\kaggle1million dataset(highest).zip','r') as z:
    
    z.extractall('ex')