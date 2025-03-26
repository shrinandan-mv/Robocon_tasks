class Solution(object):
    def generate(self, numRows):
        final_list = [[1]]

        if(numRows >= 2):
            final_list = [[1], [1,1]]
        
        for i in range(2, numRows):
            row_list = [1]

            for j in range(1, i):
                row_list.append(final_list[i-1][j-1] + final_list[i-1][j])

            row_list.append(1)
            final_list.append(row_list)


        return final_list


        
