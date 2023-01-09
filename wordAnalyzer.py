"""
This program reads a list of words given to it and runs certain statistics on them,
including the frequencies of the lengths of the words, the maximum number of letters
in a word in the list, the total number of certain lengths of words, and write the word
information to a file in the user's computer.

Author: Réna Hajjar
Date: November 16, 2022
"""

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def readWords(url):
    """
    This function takes the url to the website with the list of words and creates a list of
    the words as strings

    Returns: list of words
    """

    #reads list of words from website
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')

    #creates a list of each word
    words = data.split()

    return words

def wordCount(wordList):
    """
    This function takes a list of strings and creates a dictionary of the lengths of words
    and their frequencies

    Returns: dictionary of lengths and frequencies
    """
    wordDict = {}

    #for loop totals the number of words of each length and adds it to the dictionary
    for word in wordList:
        key = len(word)
        count = 0
        for word in wordList:
            if key == len(word):
                count += 1
        wordDict[key] = count #adds the length as the key in dictionary and the number of appearances as value
    return wordDict

def totalWords(wordDict, n, m):
    """
    This function takes the dictionary of lengths and frequencies and two integers from the users
    and totals the number of words from the first length to the second.

    Returns: total number of words (int)
    """
    if n <= m: #ensures the first value entered is greater than the second
        number = 0
        number += n
        total = 0

        #totals the values from key n to key m
        while number <= m: 
            total += wordDict[number]
            number += 1

        return total
    else: #returns 0 if there was invalid input
        return 0

def maxWordLength(wordDict):
    """
    This function takes the dictionary of lengths and frequencies and returns the longest possible
    number of characters in all of the words.

    Returns: int
    """
    return max(wordDict) #uses built in max function to return the highest key

def maxFrequency(wordDict):
    """
    This function takes the dictionary of lengths and frequencies and returns the length with the
    highest frequency

    Returns: int
    """
    maximum = max(wordDict.values()) #creates tuples of the values in the dictionary (the frequencies of words) and finds the max
    maxKey = 0

    #for loop finds the key that corresponds to the maximum frequency of length
    for key in wordDict.keys():
        if wordDict[key] == maximum:
            maxKey = key
    return maxKey
    
    

def writeToFile(wordDict):
    """
    This function takes the dictionary of lengths and frequencies and writes each length and frequency to a
    new file on the user's device.

    Returns: none
    """
    #opens file to write the values in
    stats = open('statWords.txt', 'w')
    
    #goes through each pair in the dictionary and writes the values to the file in a user-friendly way
    for x in wordDict:
        stats.write("There are ")
        stats.write(str(wordDict[x]))
        stats.write(' words of length ')
        stats.write(str(x))
        stats.write('\n')
    stats.close()

def main():
    """
    This function tests each of the above functions with the given url from the assignment description, and
    provides user-friendly information as to what the program is doing.
    """
    #website that provides the words for the example
    url = 'https://research.cs.queensu.ca/home/cords2/words.txt'

    #calls function to create list of words
    wordList = readWords(url)
    print('Your word list consists of the following:', wordList)

    #calls function to create the dictionary of lengths and frequencies
    wordDict = wordCount(wordList)
    print('The number of words of specific lengths are as follows:')
    print(wordDict)

    #asks the user for bounds of lengths to total
    print("The following input will take 2 integer values you enter and find the "+
          "total number of words from the first length you enter to the second " +
          "length you enter.")
    n = int(input("Enter the lower length you'd like to find the sums of:"))
    m = int(input("Enter the upper length you'd like to find the sums of:"))
    length= totalWords(wordDict, n, m)
    print("The total number of words from length " + str(n) +
          " to length " + str(m) + " is", length)

    #calls function to find the maximum length in the list of words
    maxLength = maxWordLength(wordDict)
    print("The highest length of any word in your list is", maxLength)

    #calls function to find the length with the highest frequency
    maxFreq = maxFrequency(wordDict)
    print("The most common length of word in your list is", maxFreq)

    #writes the data to a file
    writeToFile(wordDict)
    print("Writing your dictionary of lengths to a file...")
    print("File has been written! Your file is named statWords.txt and is in the same place as this program.")
    

main()



    
