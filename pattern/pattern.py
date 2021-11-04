# this file will consist patterns example 


''' pattern1
 *  
 *   *          
 *   *   *      
 *   *   *   * 
'''



def pattern1(n):
    for row in range(n+1):
        for column in range(row):
            print(' * ' , end=' ')
        print('')



'''pattern2 (reverse)

            *   *   *   *
            *   *   *
            *   *
            *

'''

def pattern2(n):
    print('\n')
    for row in range(n):
        for column in range(n - row):
            print(' * ' , end=' ')
        print('')

'''pattern3
                        1
                        1 2
                        1 2 3
                        1 2 3 4

'''


def pattern3(n):
    print('\n')
    for row in range(1 , n+1):
        for column in range(1,row+1):
            print( column , end=' ')
        print('')

'''pattern4 
                    1 2 3 4
                    1 2 3
                    1 2
                    1

'''

def pattern4(n):
    print('\n')
    for row in range(1 , n+1):
        for column in range( 1 , (n+2-row)):
            print( column , end=' ')
        print('')

'''pattern5

                1 2 3 4
                1 2 3
                1 2
                1

'''

def pattern5(n):
    print('\n')
    for row in range(0 ,n):
        for column in range( 1 , (n+1-row)):
            print( column , end=' ')
        print('')



# logical 
def pattern6(n):
    for row in range(n):
        pass 



'''pattern 7 
            
                        *
                        *  *
                        *  *  *
                        *  *  *  *
                        *  *  *  *  *
                        *  *  *  *  *  *
                        *  *  *  *  *  *  *
                        *  *  *  *  *  *
                        *  *  *  *  *
                        *  *  *  *
                        *  *  *
                        *  *
                        *        

'''

# here : n_rows = 14/2 = 7 

# 4*2 = 8 
# 4 cond break
# 8- 5 = 3 

def pattern7(n):
    print('\n')
    for row in range(2*n):
        if row <= n :
            c = row   # until row = n : i'e row= 7 (normal print)
        else:
            c = 2*n + 1 - row -1   
    
        for col in range(c):
            print('* ' , end=' ')

        print('')



        

def pattern8(n):
    pass 
















if __name__ == '__main__':
    pattern1(4)
    pattern2(4)
    pattern3(4)
    pattern4(4)
    pattern5(4)
    pattern7(7)