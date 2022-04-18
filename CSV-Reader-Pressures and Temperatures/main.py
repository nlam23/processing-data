import csv
#combo of both
temperatures = []
pressures = []
biggestTemp = 0
smallestTemp = 0
biggestPressure = 0
smallestPressure = 0

with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestPressure = float(row[1])

          #print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestPressure<float(row[1])):
            biggestPressure = float(row[1])
            
          if(line_count == 1):
            smallestPressure = float(row[1])

          if(smallestPressure>float(row[1])):
            smallestPressure = float(row[1])
          line_count += 1
    print(f'Processed {line_count} lines.')
print(len(pressures))
print(biggestPressure)
print(smallestPressure)
print(f'max pressure is {biggestPressure}' )
print(f'min pressure is {smallestPressure}' )

with open('temperature_full.csv') as csv_file:
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
          temperatures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestTemp<float(row[1])):
            biggestTemp = float(row[1])
            
          if(line_count == 1):
            smallestTemp = float(row[1])

          if(smallestTemp>float(row[1])):
            smallestTemp = float(row[1])
          line_count += 1
    print(f'Processed {line_count} lines.')
print(len(temperatures))
print(biggestTemp)
print(smallestTemp)
print(f'max temperature is {biggestTemp}' )
print(f'min temperature is {smallestTemp}' )