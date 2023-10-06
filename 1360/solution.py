import datetime

dt_format = '%Y-%m-%d'

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        dt1 = datetime.datetime.strptime( date1, dt_format )
        dt2 = datetime.datetime.strptime( date2, dt_format )
        return ( abs( (dt2-dt1).days ) )

