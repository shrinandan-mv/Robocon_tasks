import sys

from MapNode import MapNode

class PlannerNode:
    def __init__(self):
        self.current_obj=MapNode()
        
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1

        self.wall_callback()

    def wall_callback(self):
        # current_obj has all the attributes to help you in in your path planning !
                
        pass # Your code goes here. You need to figure out an algorithm to decide on the best direction of movement of the bot based on the data you have.
        # after deciding on the direction, you need to call the direction_callback() function as done in example 1.
    

        visited_coords = [self.current_obj._MapNode__map.start]
        last_node_moves = ["down"]

        #print("AT BEGINNING")
        #print("visited_coords", visited_coords)
        #print("last_node_moves", last_node_moves)
        #print()
        #print()

        self.number_of_walls = self.check_number_of_walls()

        while(self.current_obj.current != self.current_obj._MapNode__map.end):

            if(self.current_obj.current not in visited_coords):
                visited_coords.append(self.current_obj.current)

            #print("visited_coords", visited_coords)
            #print("last_node_moves", last_node_moves)
            #print()
            #print()

            if((self.current_obj._MapNode__map.check_top_wall(self.current_obj.current) == False) and ((self.current_obj.current[0]-1, self.current_obj.current[1]) not in visited_coords)):
                self.current_obj.direction_callback("up")
                last_node_moves.append("up")

            elif((self.current_obj._MapNode__map.check_right_wall(self.current_obj.current) == False) and ((self.current_obj.current[0], self.current_obj.current[1]+1) not in visited_coords)):
                self.current_obj.direction_callback("right")
                last_node_moves.append("right")

            elif((self.current_obj._MapNode__map.check_bottom_wall(self.current_obj.current) == False) and ((self.current_obj.current[0]+1, self.current_obj.current[1]) not in visited_coords)):
                self.current_obj.direction_callback("down")
                last_node_moves.append("down")

            elif((self.current_obj._MapNode__map.check_left_wall(self.current_obj.current) == False) and ((self.current_obj.current[0], self.current_obj.current[1]-1) not in visited_coords)):
                self.current_obj.direction_callback("left")
                last_node_moves.append("left")

            else:
                previous_move = last_node_moves.pop()

                if(previous_move == "up"):
                    self.current_obj.direction_callback("down")
                elif(previous_move == "right"):
                    self.current_obj.direction_callback("left")
                elif(previous_move == "down"):
                    self.current_obj.direction_callback("up")
                elif(previous_move == "left"):
                    self.current_obj.direction_callback("right")

    def check_number_of_walls(self):
        number_of_walls = 0;
            
        if self.current_obj._MapNode__map.check_top_wall(self.current_obj.current):
            number_of_walls += 1
        if self.current_obj._MapNode__map.check_left_wall(self.current_obj.current):
            number_of_walls += 1
        if self.current_obj._MapNode__map.check_right_wall(self.current_obj.current):
            number_of_walls += 1
        if self.current_obj._MapNode__map.check_bottom_wall(self.current_obj.current):
            number_of_walls += 1

        return number_of_walls


if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
