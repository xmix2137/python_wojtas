#14.	Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg and height in cm. 
# Then calculate BMI for Peter (81kg, 182cm).

calculate_bmi = lambda weight_kg, height_cm: weight_kg / ((height_cm / 100) ** 2)

weight_peter_kg = 81
height_peter_cm = 182

bmi_peter = calculate_bmi(weight_peter_kg, height_peter_cm)
print(f"The BMI for Peter is: {bmi_peter:.2f}")
