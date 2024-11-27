import logging

import easy_biologic as ebl
import easy_biologic.base_programs as ebp

logging.basicConfig( level = logging.DEBUG )

channels = [ 1]
by_channel = False
params = { 
	'voltages':  [ 0]* 2,
	'durations': [ 2 ]* 4
}

save_path = 'data/ca-limit'
if not by_channel:
	# file if saving individually
	save_path += '.csv'

bl = ebl.BiologicDevice( 'USB0' )
prg = ebp.CALimit( bl,  params, channels = channels )

prg.run()
prg.save_data( save_path, by_channel = by_channel )