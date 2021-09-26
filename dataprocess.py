import seaborn as sns

sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

#load the complete election results, including primary candidates
#but I had premodified this to include both nomination and presidential victories
def load_election_data():
    csv_path = ("colorswithresults.csv")
    return pd.read_csv(csv_path)

#bring in the election data and give it a name so it can be processed
elections = load_election_data()

#first I want to look at how many of each unique color there is. Spoiler alert: there's a LOT of unique colors
# count number per color
countBlue = 0
countRed = 0
countWhite = 0
countOther1 = 0
countOther2 = 0
countOther3 = 0

# count if the campaigns used red, white, AND blue
countRWBYES = 0
countRWBNO = 0

# count successful campaigns
countPresidentWin = 0
countPresidentLoss = 0

# lists of colors in hex by column
# this is for cluster analysis
colorListBlue = []
colorListRed = []
colorListWhite = []
colorListOther1 = []
colorListOther2 = []
colorListOther3 = []

#now the program will iterate through the individual columns of color values to count
for i in range(0, len(elections['redHex'])):

    if elections['redHex'][i] not in colorListRed and isinstance(elections['redHex'][i], str) is True:
        colorListRed.append(elections['redHex'][i])
        countRed += 1

print("Number of Unique Red values :", countRed)

# print("Unique Red Values :", colorListRed)

for i in range(0, len(elections['blueHex'])):

    if elections['blueHex'][i] not in colorListBlue and isinstance(elections['blueHex'][i], str) is True:
        colorListBlue.append(elections['blueHex'][i])
        countBlue += 1

print("Number of Unique Blue values :", countBlue)

# print("Unique Blue Values :", colorListBlue)

for i in range(0, len(elections['whiteHex'])):
    if elections['whiteHex'][i] not in colorListWhite and isinstance(elections['whiteHex'][i], str) is True:
        colorListWhite.append(elections['whiteHex'][i])
        countWhite += 1

print("Number of Unique White values :", countWhite)

# print("Unique White Values :", colorListWhite)

for i in range(0, len(elections['other1Hex'])):
    if elections['other1Hex'][i] not in colorListOther1 and isinstance(elections['other1Hex'][i], str) is True:
        colorListOther1.append(elections['other1Hex'][i])
        countOther1 += 1

print("Number of Unique Other values 1 :", countOther1)

# print("Unique White Values :", colorListOther1)

for i in range(0, len(elections['other2Hex'])):
    if elections['other2Hex'][i] not in colorListOther2 and isinstance(elections['other2Hex'][i], str) is True:
        colorListOther2.append(elections['other2Hex'][i])
        countOther2 += 1

print("Number of Unique Other values 2 :", countOther2)

# print("Unique White Values :", colorListOther2)

for i in range(0, len(elections['other3Hex'])):
    if elections['other3Hex'][i] not in colorListOther3 and isinstance(elections['other3Hex'][i], str) is True:
        colorListOther3.append(elections['other3Hex'][i])
        countOther3 += 1

print("Number of Unique Other values 3 :", countOther3)

# print("Unique White Values :", colorListOther3)

for i in range(0, len(elections['RWB'])):
    if elections['RWB'][i] is 'Y':
        countRWBYES += 1
    else:
        countRWBNO += 1

print("Number of Campaigns using Red White and Blue :", countRWBYES)
print("Number of Campaigns not using only Red White and Blue :", countRWBNO)

for i in range(0, len(elections['presidencyWin'])):
    if elections['presidencyWin'][i] is 'Y':
        countPresidentWin += 1
    else:
        countPresidentLoss += 1

print("Number of Campaigns that won presidency :", countPresidentWin)
print("Number of Campaigns that did not win presidency :", countPresidentLoss)


elections = load_election_data()
# print(elections)

red = elections['redHex']
blue = elections['blueHex']
other1 = elections['other1Hex']
other2 = elections['other2Hex']

# print(red)
redRGB = []
blueRGB = []
other1RGB = []
other2RGB = []

#here I was playing with changing the colors from RGB to Hex and back again for analysis purposes
#to see which was the best choice for analysis
#I ultimately used the hex values
for x in red:
    if isinstance(x, str) == True:
        x = x.replace('#', '')
        x = tuple(int(x[i:i + 2], 16) for i in (0, 2, 4))
        redRGB.append(x)

for x in blue:
    if isinstance(x, str) == True:
        x = x.replace('#', '')
        x = tuple(int(x[i:i + 2], 16) for i in (0, 2, 4))
        blueRGB.append(x)

for x in other1:
    if isinstance(x, str) == True:
        x = x.replace('#', '')
        x = tuple(int(x[i:i + 2], 16) for i in (0, 2, 4))
        other1RGB.append(x)

for x in other2:
    if isinstance(x, str) == True:
        x = x.replace('#', '')
        x = tuple(int(x[i:i + 2], 16) for i in (0, 2, 4))
        other2RGB.append(x)

# print(redRGB)


redRGB = pd.DataFrame(np.array(redRGB).reshape(-1, 3),
                      columns=['R', 'G', 'B'])
blueRGB = pd.DataFrame(np.array(blueRGB).reshape(-1, 3),
                      columns=['R', 'G', 'B'])
other1RGB = pd.DataFrame(np.array(other1RGB).reshape(-1, 3),
                      columns=['R', 'G', 'B'])
other2RGB = pd.DataFrame(np.array(other2RGB).reshape(-1, 3),
                      columns=['R', 'G', 'B'])
kmeans = KMeans(n_clusters=5,
                random_state=0)
# Fit and assign clusters
def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)

#here is the cluster analysis
#which I used to create pie charts
#although, I would prefer in the future to find a better visualization for data of this type

def color_analysis(color_list):
    color_list['Cluster'] = kmeans.fit_predict(color_list)
    palette = kmeans.cluster_centers_
    palette_list = list()
    color_list_rgb = []
    color_list_hex = []
    color_list_count = 0
    values = [20, 20, 20, 20, 20]
    for color in palette:
        palette_list.append(tuple(color))

    for i in palette_list:
        print([i[0].astype(int), i[1].astype(int), i[2].astype(int)])
        color = (i[0].astype(int), i[1].astype(int), i[2].astype(int))
        color_list_rgb.append(color)
        colorhex = rgb_to_hex(i[0].astype(int), i[1].astype(int), i[2].astype(int))
        color_list_hex.append(colorhex)
        color_list_count += 1

    plt.figure(figsize=(12, 8))
    plt.pie(values, labels=color_list_hex, colors=color_list_hex);
    plt.pie
    plt.show();

#then I ran each color analysis to produce piecharts of the top 5 average colors
#among the MANY in the initial data set
color_analysis(redRGB)
color_analysis(blueRGB)
color_analysis(other1RGB)
color_analysis(other2RGB)
