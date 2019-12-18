
infile ='./Documents/proyecto1/archivoxxxzz.txt'
def writefile(infile):
    """ escribir archivo """
    with open(infile, 'w') as f:
        for i in range(10):
            f.write(str(i))

def readfile(infile):
    """leer archivo"""
    with open(infile, 'r') as f:
        f.

if __name__ == "__main__":
    writefile()