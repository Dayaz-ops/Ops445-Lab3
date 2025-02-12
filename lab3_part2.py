def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting
text = return_text_value()

if "Morning" in text:
    print("The function returned a morning greeting!")
