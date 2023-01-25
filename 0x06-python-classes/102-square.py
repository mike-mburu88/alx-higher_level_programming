#!/usr/bin/python3

"""Defines square as a class"""





class Square:
    
    """Represents a square  Attributes: size of each side"""
    
    def __init__(self, size=0):
        
        """initializes the square Args"""
        
        self.size = size
        

        
    def area(self):
        
        """calculates the square's area"""
        
        return (self.__size) ** 2
    

    
    
    
    def size(self):
        
        """getter of __size"""
        
        return self.__size
    

    
        
    def size(self, value):
        
        """setter of __size

        Args:

            value (int): the size of a size of the square

        Returns:

            None

        """
        
        if type(value) is not int:
            
            raise TypeError("size must be an integer")
        
        else:
            
            if value < 0:
                
                raise ValueError("size must be >= 0")
            
            else:
                
                self.__size = value
                

                
    def __lt__(self, other):
        
        """Compare if square is less than another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size < other.size
    

    
    def __le__(self, other):
        
        """Compare if square is less than or equal to another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size <= other.size
    

    
    def __eq__(self, other):
        
        """Compare if square is equal to another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size == other.size
    

    
    def __ne__(self, other):
        
        """Compare if square is not equal to another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size != other.size
    

    
    def __ge__(self, other):
        
        """Compare if square is greater than or equal to another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size >= other.size
    

    
    def __gt__(self, other):
        
        """Compare if square is greater than another by area

        Args:

            other (Square): square to compare against

        Returns:

            True or False

        """
        
        return self.size > other.size
