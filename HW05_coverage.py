import unittest
import random

def count_vowels(word):
    """Counts and returns the number of vowels in a string"""
    word=word.lower()
    num_of_vowels = 0

    for letter in word:
        if letter in "aeiou":
            num_of_vowels+=1
    return num_of_vowels

def find(target, collection):
    """Finds the last occurance of a target instance in a list"""
    counter = None
    for offset, c in enumerate (collection):
        if c == target:
            counter = offset
    return counter

def random_number_generate(min,max):
    """Generator to find a random number between a minimum and a maximum range (including both the minimum and maximum numbers)"""
    while True:
        yield random.randint(min,max)
    
def find_target(target, min_value, max_value, max_attempts):
    """Returns the number of times it takes to randomly generate a number within a minimum and maximum range (including min and max)
    to find a target value. Takes in a parameter specifying the maximum attempts to find this target number using the random generator"""
    if min_value > target or max_value < target:
        raise ValueError("Target is not in min and max range")
    answer = None
    gen = random_number_generate(min_value, max_value)
    for attempt in range(max_attempts):
        if next(gen) == target:
            answer = attempt + 1
            break
    return answer 

def my_enumerate(sequence):
    """Generator that goes through a sequence and returns the index and value at that index starting from index 0"""
    for index in range(len(sequence)):
        yield index, sequence[index]

class FindTarget (unittest.TestCase):
    def test_find(self):
        """tests find funciton when searching a list for an target"""
        self.assertEqual(find('p','apple'),2)               #checks lowercase letter in string with multiple occurances
        self.assertEqual(find(27,[27,11,34,11,4]),0)        #checks number in list of numbers
        self.assertEqual(find('z', "hello world"), None)    #checks non-present letter in string
        self.assertEqual(find('a','abcdefga'),7)            #checks letter with multiple occurances
        self.assertEqual(find(0,[0, 7, 90, 3, 0, 5, 0]),6)     #checks number with multiple occurances
        self.assertEqual(find(0,[0, 1, 2, 3, 4, 5, 6]),0)     #checks boundary condition with position being 0

class CountVowelsTest (unittest.TestCase):
    def test_count_vowels(self):
        """tests count vowels function to count number of vowels in a string"""
        self.assertEqual(count_vowels('hello world'),3)    #checks lowercase vowels
        self.assertEqual(count_vowels('hEllO wOrld'),3)    #checks uppercase vowels
        self.assertEqual(count_vowels('gg wrld'),0)       #checks no vowels
        self.assertEqual(count_vowels('aeiou'),5)          #checks all vowels
        self.assertEqual(count_vowels(""),0)               #checks empty string

class RandomGeneratorTest (unittest.TestCase):
    """tests find target function"""
    def test_find(self):
        self.assertEqual(find_target(5,5,5,1),1)        #tests positive numbers
        with self.assertRaises(ValueError):             #tests if number is out of range
            find_target(-1,0,10,10)
        self.assertLess(find_target(2,1,2,1000),1000)   #tests a 99.9% likely answer
        self.assertEqual(find_target(1,1,1000,0),None)  #tests if no numbers are found in the range


    unittest.main(exit=False, verbosity=2)
