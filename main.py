import json
def save_ideas(ideas):
    with open("ideas.json", "w") as file:
        json.dump(ideas, file)

def load_ideas():
    try:
        with open("ideas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def show_ideas(ideas):
    for idea in ideas:
        print(idea)

def add_show(ideas,n):                 
    while len(ideas)<n:
        print('please enter an idea:')
        idea=input().lower().strip()
        if idea=="":
            print('idea can not be empty')
        elif idea in ideas:
            print('idea already exist')
        else:
            ideas.append(idea)

ideas=load_ideas()
valid=False
while not valid:
    try:
        print('enter the number of repeat:')
        n=int(input()) 
        if n<1:
            print('Please enter a positive number.')
        else:
            valid=True  
            if len(ideas)>=n:
                print('Enough ideas')
            else:
                add_show(ideas,n)
                save_ideas(ideas)
            print('total:',len(ideas))

            show_ideas(ideas)

            delete_idea=input('which idea do you want to delet:').lower().strip()     
            if delete_idea in ideas:
                print('idea found')
                ideas.remove(delete_idea)
                save_ideas(ideas)
            else:
                print("idea not found")
    
            print('ideas:')
            show_ideas(ideas)

    except ValueError:
           print('please enter a number: ')
    
