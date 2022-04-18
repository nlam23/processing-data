import csv

pressures = []
biggestNumber = 0
smallestNumber = 0
#pressure_partial has 1825 lines, max pressure of 1004.77, min pressure of 1000.41
with open('pressure_partial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])
            
          if(line_count == 1):
            smallestNumber = float(row[1])

          if(smallestNumber>float(row[1])):
            smallestNumber = float(row[1])
          line_count += 1
    print(f'Processed {line_count} lines.')
print(len(pressures))
print(biggestNumber)
print(smallestNumber)
print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )