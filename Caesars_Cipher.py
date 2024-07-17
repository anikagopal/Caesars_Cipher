{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #This program is the starter code for the Programming Caesar's Cipher Project. \
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)\
\
# Global variables\
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
initialPosition = 0\
shiftedPosition = 0\
shiftedPosition = ""\
\
# Run code\
\
# Introduction\
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \\n\\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\\n\\nLet's get started!\\n")\
\
# Receive user input\
initialMessage = input("What is your message? ")\
key = int(input("What is the key? Choose a number from 0 to 25. "))\
mode = input("Do you want to encrypt or decrypt? ")\
shiftedMessage = ""\
# Encrypt or decrypt the message\
for character in initialMessage:\
  if character in possibleCharacters:\
    initialPosition = possibleCharacters.find(character)\
    \
    if mode.lower() == "encrypt":\
      shiftedPosition = initialPosition + key\
  \
    elif mode.lower() == "decrypt":\
      shiftedPosition = initialPosition - key\
  \
    if shiftedPosition >= len(possibleCharacters):\
      shiftedPosition = shiftedPosition - len(possibleCharacters)\
  \
    elif shiftedPosition < 0:\
      shiftedPosition = shiftedPosition + len(possibleCharacters)\
  \
    shiftedMessage = shiftedMessage + (possibleCharacters[shiftedPosition])\
\
  else:\
    shiftedMessage = shiftedMessage + character\
    \
# Print the shifted message\
print("Your " + mode.lower() + "ed message is: " + shiftedMessage)}