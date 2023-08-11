import streamlit as st
import pickle

#with open('model.pkl', 'rb') as file:
    #model = pickle.load(file)
with open("Car_Price_Prediction_model.pkl",'rb') as file:  
    model=pickle.load(file)

st.title("Car Price Prediction : Input Data")

#Text Field
#Manufacturer
st.subheader("Manufacturer")
Manufacturer = st.radio("Select the Manufacturer of the Car", ['HYUNDAI','TOYOTA', 'MERCEDES-BENZ', 'CHEVROLET', 'FORD', 'HONDA', 'BMW', 'NISSAN', 'VOLKSWAGEN', 'OPEL', 'KIA', 'SSANGYONG', 'MITSUBISHI', 'SUBARU', 'LEXUS', 'AUDI', 'MAZDA', 'FIAT', 'DAEWOO', 'SUZUKI', 'MINI', 'JEEP' ,'VAZ', 'DODGE', 'RENAULT', 'SKODA', 'INFINITI', 'CHRYSLER', 'VOLVO', 'PEUGEOT', 'LAND ROVER', 'BUICK', 'PORSCHE', 'GAZ', 'UAZ', 'DAIHATSU', 'GMC', 'SCION', 'CITROEN', 'JAGUAR', 'ALFA ROMEO', 'ISUZU', 'ROVER', 'ACURA', 'CADILLAC', 'LINCOLN', 'SEAT', 'ZAZ', 'MASERATI', 'SAAB', 'LANCIA', 'HAVAL', 'MERCURY', 'HUMMER', 'PONTIAC', 'SATURN', 'ROLLS-ROYCE','MOSKVICH', 'GREATWALL', 'Else'])
st.write("Manufacturer:", Manufacturer)
if Manufacturer == "HYUNDAI":
    Manufacturer = 2523
elif Manufacturer == 'TOYOTA':
    Manufacturer = 2264
elif Manufacturer == "MERCEDES-BENZ":
    Manufacturer = 800
elif Manufacturer == "CHEVROLET":
    Manufacturer = 772
elif Manufacturer == "FORD":
    Manufacturer = 691
elif Manufacturer == "HONDA":
    Manufacturer = 681
elif Manufacturer == "BMW":
    Manufacturer = 598
elif Manufacturer == "NISSAN":
    Manufacturer = 533
elif Manufacturer == "VOLKSWAGEN":
    Manufacturer = 517
elif Manufacturer == "OPEL":
    Manufacturer = 323
elif Manufacturer == "KIA":
    Manufacturer = 316
elif Manufacturer == "SSANGYONG":
    Manufacturer = 261
elif Manufacturer == "MITSUBISHI":
    Manufacturer = 243
elif Manufacturer == "SUBARU":
    Manufacturer = 217
elif Manufacturer == "LEXUS":
    Manufacturer = 208
elif Manufacturer == "AUDI":
    Manufacturer = 165
elif Manufacturer == "MAZDA":
    Manufacturer = 127
elif Manufacturer == "FLAT":
    Manufacturer = 77
elif Manufacturer == "DAEWOO":
    Manufacturer = 77
elif Manufacturer == "SUZUKI":
    Manufacturer = 58
elif Manufacturer == "MINI":
    Manufacturer = 45
elif Manufacturer == "JEEP":
    Manufacturer = 42
elif Manufacturer == "VAZ":
    Manufacturer = 42
elif Manufacturer == "DODGE":
    Manufacturer = 37
elif Manufacturer == "RENAULT":
    Manufacturer = 33
elif Manufacturer == "SKODA":
    Manufacturer = 17
elif Manufacturer == "INFINITI":
    Manufacturer = 15
elif Manufacturer == "CHRYSLER":
    Manufacturer = 15
elif Manufacturer == "VOLVO":
    Manufacturer = 13
elif Manufacturer == "PEUGEOT":
    Manufacturer = 12
elif Manufacturer == "LAND ROVER":
    Manufacturer = 11
elif Manufacturer == "BUICK":
    Manufacturer = 11
elif Manufacturer == "PORSCHE":
    Manufacturer = 9
elif Manufacturer == "GAZ":
    Manufacturer = 8
elif Manufacturer == "UAZ":
    Manufacturer = 8
elif Manufacturer == "DAIHATSU":
    Manufacturer = 7
elif Manufacturer == "GMC":
    Manufacturer = 6
elif Manufacturer == "SCION":
    Manufacturer = 6
elif Manufacturer == "CITROEN":
    Manufacturer = 5
elif Manufacturer == "JAGUAR":
    Manufacturer = 5
elif Manufacturer == "ALFA ROMEO":
    Manufacturer = 4
elif Manufacturer == "ISUZU":
    Manufacturer = 3
elif Manufacturer == "ROVER":
    Manufacturer = 3
elif Manufacturer == "ACURA":
    Manufacturer = 3
elif Manufacturer == "CADILLAC":
    Manufacturer = 3
elif Manufacturer == "LINCOLN":
    Manufacturer = 2
elif Manufacturer == "SEAT":
    Manufacturer = 2
elif Manufacturer == "ZAZ":
    Manufacturer = 2
elif Manufacturer == "MASERATI":
    Manufacturer = 2
elif Manufacturer == "SAAB":
    Manufacturer = 2
elif Manufacturer == "LANCIA":
    Manufacturer = 1
elif Manufacturer == "HAVAL":
    Manufacturer = 1
elif Manufacturer == "MERCURY":
    Manufacturer = 1
elif Manufacturer == "HAMMER":
    Manufacturer = 1
elif Manufacturer == "PONTIAC":
    Manufacturer = 1
elif Manufacturer == "SATURN":
    Manufacturer = 1
elif Manufacturer == "ROOLS-ROYCE":
    Manufacturer = 1
elif Manufacturer == "MOSKVICH":
    Manufacturer = 1
elif Manufacturer == "GREATWALL":
    Manufacturer = 1
else:
    Manufacturer = 1

#Category
st.subheader("Category")
Category = st.radio("Select the Category of the Car", ['Hatchback', 'Jeep', 'Sedan', 'Microbus', 'Coupe', 'Minivan', 'Universal', 'Goods wagon', 'Cabriolet', 'Limousine', 'Pickup', 'Else'])
st.write("Category:", Category)
if Category == "Hatchback":
    Category = 2134
elif Category == "Jeep":
    Category = 2548
elif Category == "Sedan":
    Category = 5814
elif Category == "Microbus":
    Category = 193
elif Category == "Coupe":
    Category = 298
elif Category == "Minivan":
    Category = 448
elif Category == "Universal":
    Category = 175
elif Category == "Goods wagon":
    Category = 178
elif Category == "Cabriolet":
    Category = 17
elif Category == "Limousine":
    Category = 6
elif Category == "Pickup":
    Category = 22
else:
    Category = 1

#Production_Year
st.subheader("Prod_Year")
Prod_year = st.text_input("Enter the production year")
st.write("Prod_year :", Prod_year)
if Prod_year == (1980 or 1977 or 1964 or 1953 or 1939):
    Prod_yearrod_year = 2
elif Prod_year == (1985 or 1983):
    Prod_year = 3
elif Prod_year == (1987 or 1986 or 1984):
    Prod_year = 4
elif Prod_year == 1989:
    Prod_year = 5
elif Prod_year == (2020 or 1991):
    Prod_Year = 7
elif Prod_year == 1988:
    Prod_year = 10
elif Prod_year == 1990:
    Prod_year = 12
elif Prod_year == 1993:
    Prod_year = 16
elif Prod_year == 1992:
    Prod_year = 26
elif Prod_year == 1994:
    Prod_year = 35
elif Prod_year == 2019:
    Prod_year = 77
elif Prod_year == 1995:
    Prod_year = 81
elif Prod_year == 1996:
    Prod_year = 87
elif Prod_year == 1997:
    Prod_year = 129
elif Prod_year == 2018:
    Prod_year = 140
elif Prod_year == 1999:
    Prod_year = 172
elif Prod_year == 1998:
    Prod_year = 183
elif Prod_year == 2001:
    Prod_year = 205
elif Prod_year == 2000:
    Prod_year = 229
elif Prod_year == 2006:
    Prod_year = 234
elif Prod_year == 2017:
    Prod_year = 242
elif Prod_year == 2002:
    Prod_year = 254
elif Prod_year == 2007:
    Prod_year = 259
elif Prod_year == 2004:
    Prod_year = 281
elif Prod_year == 2003:
    Prod_year = 296
elif Prod_year == 2009:
    Prod_year = 303
elif Prod_year == 2005:
    Prod_year = 314
elif Prod_year == 2008:
    Prod_year = 361
elif Prod_year == 2016:
    Prod_year = 689
elif Prod_year == 2010:
    Prod_year = 837
elif Prod_year == 2015:
    Prod_year = 848
elif Prod_year == 2011:
    Prod_year = 1073
elif Prod_year == 2014:
    Prod_year = 1188
elif Prod_year == 2013:
    Prod_year = 1566
elif Prod_year == 2012:
    Prod_year = 1633
else:
    Prod_year = 1

#Levy
st.subheader("Levy (Enter the value in Float)")
Levy = st.text_input("Enter Levy")
st.write("Levy :", Levy)

#Mileage(km)
st.subheader("Mileage(km) (Enter the value in Float)")
Mileage = st.text_input("Enter Mileage(km)")
st.write("Mileage(km) :", Mileage)

#Engine_Volume
st.subheader("Engine_Volume (Enter the value in Float)")
Engine_Volume = st.text_input("Enter Engine volume")
st.write("Engine_Volume :", Engine_Volume)

#Engine_type
st.subheader("Engine_Type")
Engine_Type = st.radio("Select Whether the Engine is Turbo type or Not", ["Yes", "No"])
st.write("Engine_Type:", Engine_Type)
if Engine_Type == "Yes":
    Engine_Type = 1302
elif Engine_Type == "No":
    Engine_Type = 10531

#Fuel_type
st.subheader("Fuel_type")
Fuel_type = st.radio("Select the Fuel Type", ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen'])
st.write("Fuel_Type:", Fuel_type)
if Fuel_type == "Hybrid":
    Fuel_type = 2077
elif Fuel_type == "Petrol":
    Fuel_type = 6576
elif Fuel_type == "Diesel":
    Fuel_type = 2208
elif Fuel_type == "CNG":
    Fuel_type = 399
elif Fuel_type == "Plug-in Hybrid":
    Fuel_type = 66
elif Fuel_type == "LPG":
    Fuel_type = 506
elif Fuel_type == "Hydrogen":
    Fuel_Type = 1

#Wheel
st.subheader("Wheel")
Wheel = st.radio("Select the Wheel type", ['Left wheel', 'Right-hand drive'])
st.write("Wheel:", Wheel)
if Wheel == "Left wheel":
    Wheel = 10685
elif Wheel == "Right-hand drive":
    Wheel = 1148

#Airbags
st.subheader("Airbags (Enter the value in range of 0-16)")
Airbags = st.text_input("Enter the No.of Airbags")
st.write("Airbags :", Airbags)
if Airbags == 0:
    Airbag = 1391
elif Airbags == 1:
    Airbags = 61
elif Airbags == 2:
    Airbags = 786
elif Airbags == 3:
    Airbags = 30
elif Airbags == 4:
    Airbags = 3853
elif Airbags == 5:
    Airbags = 85
elif Airbags == 6:
    Airbags = 1045
elif Airbags == 7:
    Airbags = 67
elif Airbags == 8:
    Airbags = 1246
elif Airbags == 9:
    Airbags = 46
elif Airbags == 10:
    Airbags = 602
elif Airbags == 11:
    Airbags = 20
elif Airbags == 12:
    Airbags = 2525
elif Airbags == 13:
    Airbags = 2
elif Airbags == 14:
    Airbags = 12
elif Airbags == 15:
    Airbags = 5
elif Airbags == 16:
    Airbags = 57

#Gear_box_type
st.subheader("Gear_box_type")
Gear_box_type = st.radio("Select the Gear box type", ['Automatic', 'Tiptronic', 'Manual','Variator', 'Else'])
st.write("Gear_box_type:", Gear_box_type)
if Gear_box_type == "Automatic":
    Gear_box_type = 7718
elif Gear_box_type == "Tiptronic":
    Gear_box_type = 2056
elif Gear_box_type == "Manual":
    Gear_box_type = 1469
elif Gear_box_type == "Variator":
    Gear_type_box = 590
else:
    Gear_type_box = 1

# Button
#st.subheader("Button Example")
if st.button("Predict Price"):
    st.write("Price Predicted!")
    yhat_test = model.predict([[Manufacturer,Category,Prod_year,Levy,Mileage,Engine_Volume,Engine_Type,Fuel_type,Wheel,Airbags,Gear_box_type]])
    st.write("Estimated Car Price is $",yhat_test)
# Display Messages
#st.success("Success message")
#st.info("Info message")
#st.warning("Warning message")
#st.error("Error message")