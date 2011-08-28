#!/usr/bin/python
from daemon import Daemon
import sys
import time
import logging

PIDFILE = '/var/run/yourdaemon.pid'
LOGFILE = '/var/log/yourdaemon.log'

# Configure logging
logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)

class YourDaemon(Daemon):

	def run(self):
		# Define your tasks here
		# Anything written in python is permitted
		# For example you can clean up your server logs every hour
		
		
		# Logging errors and exceptions
		try:
			pass
		except Exception, e:
			logging.exception('Human friendly error message, the exception will be captured and added to the log file automaticaly')

		while True:
			# The daemon will repeat your tasks according to this variable
			# it's in second so 60 is 1 minute, 3600 is 1 hour, etc. 
			time.sleep(60)

if __name__ == "__main__":

	daemon = YourDaemon(PIDFILE)

	if len(sys.argv) == 2:

		if 'start' == sys.argv[1]:
			try:
				daemon.start()
			except:
				pass

		elif 'stop' == sys.argv[1]:
			print "Stopping ..."
			daemon.stop()

		elif 'restart' == sys.argv[1]:
			print "Restaring ..."
			daemon.restart()

		elif 'status' == sys.argv[1]:
			try:
				pf = file(PIDFILE,'r')
				pid = int(pf.read().strip())
				pf.close()
			except IOError:
				pid = None
			except SystemExit:
				pid = None

			if pid:
				print 'YourDaemon is running as pid %s' % pid
			else:
				print 'YourDaemon is not running.'

		else:
			print "Unknown command"
			sys.exit(2)
			sys.exit(0)
	else:
		print "usage: %s start|stop|restart|status" % sys.argv[0]
		sys.exit(2)

