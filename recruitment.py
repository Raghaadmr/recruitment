def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    name = input("What's your name?")
    age = int(input("How old are you?"))
    experience = int(input("How many years of experience do you have?"))
    cv={}
    skills=["Python","C++","javascript","Juggling","Running","Eating"]
    cv['name']=name
    cv['age']=age
    cv['experience']=experience
    cv['skills']=[]
    for index,value in enumerate(skills):
      print(f"{index+1}. {value}")
    skill = input("Choose a skill from above by entering its number: ")
    another = input ("Choose another skill from above by entering its number: ")
    cv['skills'].append(skills[int(skill)-1])
    cv['skills'].append(skills[int(another)-1])
    if (25<int(cv['age'])<40)and(int(cv["experience"])>5)and(skills[5]in cv['skills']):
      print("accepted")
    else:
      print("rejected")
if __name__ == '__main__':
    main()
