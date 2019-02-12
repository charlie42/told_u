import re
import pandas as pd
df = pd.read_csv('CDO5012767240555.csv', dtype={' YEARMODA':str, ' FRSHTT': str})
#print(df)
#print(df[[TEMP]])
print(df.columns)
df1 = df[[' YEARMODA','   TEMP', ' FRSHTT']]
print(df1)
df_rain = df1[df1[' FRSHTT'].str.contains('.1....', regex=True)]

rain_mean = df_rain['   TEMP'].mean()
print("mean temperature (F) for rainy days " + str(rain_mean))
df_no_rain = df1[~df1[' FRSHTT'].str.contains('.1....', regex=True)]

no_rain_mean = df_no_rain['   TEMP'].mean()
print("mean temperature (F) for not rainy days " + str(no_rain_mean))

df2 = df1
for i in df1[' YEARMODA']:
    #df2[[' YEARMODA'],df2[' YEARMODA'] == i] = i[5:7]
    df2.set_value(df2[' YEARMODA'] == i, ' YEARMODA', i[5:7])

print("__WINTER__")

yeps = 0
nopes = 0

i=12
df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '%d' % i)]
rain_mean = df_jan_rain['   TEMP'].mean()
print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '%d' % i)]
no_rain_mean = df_jan_no_rain['   TEMP'].mean()
print("mean temperature (F) for not rainy days in " + str(i) + " month " + str(int(no_rain_mean)))

if rain_mean - no_rain_mean >= 2:
    print("YEP")
    yeps += 1
else:
    print("NOPE")
    nopes += 1

for i in range(1,3):
    df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '0%d' % i)]
    rain_mean = df_jan_rain['   TEMP'].mean()
    print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

    df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '0%d' % i)]
    no_rain_mean = df_jan_no_rain['   TEMP'].mean()
    print("mean temperature (F) for not rainy days in " + str(i) + " month  " + str(int(no_rain_mean)))

    if rain_mean - no_rain_mean >= 2:
        print ("YEP")
        yeps += 1
    else:
        print("NOPE")
        nopes += 1

print (str(yeps) + " yeps")
print (str(nopes) + " nopes")
if (yeps > nopes):
    print ("Not bullshit")
else:
    print ("Bullshit")

print("__SPRING__")

yeps = 0
nopes = 0

for i in range(3, 6):
    df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '0%d' % i)]
    rain_mean = df_jan_rain['   TEMP'].mean()
    print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

    df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '0%d' % i)]
    no_rain_mean = df_jan_no_rain['   TEMP'].mean()
    print("mean temperature (F) for not rainy days in " + str(i) + " month " + str(int(no_rain_mean)))

    if rain_mean - no_rain_mean >= 2:
        print("YEP")
        yeps += 1
    else:
        print("NOPE")
        nopes += 1

print(str(yeps) + " yeps")
print(str(nopes) + " nopes")
if (yeps > nopes):
    print ("Not bullshit")
else:
    print ("Bullshit")

print("__SUMMER__")

yeps = 0
nopes = 0

for i in range(6, 9):
    df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '0%d' % i)]
    rain_mean = df_jan_rain['   TEMP'].mean()
    print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

    df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '0%d' % i)]
    no_rain_mean = df_jan_no_rain['   TEMP'].mean()
    print("mean temperature (F) for not rainy days in " + str(i) + " month " + str(int(no_rain_mean)))

    if rain_mean - no_rain_mean >= 2:
        print("YEP")
        yeps += 1
    else:
        print("NOPE")
        nopes += 1

print(str(yeps) + " yeps")
print(str(nopes) + " nopes")

print("__FALL__")

yeps = 0
nopes = 0

i=9
df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '0%d' % i)]
rain_mean = df_jan_rain['   TEMP'].mean()
print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '0%d' % i)]
no_rain_mean = df_jan_no_rain['   TEMP'].mean()
print("mean temperature (F) for not rainy days in " + str(i) + " month " + str(int(no_rain_mean)))

if rain_mean - no_rain_mean >= 2:
    print("YEP")
    yeps += 1
else:
    print("NOPE")
    nopes += 1

for i in range(10, 12):
    # print(i)
    # print('0(%d)' % i)
    df_jan_rain = df2[((df2[' FRSHTT'].str.contains('.1....', regex=True)) | (df2[' FRSHTT'].str.contains('..1...', regex=True))) & (df2[' YEARMODA'] == '%d' % i)]
    rain_mean = df_jan_rain['   TEMP'].mean()
    print("mean temperature (F) for rainy days in " + str(i) + " month " + str(int(rain_mean)))

    df_jan_no_rain = df2[(~df2[' FRSHTT'].str.contains('.1....', regex=True)) & (df2[' YEARMODA'] == '%d' % i)]
    no_rain_mean = df_jan_no_rain['   TEMP'].mean()
    print("mean temperature (F) for not rainy days in " + str(i) + " month " + str(int(no_rain_mean)))

    if rain_mean - no_rain_mean >= 2:
        print("YEP")
        yeps += 1
    else:
        print("NOPE")
        nopes += 1

print(str(yeps) + " yeps")
print(str(nopes) + " nopes")
if (yeps > nopes):
    print("Not bullshit")
else:
    print("Bullshit")
