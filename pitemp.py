#!/usr/bin/env python

from subprocess import Popen,PIPE
import time,sys,argparse

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Get the Raspberry Pi's temperature")
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

def getTempString():
	result = Popen(["vcgencmd","measure_temp"],stdout=PIPE,stderr=PIPE)
	output,error = result.communicate()
	return output

def convertToC(text):
	newString = text.split("=",1)[-1]
	celsius = float(newString.split("'",1)[0])
	return celsius

def celsiusToF(celsius):
	fahrenheit = (celsius * 1.8) + 32
	return fahrenheit

def main():
	tempString = getTempString()
	celsius = convertToC(tempString)
	fahrenheit = celsiusToF(celsius)
	if args.live:
		print "|\tCelsius\t\t|\tFahrenheit\t|"
		while True:
			try:
				tempString = getTempString()
				celsius = convertToC(tempString)
				fahrenheit = celsiusToF(celsius)
				print "\t{0:.2f}{1}C\t\t\t{2:.2f}{3}F\r".format(celsius,u"\u00B0",fahrenheit,u"\u00B0"),
				sys.stdout.flush()
				time.sleep(args.interval)
				print "\r",
			except (KeyboardInterrupt, SystemExit):
				print "Exiting..."
				raise
	elif args.fahrenheit:
		print "Temperature:\t{:.2f}".format(fahrenheit)
	elif args.celsius:
		print "Temperature:\t{:.2f}".format(celsius)
	else:
		print "Celsius:\t{:.2f}{}C".format(celsius,u"\u00B0")
		print "Fahrenheit:\t{:.2f}{}F".format(fahrenheit,u"\u00B0")

if __name__ == "__main__":
	main()
