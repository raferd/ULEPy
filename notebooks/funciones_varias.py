# Módulo con funciones varias
import numpy as np

def print_int_bits(valor_entero, formato='',num_bits=16):
    ''' formato: 'hex'-> hexadecimal; 'bin'-> binario; ''-> binario y hexadecimal
        num_cifras: número de cifras para representar el valor en el/los formato/s seleccionado/s
    '''
    num_cifras_hex=int(np.ceil(num_bits/4))
    num_bits=num_cifras_hex*4
    
    if valor_entero<0:
        t=2**num_bits-1
        aux=valor_entero+t+1
    else:
        aux=valor_entero
        
        
    if formato=='hex':
        cadena_formato='{:0'+str(num_cifras_hex)+'X}h :: {:d} '
        print(cadena_formato.format(valor_entero,aux))
    elif formato=='bin':
        cadena_formato='{:0'+str(num_bits)+'b}b :: {:d}'
        print(cadena_formato.format(valor_entero,aux))
    else:
        cadena_formato='{:0'+str(num_cifras_hex)+'X}h'+' :: {:0'+str(num_bits)+'b}b :: {:d}'
        print(cadena_formato.format(valor_entero,aux,aux))
    
