#!/usr/bin/python
'''
*  Copyright (C) Gassan Idriss <ghassani@gmail.com>
*
* This program is free software ; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation ; either version 2 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY ; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with the program ; if not, write to the Free Software
* Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
*
* @file akseed_calc.py
* @brief Calculates AKSEEDNO challenge response for newer Samsung basebands
* @author Gassan Idriss <ghassani@gmail.com>
'''

import sys
import argparse
import math
import six

'''
Used in test, iterate over and calculate each with -t
'''
testData = {
	"1349-121-139"   : "400-91-114",
	"10441-13-55"    : "1279-91-94",
	"5611-121-143"   : "3705-96-114",
	"9847-174-197"   : "2069-94-123",
	"29999-241-2711" : "20088-98-133",
	"973-167-19"	 : "207-96-122",
	"20437-229-2579" : "13772-98-131",
	"2021-145-167"   : "425-96-118",
	"2491-83-101"    : "1179-95-108",
	"3959-124-143"   : "1219-94-115",
}

'''
Some devices have different amounts that are 
added to the final calulcation of each segment
'''
addOffsets = {
	"Default"	    : 89,
	"Marvell" 		: 0,
	"SM-N900S" 		: 51,
	"Korea" 		: 51,
	"SM-N900L" 		: 71,
	"SM-G900L" 		: 47,
	"SM-G900K" 		: 54,
	"SM-G900S" 		: 73,
	"SHV-E470S" 	: 73,
	"SM-N900K" 		: 61,
	"SHV-E250K" 	: 88,
}

def CalculateAkseed(number1, number2, number3, addOffset=addOffsets['Default']):  
	i = 1
	calc1 = number2
	while (i <= (number3/2)):
		calc1 = (((number2 * number2) % number1) * calc1) % number1
		i+=1

	calc1 += addOffset

	calc2  = round((number1 * 0x181E5) % math.log(number1)) + addOffset
	calc3  = round(((number2 * number1) / number1) / math.log(number2)) + addOffset	
	return "%d-%d-%d" % (calc1,calc2,calc3)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number1', metavar='number1', help='The 1st number in the akseed challenge.', nargs='?')
    parser.add_argument('number2', metavar='number2', help='The 2nd number in the akseed challenge.', nargs='?')
    parser.add_argument('number3', metavar='number3', help='The 3rd number in the akseed challenge.', nargs='?')
    parser.add_argument('-t', '--test', help='Run against the test numbers. Ignores other input.', action='store_true')

    args = parser.parse_args()

    if args.test is True:
    	for challenge, expected in six.iteritems(testData):
    		number1, number2, number3 = challenge.split("-")
    		result = CalculateAkseed(int(number1), int(number2), int(number3))
    		print ("Input: %s Result: %s Expecting: %s" % (challenge, result, expected))
    elif args.number1 is not None and args.number2 is not None and args.number3 is not None:
    	print ("%s" % CalculateAkseed(int(args.number1), int(args.number2), int(args.number3)))
    else:
    	parser.print_help()

if __name__ == '__main__':    
    main()


