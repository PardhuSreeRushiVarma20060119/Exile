#
# Regular cron jobs for the exile package.
#
0 4	* * *	root	[ -x /usr/bin/exile_maintenance ] && /usr/bin/exile_maintenance
