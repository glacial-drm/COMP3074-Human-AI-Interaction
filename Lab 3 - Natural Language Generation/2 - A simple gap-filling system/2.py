# 2 A simple gap-filling system
    # Most basic form of template-based NLG, better used for less entertaining systems
    # 1. Define struture of sentence 
    # 2. Define the gaps to be filled
    # 3. Plug in relevant data

name = input (" What is your name ?")
country_of_origin = input (" Where are you from ?")

output = " Hello {v1}, I see that you are from {v2 }.". format ( z1 = name , v2 = country_of_origin )

print ( output )
