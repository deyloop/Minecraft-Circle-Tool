import sys
from math import floor,sqrt

def main():
    radius = 0
    if len(sys.argv) == 2:
        radius = int(sys.argv[1])
    else:
        print(f'Usage: {sys.argv[0]} [radius]')
        exit()
    
    printCircle(radius)
    
def Distance(point):
    '''
    Caluculates the Euclidian distance of a 2D point from the origin
    Arguments:
    [IN] point - tuple representing the 2D point
    '''
    ( x, y )= point
    return sqrt(x*x + y*y)  

def printCircle(radius: int):
    '''
    Outputs the block pattern to be used to make a quarter of a circle into
    a file named circleBlocks.txt
    Arguments:
    [IN] radius -   The radius of the circle to create
    '''
    with open('circleBlocks.txt','w') as output:
        
        for y in range(radius+1):
            
            for x in range(radius+3):

                distance = floor(Distance((x,y)))
                
                if distance > radius:
                    break
                elif distance == radius:
                    output.write('#')
                else:
                    output.write('+')
            output.write(str(y)+'\n')
    

if __name__ == "__main__":
    main()