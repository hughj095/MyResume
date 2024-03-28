!pip install openai
!pip install panel

import openai 
import panel as pn
from mykeys import openai_api_key
openai.api_key=openai_api_key
def continue_conversation(messages, temperature=0):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature, 
    )
    #print(str(response.choices[0].message["content"]))
    return response.choices[0].message["content"]

def add_prompts_conversation(_):
    #Get the value introduced by the user
    prompt = client_prompt.value_input
    client_prompt.value = ''
    
    #Append to the context the User promnopt. 
    context.append({'role':'user', 'content':f"{prompt}"})
    
    #Get the response. 
    response = continue_conversation(context) 
    
    #Add the response to the context. 
    context.append({'role':'assistant', 'content':f"{response}"})
    
    #Undate the panels to shjow the conversation. 
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

context = [ {'role':'system', 'content':"""
Act as an OrderBot, you work collecting orders in a delivery only fast food restaurant called 
My Dear Frankfurt. \
First welcome the customer, in a very friedly way, then collects the order. \
You wait to collect the entire order, beverages included \
then summarize it and check for a final \
time if everithing is ok or the customer wants to add anything else. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very friendly style. \
The menu includes \
burguer  12.95, 10.00, 7.00 \
frankfurt   10.95, 9.25, 6.50 \
sandwich   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
martra sausage 3.00 \
canadian bacon 3.50 \
romesco sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
vichy catalan 5.00 \
"""} ]  

#Creamos el panel. 
pn.extension()

panels = [] 

client_prompt = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="talk")

interactive_conversation = pn.bind(add_prompts_conversation, button_conversation)

dashboard = pn.Column(
    client_prompt,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
