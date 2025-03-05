import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "feet": 3.28084,
        # "inches": 39.3701,
        "kilometers": 0.001,
        "miles": 0.000621371
    }
    
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # No conversion needed

# Streamlit UI
st.title("Unit Converter")

category = st.selectbox("Choose a conversion category:", ["Length", "Temperature"])

if category == "Length":
    value = st.number_input("Enter the value to convert:")
    from_unit = st.selectbox("From unit:", ["meters", "feet", "kilometers", "miles"])
    to_unit = st.selectbox("To unit:", ["meters", "feet", "kilometers", "miles"])
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    value = st.number_input("Enter the temperature to convert:")
    from_unit = st.selectbox("From unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
