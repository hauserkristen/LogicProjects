from CollisionDetection import CollisionDetection
from Position import Position
from Node import Node

def main():
    #Construct nodes
    start_a = Position(2,3,4)
    end_a = Position(0,1,2)
    length_a = 4
    width_a = 6
    height_a = 2
    node_a = Node(start_a, end_a, length_a, width_a, height_a)
    
    start_b = Position(0,0,1)
    end_b = Position(0,1,1)
    length_b = 3
    width_b = 2
    height_b = 8
    node_b = Node(start_b, end_b, length_b, width_b, height_b)

    #Check for static collision
    static_hit = CollisionDetection.check_for_collision(node_a, node_b)
    print('Static hit: ' + str(static_hit))

    #Check for linear velocity collision
    time_step = 0.2
    linear_hit = CollisionDetection.check_for_collision_velocity(node_a, node_b, time_step)
    print('Linear hit with time step (' + str(time_step) + ' seconds): ' + str(linear_hit))
    
    return

if __name__ == "__main__":
    main()