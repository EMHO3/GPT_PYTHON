from openai import OpenAI
import pdb

client = OpenAI(api_key="ponga su API-key de openai aca",)


while True:
    a=input("ingrese su pregunta") 
        

    if a=="exit":
        break
    else:
        
        response=client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role":"user","content":a}] ,
           
            max_tokens=100
            )
        print(response.choices[0].message.content)
        