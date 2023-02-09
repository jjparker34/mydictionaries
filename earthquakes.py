'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.


NOTE: No hard-coding allowed except for keys for the dictionaries


1) print out the number of earthquakes


2) iterate through the dictionary and extract the location, magnitude,
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.


3) using the eq_dict dictionary, print out the information as shown below (first three shown):


Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364




Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604




Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628


'''






import json


infile = open('eq_data.json','r')
eq = json.load(infile)


#prints eq count


print('Number of earthquakes: ', eq['metadata']['count'])
print()


eq_dict = {'Earthquakes': []}




#loops through to find mag>6 and then puts them to a temp dictionary then appends to eq_dict


for i in range(0, len(eq['features'])):
   if eq['features'][i]['properties']['mag'] > 6:
      temp_dict = {}
      temp_dict['location'] = eq['features'][i]['properties']['place'],
      temp_dict['magnitude'] = eq['features'][i]['properties']['mag'],
      temp_dict['long'] = eq['features'][i]['geometry']['coordinates'][0],
      temp_dict['lat'] = eq['features'][i]['geometry']['coordinates'][1],


      eq_dict['Earthquakes'].append(temp_dict)
     


     
#prints eq_dict


   #print(eq_dict, '\n')
   


# prints items in eq_dict


for i in range(0, len(eq_dict['Earthquakes'])):
   print('Location: ', eq_dict['Earthquakes'][i]['location'])
   print('Magnitude: ', eq_dict['Earthquakes'][i]['magnitude'])
   print('Longitude: ', eq_dict['Earthquakes'][i]['long'])
   print('Latitude: ', eq_dict['Earthquakes'][i]['lat'])
   print()
     
infile.close()
