# Name = Lloyd Ngaindjo
# Student # = 251301088
# Email = lngindj@uwo.ca
# import os

def getInformation(selectedCountry, TopUni='input.dat', capitals='input.dat'):
    universityList=[]
#list of universities
    countryNames=[]
#list of countries
    continentNames=[]
#list of continents
    rankings_uni = []
#Universities rankings for all the countries listed
    capitals_Continents = []
#capitals of the selected countries
    worldranklist = []
#universities rankings world wide
    availableuniList = []
    nationalRankList=[]
#universities rankings nationally
    universitywithcapital = []
#universities with the capital in the name
    total_Scores = 0
    count = 0
    selectedCountry = selectedCountry.upper()
    with open("output.txt", "w") as O:
        with open("TopUni.csv", "r", encoding='utf8') as universities:
#this function opens the "TopUni" file
            next(universities)
            for line in universities:
                line = line.upper().strip("\n").split(",")
                universityList.append(line[1])
                if line[2] not in countryNames:
                    countryNames.append(line[2])
                    rankings_uni.append(line[8])
                    worldranklist.append(line[0])
                    availableuniList.append(line[1])
                    nationalRankList.append(line[3])

        with open("capitals.csv", "r", encoding='utf8') as capitals:
#this function opens the "TopUni" file
            next(capitals)
            for line in capitals:
                line = line.upper().strip("\n").split(",")
                if line[0] not in capitals_Continents:
                    capitals_Continents.append(line[0])
                    capitals_Continents.append(line[1])
                    capitals_Continents.append(line[5])

        O.write("The total number of universities => {} \n".format(len(universityList)))
#this functions serves to write down the number of universities in the file output using the "O.write" function
        O.write("Available Countries => {}\n".format(countryNames))

        for x in range(len(countryNames)):
            theIndex = capitals_Continents.index(countryNames[x])
            if capitals_Continents[theIndex +2] not in continentNames:
                continentNames.append(capitals_Continents[theIndex + 2])

        allContinent = capitals_Continents[2::3]
        for x in range(len(allContinent)):
            if (allContinent[x]) not in continentNames:
                continentNames.append(allContinent[x])
        O.write("Available Continents => {}\n".format(continentNames))
#this functions serves to write down all the available continents in the file output using the "O.write" function
        capitals_Continents.index(selectedCountry)
        worldrankposition = worldranklist[countryNames.index(selectedCountry)]
        uniName= availableuniList[countryNames.index(selectedCountry)]
        national_rank = nationalRankList[countryNames.index(selectedCountry)]

        O.write("At International Rank => {} the university name is => {}\n".format(worldrankposition, uniName))
#this functions serves to write down name of the university and its international rank in the file output using the "O.write" function
        natRank = ""
        with open('TopUni.csv', 'r', encoding='utf8') as universities:
            next(universities)
            for line in universities:
                line = line.upper().strip("\n").split(",")
                if line[3] == "1" and line[2].upper() == selectedCountry:
                    natRank = line[1]
        O.write("At National Rank => 1 the university name is => {}\n".format(natRank))

        with open('TopUni.csv', 'r', encoding='utf8') as universities:
            next(universities)
            for line in universities:
                line = line.upper().strip("\n").split(",")
                if line[2] == selectedCountry:
                    total_Scores += float(line[8])
                    count += 1

        average_score = (total_Scores/count) #this formula is used to calculate the average score of all the unis within the selected country
        O.write("The average score => {}\n".format(average_score))

        relevantCont = capitals_Continents.index(selectedCountry) + 2
        with open('TopUni.csv', 'r', encoding='utf8') as universities:
            next(universities)
            topCont = []
            for line in universities:
                line = line.upper().strip("\n").split(",")
                currentCont = (capitals_Continents.index(line[2]) + 2)
                if capitals_Continents[currentCont] == capitals_Continents[relevantCont]:
                    topCont.append(line[8])
        topCont = [eval(x) for x in topCont]
        topCont = max(topCont)
        equation = (average_score/topCont) * 100
        O.write("The relative score to the top university in {} is => ({} / {}) x 100% = {}%\n".format(capitals_Continents[relevantCont], average_score, topCont, equation))
#this fucntion contains the formula to find the continent relative score to the top within the continent
        capital = capitals_Continents[capitals_Continents.index(selectedCountry)+1]
        O.write("The capital is => {}\n".format(capital))

        # universityName = capitals_Continents[universityList]

        with open('TopUni.csv', 'r', encoding='utf8') as universities:
            for identical in universities:
                identical = identical.upper().strip("\n").split(",")
                if capital in identical[1]:
                    universitywithcapital.append(identical[1]) #this set of code is used to assemble all universities with the name of the capital in it
            O.write("The universities that contain the capital name => {} \n".format(capital))

            for i in range(len(universitywithcapital)):
                O.write("\t#{} {}\n".format(i+1, universitywithcapital[i]))

        # with open("capitals.csv","r") as capitals:
        #     next(capitals)
        #     for line in capitals:
        #         line = line.upper().strip("\n").split(",")
        #         if line[]

getInformation("japan", "TopUni.csv", "capitals.csv")
