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

        Errkomp = 0

        if np.amin(CXZJ) >= 0 :
            print("sukces")
            return

        INDEX = np.nonzero( CXZJ == np.amin(CXZJ) )

        if self.strzm[INDEX[0].min()][0] == 'x' :
            if self.strzm[INDEX[0].min()][1] == 'd':
                print("jest xd")
                wskkomp = 0
            else :
                print("nie jest xd")
                wskkomp = 1
        else:
            if self.strzb[INDEX[0].min()][1] == 'd':
                print("jest yd")
                wskkomp = 2
            else :
                print("nie jest yd")
                wskkomp = 3

        CBI = np.array( [] )
        for i in range( len( ZM ) ):
            CBI = np.append( CBI, B[i] / ZM[i, INDEX][1] )

        INDEX2 = np.nonzero( CBI == np.amin(CBI) )
        #TODO:
        print(wskkomp)
        print(self.strzb[INDEX[0].min()][0])
        if wskkomp == 0:
            if self.strzb[INDEX[0].min()][0] == 'y':
                Errkomp = 1
                print("nie ma 1")
        elif wskkomp == 1:
            if self.strzb[INDEX[0].min()][0:1] == "yd":
                print("nie ma 1")
                Errkomp = 1
        elif wskkomp == 2:
            if self.strzb[INDEX[0].min()][0] == 'x':
                print("nie ma 1")
                Errkomp = 1
        elif wskkomp == 3:
            if self.strzb[INDEX[0].min()][0:1] == "xd":
                print("nie ma 1")
                Errkomp = 1


        tmp = copy.deepcopy(ZB)
        for i in range( self.lenogr + self.lenfc ) :
            tmp[i,INDEX2] = copy.deepcopy(ZM[i, INDEX].min())

        ZB = copy.deepcopy( tmp )
        print("------------------")
        print(self.strzm)
        print(ZM)
        ZB1 = np.linalg.inv(ZB)

        ZNB = ZB1 @ ZNB
        B = ZB1 @ B

        ZM = np.append( ZB1, ZNB, axis= 1)

        # print(ZB1)
        print("************")

        self.zm = ZM
        self.zb = ZB
        self.znb = ZNB
        self.cb = CB
        self.cx = CX
        self.b = B


        # CB = np.array(self.cb)
        # CX = np.array(self.cx)
        # B = np.array(self.b)

