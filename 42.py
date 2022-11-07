# Trapping Rain Water
from typing import List
class Solution:
    def __init__(self):
        self.stack = []
        self.water = 0
        
    def push(self, num):
        pointer = len(self.stack) - 1
        while self.stack and self.stack[pointer] < num:
            n = min(num, self.stack[0])
            m = self.stack[pointer]
            if self.stack and self.stack[0] > m:
                self.water += n - m
                self.stack[pointer] = n
                pointer -= 1
            else: 
                while self.stack and len(self.stack) > pointer: self.stack.pop()
                pointer = len(self.stack) - 1
        self.stack.append(num)
            
    def trap(self, height: List[int]) -> int:
        for h in height:
            self.push(h)
        return self.water