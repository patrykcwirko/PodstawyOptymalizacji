import numpy as np
import copy

class Problem:
    def __init__(self):
        #Zmienne pomocnicze
        self.lenfc = 0
        self.lenznb = 0
        self.lenogr = 0


        self.fc = []
        self.ogr = []
        self.b = []
        self.lag = []
        self.cx = []
        self.cb = []
        self.zb = []
        self.znb = []
        self.zm = []
        self.strzm = []
        self.strzb = []

    def simplex(self):
        ZM = np.array(self.zm)
        ZB = np.array(self.zb)
        ZNB = np.array(self.znb)
        CB = np.array(self.cb)
        CX = np.array(self.cx)
        B = np.array(self.b)

        ZJ =  CB.T @ ZM
        CXZJ = np.subtract(CX, ZJ)

        if np.amin(CXZJ) >= 0 :
            print("sukces")
            return
        #TODO: sprawdzanie zmiennych komplementarnych
        INDEX = np.nonzero( CXZJ == np.amin(CXZJ) )

        CBI = np.array( [] )
        for i in range( len( ZM ) ):
            CBI = np.append( CBI, B[i] / ZM[i, INDEX].min() )

        INDEX2 = np.nonzero( CBI == np.amin(CBI) )

        tmp = copy.deepcopy(ZB)
        for i in range( self.lenogr + self.lenfc ) :
            tmp[i,INDEX2] = copy.deepcopy(ZM[i, INDEX].min())

        ZB = copy.deepcopy( tmp )
        ZB1 = np.linalg.inv(ZB)

        ZNB = ZB1 @ ZNB

        print(ZM)
        print("************")
        print(ZB)
        print("************")
        print(CBI)

        print("*************")
        # print(ZM)
        # print( ZM[INDEX] )

        # print(CXZJ)
        # print("*************")
        # print(np.amin(CXZJ))

