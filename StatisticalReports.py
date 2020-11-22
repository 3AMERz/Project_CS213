import inputFile

class Functions :


    # Number of books read by the whole group members
    def NBR_ALL () :

        x = len(inputFile.members)
        sum = 0
        for n in range(0, x):
            print("Member", n+1,"reed (", len(inputFile.members[n].LBooks),") books .")
            sum += len(inputFile.members[n].LBooks)
        print("The Number of books read by the whole group members is (", sum, ") books")
        print("-----------------------------------------------------------------------------------------")



    # Number of books read by the whole group members
    def PBR_ALL () :

        x = len(inputFile.members)
        sum = 0
        for n in range(0, x):
            z = len(inputFile.members[n].LBooks)
            for h in range (0 , z) :
                sum += inputFile.members[n].LBooks[h].pages
            print("Member", n + 1, "reed (", sum, ") pages .")
        print("The Number of pages read by the whole group members is (", sum, ") pages")
        print("-----------------------------------------------------------------------------------------")



    #Ranking of books categories mostly read by the group members
    def Rank_categ () :
        N = 0
        A = 0
        S = 0
        L = 0

        x = len(inputFile.members)
        sum = 0
        for n in range(0, x):
            z = len(inputFile.members[n].LBooks)
            for h in range(0, z):
                c = inputFile.members[n].LBooks[h].category
                if c == "Novel" :
                    N += 1
                elif c == "Autobiography" :
                    A += 1
                elif c == "scientific" :
                    S += 1
                elif c == "literature" :
                    L += 1
        print("The categories of books that group members read mostly are :")

        #Ranking
        NASL = [N, A, S, L]

        for y in range (1 , 5) :
            if N == max(NASL):
                print(y,"-  Novel =",N )
                NASL.remove(N)
            elif A == max(NASL):
                print(y,"-  Autobiography =",A )
                NASL.remove(A)
            elif S == max(NASL):
                print(y,"-  Scientific =",S )
                NASL.remove(S)
            elif L == max(NASL):
                print(y,"-  Literature =",L )
                NASL.remove(L)
        print("-----------------------------------------------------------------------------------------")



    #Ranking of group members based on number of books read
    def Rank_reedBK () :
        print("Ranking of group members based on number of books read is :\n")

        x = len(inputFile.members)
        mes = [None]*x
        names = [None]*x

        for q in range(0,x):
            names[q] = inputFile.members[q].name

        for n in range(0, x):
            mes[n] = len(inputFile.members[n].LBooks)

        # Ranking
        for y in range(0, x):
            if mes[0] == max(mes):
                print(y+1,"-",names[0],"is reeded = ", mes[0], "books")
                mes[0] = 0
            elif mes[1] == max(mes):
                print(y+1,"-",names[1],"is reeded = ", mes[1], "books")
                mes[1] = 0
            elif mes[2] == max(mes):
                print(y+1,"-",names[2],"is reeded = ", mes[2], "books")
                mes[2] = 0
            elif mes[3] == max(mes):
                print(y+1,"-",names[3],"reeded = ", mes[3], "books")
                mes[3] = 0
            elif mes[4] == max(mes):
                print(y+1,"-",names[4],"is reeded = ", mes[4], "books")
                mes[4] = 0
            elif mes[5] == max(mes):
                print(y+1,"-",names[5],"is reeded = ", mes[5], "books")
                mes[5] = 0
            elif mes[6] == max(mes):
                print(y+1,"-",names[6],"is reeded = ", mes[6], "books")
                mes[6] = 0
            elif mes[7] == max(mes):
                print(y+1,"-",names[7],"is reeded = ", mes[7], "books")
                mes[7] = 0
            elif mes[8] == max(mes):
                print(y+1,"-",names[8],"is reeded = ", mes[8], "books")
                mes[8] = 0
            elif mes[9] == max(mes):
                print(y+1,"-",names[9],"is reeded = ", mes[9], "books")
                mes[9] = 0
        print("-----------------------------------------------------------------------------------------")



    #Ranking of group members based on number of pages read
    def Rank_reedP () :
        print("Ranking of group members based on number of pages read is :\n")

        x = len(inputFile.members)
        sum = 0
        mes = [None]*x
        names = [None]*x

        for q in range(0,x):
            names[q] = inputFile.members[q].name

        for n in range(0, x):
            sum = 0
            z = len(inputFile.members[n].LBooks)
            for h in range(0, z):
                sum += inputFile.members[n].LBooks[h].pages
                mes[n] = sum

        # Ranking
        for y in range(0, x):
            if mes[0] == max(mes):
                print(y+1,"-",names[0],"is reeded = ", mes[0], "pages")
                mes[0] = 0
            elif mes[1] == max(mes):
                print(y+1,"-",names[1],"is reeded = ", mes[1], "pages")
                mes[1] = 0
            elif mes[2] == max(mes):
                print(y+1,"-",names[2],"is reeded = ", mes[2], "pages")
                mes[2] = 0
            elif mes[3] == max(mes):
                print(y+1,"-",names[3],"reeded = ", mes[3], "pages")
                mes[3] = 0
            elif mes[4] == max(mes):
                print(y+1,"-",names[4],"is reeded = ", mes[4], "pages")
                mes[4] = 0
            elif mes[5] == max(mes):
                print(y+1,"-",names[5],"is reeded = ", mes[5], "pages")
                mes[5] = 0
            elif mes[6] == max(mes):
                print(y+1,"-",names[6],"is reeded = ", mes[6], "pages")
                mes[6] = 0
            elif mes[7] == max(mes):
                print(y+1,"-",names[7],"is reeded = ", mes[7], "pages")
                mes[7] = 0
            elif mes[8] == max(mes):
                print(y+1,"-",names[8],"is reeded = ", mes[8], "pages")
                mes[8] = 0
            elif mes[9] == max(mes):
                print(y+1,"-",names[9],"is reeded = ", mes[9], "pages")
                mes[9] = 0
        print("-----------------------------------------------------------------------------------------")

