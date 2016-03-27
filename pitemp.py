#!/usr/bin/env python

from subprocess import Popen,PIPE
import sys,argparse

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Get the Raspberry Pi's temperature")
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
	if args.fahrenheit:
		print "{:.2f}".format(fahrenheit)
	elif args.celsius:
		print "{:.2f}".format(celsius)
	else:
		print "{:.2f}{}C".format(celsius,u"\u00B0")
		print "{:.2f}{}F".format(fahrenheit,u"\u00B0")

if __name__ == "__main__":
	main()
