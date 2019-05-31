# Find min

def main():
    def findMin(x):
        minNum = x[0]
        for i in x:
            if minNum > i:
                minNum = i
        return minNum

    print(findMin([0,1,2,3,4,5,-3,34,-56,-1000])) # = -1000

if __name__=='__main__':
    main()
