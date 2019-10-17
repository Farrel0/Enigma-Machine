# Engigma machine.
import os

debug = 0
lowerBound = 32
upperBound = 127
characterRange = upperBound - lowerBound


def mydebug(message):
    if debug == 1:
        print(message)


class Enigma:

    def __init__(self, keys, initialOffsets, size=95):

        self.myCypherArray = []
        self.mykey = keys[0]
        self.myLatchPoint = 0
        self.myOffset = initialOffsets[0]
        self.characterRange = size
        self.internalEnigmaMachine = []

        for i in range(self.characterRange):
            self.myCypherArray.append([-1, -1])

        for i in range(self.characterRange):
            nextLink = (i + ord(self.mykey[i % len(self.mykey)])) % self.characterRange

            # links can not be shared, if the position is already taken, find the next open link.
            while self.myCypherArray[nextLink][1] > -1:
                nextLink = (nextLink + 1) % self.characterRange

            self.myCypherArray[i][0] = nextLink
            self.myCypherArray[nextLink][1] = i

        # Choose an arbitrary point as a latch point
        self.myLatchPoint = (ord(self.mykey[0])^2) % self.characterRange

        # if there is more than one key in the input set, create an internal enigma machine
        if len(keys) > 1:
            self.internalEnigmaMachine = Enigma(keys[1:], initialOffsets[1:], size)

    def reflectSignal(self, wirenumber):

        if wirenumber == 0:
            return 0
        elif (wirenumber % 2) == 0:
            return wirenumber - 1
        else:
            return wirenumber + 1

    def connect(self, wireNumber):
        mydebug("Signal received on wire " + str(wireNumber) + " with offset " + str(self.myOffset))
        outbound = (self.myCypherArray[(wireNumber + self.myOffset) % self.characterRange][
                        0] - self.myOffset) % self.characterRange
        mydebug("Signal outbound to case " + str(outbound))
        if self.internalEnigmaMachine:
            inbound = self.internalEnigmaMachine.connect(outbound)
        else:
            inbound = self.reflectSignal(outbound)
        return (self.myCypherArray[(inbound + self.myOffset) % self.characterRange][
                    1] - self.myOffset) % self.characterRange

    def increment(self):
        if not self.internalEnigmaMachine:
            self.myOffset = (self.myOffset + 1) % self.characterRange
        else:
            self.myOffset = (self.myOffset + self.internalEnigmaMachine.increment()) % self.characterRange
        return self.myOffset == self.myLatchPoint

    def encodeLetter(self, letter):
        encodedLetter = letter

        if lowerBound <= ord(letter) < upperBound:
            mydebug("Calling connect with a " + chr(ord(letter)) + " on wire " + str((ord(letter) - lowerBound)))
            encodedLetter = chr(self.connect(ord(letter) - lowerBound) + lowerBound)
            self.increment()

        return encodedLetter

    def encodeMessage(self, message):
        toEncode = message
        encodedMessage = ""
        while len(toEncode) > 0:
            mydebug("Calling encode letter with " + toEncode[0])
            encodedMessage = encodedMessage + self.encodeLetter(toEncode[0])
            toEncode = toEncode[1:]
        return encodedMessage


# Check existence of data files needed.

# input file
# output file (should not exist)

# Read input file


fileIn = open('toCode.txt')
message = fileIn.read()
passwords = ['Rod','Jane','Freddie']
offsets = [14, 3, 26]
em = Enigma(passwords, offsets)
encodedMessage = em.encodeMessage(message)
try:
    os.remove('output.txt')
except OSError:
    pass
fileOut = open('output.txt', 'w')
fileOut.write(encodedMessage)
fileOut.close()
