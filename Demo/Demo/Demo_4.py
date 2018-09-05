# -*- coding: utf-8 -*-
import json


class Who:

    def __init__(self):
        self.key = {
            "oe": "0", "n": "0", "z": "0", "on": "0",
            "oK": "1", "6": "1", "5": "1",
            "ow": "2", "-": "2", "A": "2", "oc": "2",
            "oi": "3", "i": "3", "o": "3", "oz": "3",
            "7e": "4", "v": "4", "P": "4", "7n": "4",
            "7K": "5", "4": "5", "k": "5", "7": "5", "7v": "5",
            "7w": "6", "C": "6", "s": "6", "7c": "6",
            "7i": "7", "S": "7", "l": "7", "7z": "7",
            "Ne": "8", "c": "8", "F": "8", "Nn": "8", "ov": "8",
            "NK": "9", "E": "9", "q": "9", "Nv": "9"
        }


    def calc(self, string, debug=False):
        result = ""
        string = string.replace("*S1*", "oKvPoK6kow65oK4ioenioi6q")
        while string:
            if len(string) > 1:
                if string[0:2] not in self.key:
                    if debug:
                        print(string[0:1], self.key[string[0:1]])
                    result += self.key[string[0:1]]
                    string = string[1:]
                else:
                    if debug:
                        print(string[0:2], self.key[string[0:2]])
                    result += self.key[string[0:2]]
                    string = string[2:]
            else:
                if debug:
                    print(string, self.key[string])
                result += self.key[string]
                string = ""
        return result
