
Source={
    1:{
        1:{
            1:1,
            2:2,
            3:2,
            4:3
        },
        2:{
            1:2,
            2:3,
            3:4,
            4:5
        }
    },
    2:{
        1:{
            1:1,
            2:3,
            3:4,
            4:5
        },
        2:{
            1:2,
            2:4,
            3:5,
            4:6
        }
    }
}
lp =0
tony =(int(input("enter the value of i")))
miller =(int(input("enetyer the value of w")))
caption =(int(input("enter t6he value of s")))
for i in range(1,3):
    for j in range(1,3):
        for x in range(1,5):
            if tony == i and miller == j and caption == x:
                lp = lp+Source[i][j][x]
            print(lp)