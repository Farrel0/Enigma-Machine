#Enigma Machine

##Project Goals and initial consideration.

Create a software encryption program that encrypts text messages in a manner based on the World War 2 German 'Enigma' machine.

Many documents here will assume at least a base level knowledge of the construction of the enigma machine.

The software will perform the following tasks.

Read a file of encryptable data in the form of a .txt file, using the ASCII character encoding standard.
Generate encoding 'rotors' from a specified number of passwords.
Parse the data character by character and apply an encryption cypher in a manner similar to the enigma machine
Write data out to a new .txt file in the same folder.


##Initial considerations

ASCII contains provision for certain non-printable characters, given that the data will be coming from a text file, it is likely
that these can largely be ignored by the parser and simply passed on to the output without attempting to apply encryption.
The parser module should be built in a manner to allow exceptional cases to be specified, however.

For the purpose of this exercise, there will be some changes for the sake of easier development and use. The enigma machine will
function on the standard printable ASCII characters between 32 (space) and 126 (~), a total of 95 useable characters instead of
the original 26 capital letters of the wartime model. This will necessitate the creation of larger cypher rotors of 95 connections
instead of the original ones.

The initial setup of the machine for each message was performed by sending three unencrypted letters to specify the initial rotor
positions followed by three encrypted letters to begin the scrambling process. These were considered as separate to the body of
the message itself. Since this amounts to an extra password, the initial rotor positions will be specified by an additional
optional password.

One of the flaws of the enigma machine was that it could not encode a letter back to itself. This was due to the nature in which it
operated in sending electrical current down a series of wires and then reflecting them back through the same set of wires to a
lamp. A signal coming down a wire corresponding to a letter could not be sent back through the same wire. Since we are operating
digitally, this flaw becomes redundant. Due to the nature of working with an odd number of characters (95) it is necessary to do
away with the limitation.

For the sake of simplicity, the simple 'crossed wire pairs' from the keyboard into the system will be omited.
