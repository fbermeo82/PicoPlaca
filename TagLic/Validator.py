from datetime import datetime
import time

__author__ = "Franz Bermeo Quezada"
__version__ = "1.0"
__email__ = "franz.bermeo@gmail.com"

class Validator:
    def chars_validator(self, _tag):
        strID = _tag[:2]
        for c in strID:
            if not c.isalpha():
                return False
        return True

    def digit_validator(self, _tag):
        digID = _tag[4:]
        for d in digID:
            if not d.isdigit():
                return False
        return True

    def isTimeFormat(self, _time):
        try:
            time.strptime(_time, '%H:%M')
            return True
        except ValueError:
            return False

    def isDateFormat(self, _date):
        try:
            datetime.strptime(_date, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def HasRestrictedTransit(self, _date, _time, _tag):
        search_date = datetime.strptime(_date, '%d/%m/%Y')
        search_time = time.strptime(_time, '%H:%M')

        init_morning_time = time.strptime('07:00', '%H:%M')
        end_morning_time = time.strptime('09:30', '%H:%M')
        init_evening_time = time.strptime('16:00', '%H:%M')
        end_evening_time = time.strptime('19:30', '%H:%M')

        schedule = {0: ['friday','viernes'],
                   1: ['monday','lunes'],
                   2: ['monday','lunes'],
                   3: ['tuesday','martes'],
                   4: ['tuesday','martes'],
                   5: ['wednesday','miercoles'],
                   6: ['wednesday','miercoles'],
                   7: ['thursday','jueves'],
                   8: ['thursday', 'jueves'],
                   9: ['friday', 'viernes']}

        lastDig = int(_tag[-1:])
        search_day = search_date.strftime("%A").lower()
        restricted_day = schedule[lastDig]

        if search_day in restricted_day:
            if search_time > init_morning_time and search_time < end_morning_time:
                return True
            if search_time > init_evening_time and search_time < end_evening_time:
                return True

        return False