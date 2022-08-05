"""
Desc: given a string s containing only characters ( ) { } [ ], determine if string is valid with opening and closing rules
"""

def isValid(self, s: str) -> bool:
        stack = []
        mydict = {"]":"[", "}":"{", ")":"("}
        for char in s: 
            if char in mydict and (stack == [] or stack.pop() != mydict[char]):
                    return False
            else:
                stack.append(char)
        return stack == []
