from statistics import mean
import sprints
import unittest

class TestFunction(unittest.TestCase):
    

    def test_All_Even_Int(myFunction):
        numList=[10,8,66,8]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(EvenAvg, 23.0)
        

    def test_All_Int(myFunction):
        numList=[10,53,8,91,66,17,8]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(EvenAvg, 23.0)
        
    def test_All_Float(myFunction):
        numList=[21.1910,45.382,95.77]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(maxFloat, 95.77)

    def test_All_String(myFunction):
        numList=["Hello","World"]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(EvenAvg, 0)
        myFunction.assertEqual(maxFloat, 0)    

    def test_Int_and_Float(myFunction):
        numList=[10,21.1910,8,45.382,66,95.77,8]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(EvenAvg, 23.0)
        myFunction.assertEqual(maxFloat, 95.77)  

    def test_Int_Float_and_String(myFunction):
        numList=[10,21.1910,8,"Hello",45.382,66,95.77,8]
        EvenAvg= mean(numList)
        maxFloat= max(numList)
        
        myFunction.assertEqual(EvenAvg, 23.0)
        myFunction.assertEqual(maxFloat, 95.77) 

if __name__ == '__main__':
    unittest.main()