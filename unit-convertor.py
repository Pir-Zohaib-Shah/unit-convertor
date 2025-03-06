import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, #1 meter = 0.001 kilometer
        "kilometer_meter": 1000, #1 kilometer = 1000 meters
        "gram_kilogram": 0.001, #1 gram = 0.001 kilogram
        "kilogram_gram": 1000, #1 kilogram = 1000 grams
        "inch_centimeter": 2.54, #1 inch = 2.54 centimeters
        "centimeter_inch": 0.393701, #1 centimeter = 0.393701 inches
        "centimeter_meter": 0.01, #1 centimeter = 0.01 meters
        "meter_centimeter": 100, #1 meter = 100 centimeters
        "feet_meter": 0.3048, #1 feet = 0.3048 meters
        "meter_feet": 3.28084, #1 meter = 3.28084 feet
        "feet_inch": 12, #1 feet = 12 inches
        "inch_feet": 0.0833333, #1 inch = 0.0833333 feet
        "liter_milliliter": 1000, #1 liter = 1000 milliliters
        "milliliter_liter": 0.001, #1 milliliter = 0.001 liters
        "meter_inch": 39.3701, #1 meter = 39.3701 inches
        "inch_meter": 0.0254, #1 inch = 0.0254 meters
        "kilometer_inch": 39370.1, #1 kilometer = 39370.1 inches
        "inch_kilometer": 0.0000254, #1 inch = 0.0000254 kilometers
        "pound_kilogram": 0.453592, #1 pound = 0.453592 kilograms
        "kilogram_pound": 2.20462, #1 kilogram = 2.20462 pounds
        "kilometer_mile": 0.621371, #1 kilometer = 0.621371 miles
    }

    key = f"{unit_from}_{unit_to}" #generate unique key for the conversion based on the units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        ValueError("Conversion not possible")
    
st.title("Unit Convertor")
st.write("The Unit Convertor app by Zohaib Shah")
st.write("")
value = st.number_input("Enter the value you want to convert")
unit_from = st.selectbox("Convert from", ["meter", "kilometer", "gram", "kilogram", "inch", "centimeter", "feet", "liter", "milliliter", "pound"])
unit_to = st.selectbox("Convert to", ["meter", "kilometer", "gram", "kilogram", "inch", "centimeter", "feet", "liter", "milliliter", "pound"])

if st.button("Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    if result: #if the result is not None
        st.write(f"{value} {unit_from} is equal to {result} {unit_to}")
    else:
        st.write("Conversion not possible")