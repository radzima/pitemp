#!/usr/bin/env python

from subprocess import Popen,PIPE
import time,sys,argparse

reload(sys)
sys.setdefaultencoding('utf-8')

temperature_file="/sys/class/thermal/thermal_zone0/temp"

parser = argparse.ArgumentParser(description="Get the Raspberry Pi's temperature")
parser.add_argument("-p","--precision",
	action="store",
	type=int,
	default=1,
	choices=range(0,4),
	help="Decimal place precision, from 0 to 3.") 
parser.add_argument("-l","--live",
	action="store_true",
	help="Monitor the temperature live.")
parser.add_argument("-i","--interval",
	action="store",
	default=5,
	type=int,
	help="Refresh interval for the live view.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-c","--celsius",
	action="store_true",
	help="Show the temperature in celsius.")
group.add_argument("-f","--fahrenheit",
	action="store_true",
	help="Show the temperature in fahrenheit.")

args = parser.parse_args()

def getTemp():
	with open(temperature_file) as f:
		c = map(float,f)
		c = float(c[0]) / 1000
		f = (c * 1.8) + 32
		return c,f

def celsiusToF(celsius):
	fahrenheit = (celsius * 1.8) + 32
	return fahrenheit

def main():
	celsius,fahrenheit = getTemp()
	if args.live:
		print "|\tCelsius\t\t|\tFahrenheit\t|"
		while True:
			celsius,fahrenheit = getTemp()
			if args.precision > 2:
				spacer = "\t\t"
			else:
				spacer = "\t\t\t"
			print "\t{0:.{prec}f}{1}C{space}{2:.{prec}f}{3}F\r".format(celsius,u"\u00B0",fahrenheit,u"\u00B0",prec=args.precision,space=spacer),
			sys.stdout.flush()
			time.sleep(args.interval)
			print "\r",
	elif args.fahrenheit:
		print "Temperature:\t{:.{prec}f}{}F".format(fahrenheit,u"\u00B0", prec=args.precision)
	elif args.celsius:
		print "Temperature:\t{:.{prec}f}".format(celsius,prec=args.precision)
	else:
		print "Celsius:\t{:.{prec}f}{}C".format(celsius,u"\u00B0",prec=args.precision)
		print "Fahrenheit:\t{:.{prec}f}{}F".format(fahrenheit,u"\u00B0",prec=args.precision)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\nExiting...\n"
		pass
