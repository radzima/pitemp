# pitemp
A simple script to get the temperature of a Raspberry Pi in either celsius or fahrenheit. Reads the output from 'vcgencmd measure_temp' and presents it cleanly in either celsius or fahrenheit.

	usage: pitemp.py [-h] [-c | -f]

		Prints the temperature of the Raspberry Pi in both celsius and fahrenheit
		-f Print the temperature in fahrenheit
		-c Print the temperature in celsius

## Example

	pi@raspberrypi:~ $ ./pitemp.py
	50.80
	123.44°F

	pi@raspberrypi:~ $ ./pitemp.py -f
	122.54

	pi@raspberrypi:~ $ ./pitemp.py -c
	49.80
