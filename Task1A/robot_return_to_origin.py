class Solution(object):
    def judgeCircle(self, moves):
        x_count = 0
        y_count = 0

        for move in moves:
            if(move == 'L'):
                x_count -= 1
            elif(move == 'R'):
                x_count += 1
            elif(move == 'U'):
                y_count += 1
            elif(move == 'D'):
                y_count -= 1

        if(x_count == 0 and y_count == 0):
            return True
        else:
            return False
        
