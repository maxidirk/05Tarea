#######################################################
'''
Metodos Numericos para la Ciencia e Ingenieria
FI3104-1
Tarea 5
Maximiliano Dirk Vega Aguilera
18.451.231-9
'''
#######################################################

import numpy as np
import matplotlib.pyplot as pyplot

#######################################################

#funciones

def crea_caja(Lx,Ly,h):
    '''
    crea caja con zeros de tamanho Lx x Ly con cuadrillas de paso h
    '''
    Nx = (Lx / h) + 1  #numero de pasos a dar en eje x
    Ny = (Ly / h) + 1  #numero de pasos a dar en eje y
    caja = np.zeros( (Nx , Ny) )  #se construye caja
    return caja


def letra_M(caja, h, rho):
    '''
    construye letra M densidad de carga rho en caja de paso h
    '''
    Llx = len(cajal[:][0])              #largo caja de letra eje x
    Lly = len(cajal[0][:])              #largo caja de letra eje y
    Nlx = (Llx / h) + 1  #numero de pasos en caja de letra a dar en eje x
    Nly = (Lly / h) + 1  #numero de pasos en caja de ltera a dar en eje y
    N_pasos_1cm = 1. / h  #numero de pasos para tener 1 cm
    cajal = crea_caja(Llx, Lly, h)
    cajal[0 : 0 + N_pasos_1cm , : ] = rho
    cajal[Nlx - N_pasos_1cm : Nlx , : ] = rho
    cajal[ : , N_pasos_1cm : 2 * N_pasos_1cm] = rho

    cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
    2 * N_pasos_1cm : 3 * N_pasos_1cm] = rho

    cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
    N_pasos_1cm : 2 * N_pasos_1cm ] =
    caja[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
    N_pasos_1cm : 2 * N_pasos_1cm ]

    return cajal

def asignar_letra(caja,cajal):
    '''
    asigna la letra a la caja principal
    caja = caja principal
    cajal = caja donde esta la letra
    '''
    pass

#######################################################

#construir caja
'''
caja de 10cmx15cm
centro de caja = (0,0)
cambio de coordenadas
x' = x - Nx/2
y' = y - Ny/2
esquina de caja = (0,0)
'''
Lx = 10.           #[cm] largo de la caja en eje x
Ly = 15.           #[cm] largo de la caja en eje y
h = 0.9            #[cm] tamanho del paso

caja = crea_caja(Lx, Ly, h)  #se construye caja

#######################################################

#construir letra
'''
dentro de caja de 5cmx7cm
construir letra M (con h = 0.25 o 0.3 o 0.5 queda bien)
grosor 1cm
'''
Llx = 5              #largo caja de letra eje x
Lly = 7              #largo caja de letra eje y
rho = 1 #densidad de carga
cajal = crea_caja(Llx, Lly, h) #se construye caja de letra
cajal = letra_M(cajal, h, rho)
'''
Construccion de la letra M

cajal[0 : 0 + N_pasos_1cm , : ] = rho
cajal[Nlx - N_pasos_1cm : Nlx , : ] = rho
cajal[ : , N_pasos_1cm : 2 * N_pasos_1cm] = rho

cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
2 * N_pasos_1cm : 3 * N_pasos_1cm] = rho

cajal[Nlx / 2 - N_pasos_1cm / 2 : Nlx / 2 + N_pasos_1cm / 2 + 1 ,
N_pasos_1cm : 2 * N_pasos_1cm ] = 0


asignacion de la letra a la caja principal
''''''
busca el centro? creo que no
caja[Nx/2,Ny/2] = 1
if Nx % 2 == 0:
    caja[(Nx / 2) - 1 ,Ny / 2] = 1
if Ny % 2 == 0:
    caja[Nx / 2 ,(Ny / 2) - 1] = 1
'''
#bordex_caja = round((Nx / 2 ) - (Nlx / 2 ))
#bordey_caja = round((Ny / 2 ) - (Nly / 2 ))

#ly = int(round(Nlx))
#lx = int(round(Nly))
'''
try:
    lx = int(round(Nly))
    try:
        ly = int(round(Nlx))
        for i in range(ly):
            for j in range(lx):
                if cajal[i][j] != 0:
                    if cajal[i][j] != 0:
                        caja[bordex_caja : bordex_caja + Nlx ,
                        bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
    except:
        ly = int(round(Nlx)) -1
        for i in range(ly):
            for j in range(lx):
                if cajal[i][j] != 0:
                    if cajal[i][j] != 0:
                        caja[bordex_caja : bordex_caja + Nlx ,
                        bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
except:
    lx = int(round(Nly)) - 1
    try:
        ly = int(round(Nlx))
        for i in range(ly):
            for j in range(lx):
                if cajal[i][j] != 0:
                    if cajal[i][j] != 0:
                        caja[bordex_caja : bordex_caja + Nlx ,
                        bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]
    except:
        ly = int(round(Nlx)) -1
        for i in range(ly):
            for j in range(lx):
                if cajal[i][j] != 0:
                    if cajal[i][j] != 0:
                        caja[bordex_caja : bordex_caja + Nlx ,
                        bordey_caja : bordey_caja + Nly][i][j] = cajal[i][j]



asignar la caja entera a la caja principal

caja[bordex_caja : bordex_caja + Nlx ,
bordey_caja : bordey_caja + Nly] = cajal
'''
#######################################################

#construir condiciiones

#######################################################

#aplicar metodo de sobrerelajacion


#######################################################


#zona de pruebas
#print bordex_caja
#print bordey_caja

#caja[(Nx-1)/2,(Ny-1)/2] = 1

print np.transpose(caja)
print np.transpose(cajal)

#######################################################
