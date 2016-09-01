# Hint:  use Google to find python function

####a) 
#date_start = '01-02-2013'  
#date_stop = '07-28-2015'   

####b)  
#date_start = '12312013'  
#date_stop = '05282015'  

####c)  
#date_start = '15-Jan-1994'  
#date_stop = '14-Jul-2015'  

from datetime import *

date_start = '01-02-2013'
date_stop = '07-28-2015'

date_format = "%m-%d-%Y"

date_start_std = datetime.strptime(date_start, date_format)    
date_stop_std = datetime.strptime(date_stop, date_format)

date_count = date_stop_std - date_start_std

print date_count.days

date_start_1 = '12312013'
date_stop_1 = '05282015'

date_format = "%m%d%Y"

date_start_std = datetime.strptime(date_start_1, date_format)    
date_stop_std = datetime.strptime(date_stop_1, date_format)

date_count = date_stop_std - date_start_std

print date_count.days

date_start_2 = '15-Jan-1994'
date_stop_2 = '14-Jul-2015'

date_format = "%d-%b-%Y"

date_start_std = datetime.strptime(date_start_2, date_format)    
date_stop_std = datetime.strptime(date_stop_2, date_format)

date_count = date_stop_std - date_start_std

print date_count.days
