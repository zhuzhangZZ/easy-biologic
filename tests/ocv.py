import logging

import easy_biologic as ebl
import easy_biologic.base_programs as ebp

logging.basicConfig( level = logging.DEBUG )

channels = [ 1 ]
by_channel = False
params = { 
	'time': 10 
}

save_path = 'C:\\Data\\Zhu\\EC_lab_test_pyhton\\' 
if not by_channel:
	# file if saving individually
	save_path += 'aa.csv'

bl = ebl.BiologicDevice( 'USB0')
bl.connect()

print(bl.info)
print(bl.kind)
prg = ebp.OCV( device=bl, params = params, channels= channels, autoconnect = False)

prg.run()
prg.save_data( save_path, by_channel = by_channel )
