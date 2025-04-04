
    def example1():
        for i in range( 3 ):
            try:
                x = int( input( "enter a number: " ) )
                y = int( input( "enter another number: " ) )
                print( x, '/', y, '=', x/y )
            except ZeroDivisionError as e:
                print('')
                

    def example2( L ):
        print( "\n\nExample 2" )
        sum = 0
        sumOfPairs = []
        for i in range( len( L ) ):
            sumOfPairs.append( L[i]+L[i+1] )

        print( "sumOfPairs = ", sumOfPairs )
    
    #def example3():


    def printUpperFile(fileName):
        file = open(fileName, "r")
        for line in file:
            print( line.upper() )
        file.close()
        
    def main():
        example1()
        L = [ 10, 3, 5, 6, 9, 3 ]
        example2( L )
        example2( [ 10, 3, 5, 6, "NA", 3 ] )
        #example3( [ 10, 3, 5, 6 ] )

        printUpperFile( "doesNotExistYest.txt" )
        printUpperFile( "./Dessssktop/misspelled.txt" )
        
    if __name__ == "__main__":
        try:
            main()
        except Exception as e:
            print("Exception raised during main()")

# except ZeroDivisionError as e:
#     print( "An error occurred: ", e )

# except ValueError as e:
#     print( "An error occurred: ", e )

# except IndexError as e:
#     print( "An error occurred: ", e )

# except FileNotFoundError as e:
#     print( "An error occurred: ", e )




