from TagLic import Car as cr
from TagLic import Validator as vl

__author__ = "Franz Bermeo Quezada"
__version__ = "1.0"
__email__ = "franz.bermeo@gmail.com"

def ValidateTagToTransit(_date, _time, _tag):
    vld = vl.Validator()

    if vld.isTimeFormat(_time):
        if vld.isDateFormat(_date):
            if vld.chars_validator(_tag):
                if vld.digit_validator(_tag):
                    if vld.HasRestrictedTransit(_date, _time, _tag):
                        return 'El vehiculo con placa ' + _tag + ' no puede transitar el ' + _date + ' a las ' + _time
                    else:
                        return 'El vehiculo con placa ' + _tag + ' esta autorizado circular en Quito el ' + _date + ' a las ' + _time
                else:
                    return 'Seccion de digitos INCORRECTA'
            else:
                return 'Seccion de letras INCORRECTA'
        else:
            return 'Formato de fecha INCORRECTO'
    else:
        return 'Formato de hora INCORRECTO'

def main():
    autom1 = cr.Car('2015', 'FZ', 'PQR-1025')
    autom2 = cr.Car('2016', 'MR', 'OTZ-6522')
    autom3 = cr.Car('2015', 'TL', 'AYC-3798')

    print(ValidateTagToTransit('10/08/2016', '08:30', autom1.getTag))
    print(ValidateTagToTransit('22/08/2016', '15:30', autom2.getTag))
    print(ValidateTagToTransit('04/08/2016', '1845', autom3.getTag))
    print(ValidateTagToTransit('04/08-2016', '18:45', autom3.getTag))

if __name__ == '__main__':
    main()