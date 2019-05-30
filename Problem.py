import numpy as np

class Problem:
    def __init__(self):
        #Zmienne pomocnicze
        self.lenfc = 0
        self.lenznb = 0


        self.fc = []
        self.ogr = []
        self.b = []
        self.lag = []
        self.cx = []
        self.cb = []
        self.zb = []
        self.znb = []
        self.zm = []

    def simplex(self):
        ZM = np.array(self.zm)
        CB = np.array(self.cb)
        CX = np.array(self.cx)
        B = np.array(self.b)

        ZJ =  CB.T @ ZM
        CXZJ = np.subtract(CX, ZJ)
        INDEX = np.nonzero( CXZJ == np.amin(CXZJ) )

        print(B)
        print("************")
        CBI = np.array( [] )
        for i in range( len( ZM ) ):
            #TODO: tablica jednoelementowa, a nie dwu
            print(ZM[i, INDEX])
            CBI = np.append( CBI, B[i] / ZM[i, INDEX] )
            print(CBI)
            # print(ZM[i, INDEX])
        print("************")
        print(CBI)

        print("*************")
        # print(ZM)
        # print( ZM[INDEX] )

        # print(CXZJ)
        # print("*************")
        # print(np.amin(CXZJ))

