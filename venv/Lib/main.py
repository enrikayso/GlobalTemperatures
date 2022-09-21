import csv
import plotly
import pandas as pd
import plotly.express as px

nation = 'United States'
flat_avg_df = pd.read_csv('venv\TopTenPopCountries.csv')
flat_avg_df.head()

simple_df = flat_avg_df[(flat_avg_df.Country == 'China')]
fig = px.bar(simple_df, x='dt', y='AverageTemperature', color='AverageTemperature')
fig.show()

# print("There are",len(flat_avg_df.Country.unique()), "countries.") #243 countries total
# site_names = flat_avg_df.Country.unique()
# short_df = flat_avg_df[flat_avg_df.Country.isin(site_names[:5])]
# fig = px.bar(short_df, x='dt', y='AverageTemperature', color='AverageTemperature', facet_row='Country')
# #fig.show()
# names_by_obs = list(flat_avg_df.groupby('Country')['AverageTemperature'].count().sort_values(ascending=False).index)
# outputfile = open('TopTenPopulations', 'w')
#     #print(nation)
# outputfile.close()

# infile = "GlobalLandTemperaturesByCountry.csv"
# fields = []
# rows = []

#def readFile(infile):
#    with open(infile, 'r') as csvfile:
#        csvreader = csv.reader(csvfile)
#        fields = next(csvreader)
#        for row in csvreader:
#            rows.append(row)
#        print('Field names are: ' + ', '.join(field for field in fields))
#    print('\nFirst 5 rows are:\n')
#    for row in rows[:5]:
#        # parsing each column of a row
#        for col in row:
#            print("%10s" % col),
#        print('\n')


# def main():
#
#
#     #readFile(infile)
#
#     inputfile = csv.reader(open('GlobalLandTemperaturesByCountry.csv', 'r'))
#     # outputfile = open('placelist.txt', 'w') #nnooooope
#     i = 0
#     previousTemp = 0.0
#     tempChange = 0.0
#     previousCountryAvg = 0.0
#
#     annualWeatherAvg = 0.0
#     countryLifetimeAvg = 0.0
#
#     monthCounter = 0
#     yearCounter = 0
#
#     country = ''
#
#     for row in inputfile:
#
#         if(i > 0):
#
#             if (monthCounter == 12):
#                 annualWeatherAvg = annualWeatherAvg / 12
#
#                 print("ANNUAL WEATHER AVERAGE for", country, ":", "{:.3f}".format(annualWeatherAvg))
#                 print("PREVIOUS YEAR AVERAGE for", country, ":", "{:.3f}".format(previousCountryAvg))
#                 previousCountryAvg = annualWeatherAvg
#                 monthCounter = 0
#                 annualWeatherAvg = 0
#                 yearCounter += 1
#             country = row[3].replace(' ,', ',')
#
#             if(row[1] == ''):
#                 row[1] = 0.0
#                 row[2] = 0.0
#             date = row[0]
#             avgTemp = row[1]
#             avgTemp = float(avgTemp)
#             annualWeatherAvg += avgTemp
#             tempChange = avgTemp - previousTemp
#             previousTemp = avgTemp
#             tempUncertainty = row[2]
#             print("Country:", country, "|| Date:", date, "|| Average Temp:", avgTemp, "|| Uncertainty:", tempUncertainty,
#                   "|| Change in Temp:", "{:.3f}".format(tempChange))
#             #place = row[3].replace(' ,', ',')
#             #print(place)
#             #outputfile.write(place + '\n')
#         i += 1
#         monthCounter += 1
#
#
# main()