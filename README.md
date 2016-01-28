# AKSEED Challenge Calculator

This can calculate the proper response to give back to Samsung basebands for the AT+AKSEEDNO command.
When sending AT commands, some commands may require AKSEEDNO challege request and response before continuing, like with IMEISIGN. Example:

    TX: AT+AKSEEDNO=1,0
    RX: +AKSEEDNO:1,XXX-XXX-XXX (Where XXX is a random number) 
    TX: AT+AKSEEDNO=0,XXX-XXX-XXX (Where XXX is the calculated challenge response)
    RX: +AKSEEDNO:0,OK

# Requirements

Python w/ six module (2.7 or 3.x)

# Usage
Take the three numbers and pass them as arguments to the script:

    python akseed_calc.py [NUMBER1] [NUMBER2] [NUMBER3]

