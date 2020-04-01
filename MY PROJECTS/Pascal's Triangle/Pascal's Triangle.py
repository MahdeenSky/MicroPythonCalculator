class Solution(object):
    def generate(self, numRows: int): #another solution involving append
        res = []
        
        for ri in range(numRows):
            if ri == 0:
                res.append([1])
                print([1])
            else:
                row = [1]
                for i in range(1, len(res[ri-1])):
                    row.append(res[ri-1][i-1] + res[ri-1][i])
                    
                res.append(row + [1])
                print(row + [1])         
       

number_of_Rows = int(input("Enter num of rows: "))
Solution.generate(0, number_of_Rows)