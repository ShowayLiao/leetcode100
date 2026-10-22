import sys

def quick_sort(data:list):

    def sort(left:int,right:int):

        while left<=right:

            pivot = data[(left+right)//2]

            less =  left

            current = left

            greater = right

            while current<=greater:

                if data[current]<pivot:
                    data[current],data[less] = data[less],data[current]
                    current+=1
                    less+=1

                elif data[current]>pivot:

                    data[current],data[greater] = data[greater],data[current]
                    greater-=1

                else:

                    current+=1

            if less-left < right-greater:

                sort(left,less-1)

                left = greater+1

            else:

                sort(greater+1,right)

                right = less-1


    sort(0,len(data)-1)


def solve():

    data = sys.stdin.buffer.read().split()

    if not data:
        return


    values = list(map(int,data[1:]))

    quick_sort(values)

    print(*values)

if __name__ =="__main__":

    solve()