import random
import json
import torch
from model  import NeuralNet
from nltkutils import bag_of_words,tokenize


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json','r') as json_file:
    intents = json.load(json_file)

FILE='data.pth'
data=torch.load(FILE)

input_size=data['input_size']
output_size=data['output_size']
hidden_size=data['hidden_size']
all_words=data['all_words']
tags=data['tags']
model_state=data['model_state']

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name='CityBank Assistant'
print("Let's chat! type 'quit' to exit the chat")

while True:
    sentence=input('You: ')
    if sentence=='quit':
        break

    sentence=tokenize(sentence)
    X=bag_of_words(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X)

    output =model(X)
    _,predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]

    probs=torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]

    print("Predicted tag:", tag)
    #print("Confidence:", prob.item())

    if prob.item()>0.5:
        for i in intents['intents']:
            if tag==i['tags']:
                print(f'{bot_name}: {random.choice(i['responses'])}')
    else:
        print(f'{bot_name}: I do not understand')

