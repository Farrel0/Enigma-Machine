# Enigma-Machine
An encryption system based on the world war 2 enigma cypher machine.

##Motivation
Written as a means of learning the basics of the python programming language.

##Build Status

Fuctionality - Complete
Testing status - Some known issues

##Features

Simple command line interface.
Variable cypher levels - Input at least one password and cypher offset.
Encodes standard ASCII text files
Symetrical encoding - Decrypt a file by encrypting an already encrypted file with the same passwords

##Testing

Being written

##Usage

construct an enigma object with two arguments. Note: the lists must be of equal length.
passwords = A list of strings each of which will generate cypher rotors
offsets = A list of integers which determine the initial position of each of the rotors

Call the encodeMessage(string) -> string method with the message to encode