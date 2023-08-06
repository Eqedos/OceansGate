import time
import sys
import winsound
import os
import random

class Player():
    def __init__(self,name,c1=0,c2=0,c3=0,c4=0,c5=0,items=["Tantrums","Guilt Trip", "Unleash Chaos"]):
        self.name=name
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.c4=c4
        self.c5=c5
        self.items=items
        self.hp=100

class Boss():
    def __init__(self, fighter, name="Gaurav", health=100):
        self.name = name
        self.health = health
        self.fighter = fighter
        self.attacks = [
            "Make me a sandwich. NOW.",
            "Do you really think I'd let you get away from me?",
            "**MENTAL ABUSE**",
            "**Physical Abuse**",
            "{} come here, OR ELSE I WILL MAKE SURE YOU ARE DISOWNED".format(fighter.name),
            "Say something I'm giving up on you",
            "OUR AGE DIFFERENCE? IT DOESN'T MATTER.",
            "WHERE. IS. MY. DOWRY?",
            "I WILL NOT LET YOU OUT OF MY SIGHT",
            "YOU ARE MINE",
            "DIE OR DONT SAY BYE",
            "SLAY? I'M GONNA SLAY YOU WITH THIS POCKET KNIFE."
        ]
        self.dmg = {
            "Make me a sandwich. NOW.": 5,
            "Do you really think I'd let you get away from me?": 10,
            "**MENTAL ABUSE**": 15,
            "**Physical Abuse**": 20,
            "{} come here, OR ELSE I WILL MAKE SURE YOU ARE DISOWNED".format(fighter.name): 25,
            "Say something I'm giving up on you": 12,
            "OUR AGE DIFFERENCE? IT DOESN'T MATTER.": 9,
            "WHERE. IS. MY. DOWRY?":25,
            "I WILL NOT LET YOU OUT OF MY SIGHT": 12,
            "YOU ARE MINE":10,
            "DIE OR DONT SAY BYE":13,
            "SLAY? I'M GONNA SLAY YOU WITH THIS POCKET KNIFE.":4
        }


def print_slow(str,pause=0.02):
    os.system('cls')
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(pause)
    print("")
    print("\n \n \n \n")
    p=input("Press enter to continue")

def print_slow2(str,pause=0.02):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(pause)
    print("")
def main():
    os.system('cls')
    winsound.PlaySound("hopes.wav",winsound.SND_ASYNC)
    global PlayerObj
    print_slow("Welcome to Ocean's Gate! What would you like to name your character? ")
    x=str(input("Name:"))
    PlayerObj=Player(x)
    z=str(input("Enter any letter to begin."))
    acad()

def acad():
    global spaces
    print_slow("You are {}, an Indian Girl born in a remote village in Bihar, India".format(PlayerObj.name))
    print_slow("You have enjoyed a pretty peaceful life so far, but an inevitable future lies ahead.")
    print_slow("You are now a student")
    print_slow("As an ambitious child, you wish to take up extracurricular activies, and nervously go up to your parents.")
    print_slow("Your parents say no.")
    spaces="            "
    os.system('cls')
    print_slow("What do you wish to do?")
    print('\n\n\n\n\n\n\n\n')
    print(spaces+"A) Try to convince your parents about your dreams and goals")
    print(spaces+"B) Give up joining extracurricular activities and focus on studies")
    print(spaces+"C) Secretly join extracurricular activities while studying")
    ans=str(input("What do you choose? (Please enter your answer as A, B or C)"))
    newdict={"a":25,"b":20,"c":15}
    
    PlayerObj.c1+=newdict[ans.lower()]
    ans=ans.lower()
    if ans=="c":
        print_slow("Good job! You can now start to pursue your dreams.")    
    print_slow("You have an important exam coming up, but your parents want you to attend a family gathering on the day before.")
    print_slow("You are feeling conflicted as you know the exam is crucial for your future.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Attend the family gathering and study afterward, risking lower exam performance and failing to manage your condition.")
    print(spaces + "B) Politely explain the importance of the exam to your parents and request to study instead.")
    print(spaces + "C) Sneak in study time during the gathering so you will not join the conversation between family a lot.")
    ans = str(input("What do you choose? (Please enter your answer as A, B or C)"))
    new_dict = {"a": 10, "b": 25, "c": 20}
    PlayerObj.c1 += new_dict[ans.lower()]
    ans=ans.lower()
    if ans == "b":
        print_slow("Hey Mom/Dad, can we talk?")
        print_slow("Sure, what's up?")
        print_slow("Well, you know how important my studies are, right?")
        print_slow("Absolutely, we've always emphasized that.")
        print_slow("With exams coming up, I really think I could do better if I stayed home to study for a bit. Would that be okay?")
        print_slow("I understand.")
        print_slow("Well done! You managed to communicate the importance of your exam to your parents and can now focus on studying.")
    elif ans == "c":
        print_slow("Guess I just have to study through all this noise....")
        print_slow("Great job! You found a way to study during the gathering without offending anyone.")
    else:
        print_slow("I'll just go for that now & maybe afterwards I'll be able to find time to study...")
        print_slow("You attended the family gathering, but it was difficult to focus on studying afterward, impacting your exam preparation.")
    print_slow("You have a strong aspiration to pursue higher education and work towards your career goals.")
    print_slow("However, your parents are unsupportive and believe that higher education is unnecessary for a girl.")
    print_slow("They ask you to drop out of school and focus on housekeeping.")
    spaces = "            "
    os.system('cls')
    print_slow("What do you wish to do?")
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Convince your parents that you can learn housekeeping while continuing your studies.")
    print(spaces + "B) Confront your parents, argue about your life, and ignore their beliefs while studying hard.")
    print(spaces + "C) Give up on your dreams of education, drop out of school, and focus on housekeeping while waiting for arranged marriage.")
    print(spaces + "D) Talk to your teacher and ask for help to persuade your parents.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, C, or D)"))
    new_dict = {"a": 10, "b": 25, "c": 5, "d": 20}
    
    PlayerObj.c1 += new_dict[ans.lower()]
    ans=ans.lower()
    if ans == "b":
        print_slow("Mum, Dad, this is my life. And I don't care about what you want for me but this is my life and I will decide for myself!")
        print_slow("Well done! You stood up for your dreams and committed to studying hard despite your parents' beliefs.")
    elif ans == "d":
        print_slow("The following day, you look for your teacher and sought her help on how you can persuade your parents.")
        print_slow("Great decision! Your teacher's support will help you in convincing your parents about the importance of education.")
    elif ans == "a":
        print_slow("You gave it more thought and came up with a reasonable argument. The next day, you asked to speak to your parents.")
        print_slow("You managed to find a middle ground and convinced your parents to let you pursue education alongside learning housekeeping.")
    else:
        print_slow("You gave it some more thought, but you doubt it would impact anything.")
        print_slow("Sadly, you dropped out of school and focused on housekeeping, giving up on your dreams of education.")
    print_slow("It's time to choose your elective course, but your parents don't let you choose what you want.")
    print_slow("Instead, they insist on you selecting a course that is popular among arranged marriage conditions.")
    print_slow("You are torn between following your passion and pleasing your parents.")
    spaces = "            "
    os.system('cls')
    print_slow("What do you wish to do?")
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Engage in an open and respectful discussion with your parents, explaining the value and relevance of the elective course to your future goals.")
    print(spaces + "B) Agree to take the preferred course and give up on your goal.")
    print(spaces + "C) Secretly enroll in the elective course that you want to take.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 20, "b": 15, "c": 25}
    ans=ans.lower()
    PlayerObj.c1 += new_dict[ans.lower()]
    if ans == "a":
        print_slow("You considered the electives you want to take and came up with an explanation for your parents. The next day, you looked for them.")
        print_slow("Well done! You chose to communicate openly with your parents and explain the importance of the elective course for your future goals.")
    elif ans == "c":
        print_slow("It was difficult, but...")
        print_slow("Great job! You took a brave step and secretly enrolled in the elective course that you want to take.")
    else:
        print_slow("why do I have to do this.... it's not what I wanted...")
        print_slow("Regardless, you agreed to take the preferred course, but it left you feeling unsatisfied and giving up on your passion.")
    social()

def social():
    print_slow("You've planned a girls' day with your friends, but your parents don't allow you to hang out with friends outside of school hours.")
    print_slow("This makes it challenging to maintain friendships and spend quality time with them.")
    spaces = "            "
    os.system('cls')
    print_slow("What do you wish to do?")
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Follow your parents' rules strictly and limit social interactions to school hours only.")
    print(spaces + "B) Secretly communicate with your friends through messaging apps or social media to keep the friendships alive.")
    print(spaces + "C) Confront your parents respectfully and try to explain the importance of friendships in your life.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 10, "b": 15, "c": 25}
    
    PlayerObj.c2 += new_dict[ans.lower()]
    ans=ans.lower
    if ans == "b":
        print_slow("You found a way to stay connected with your friends despite the restrictions, keeping your friendships alive.")
    elif ans == "c":
        print_slow("Well done! By respectfully discussing the importance of friendships, you managed to convince your parents to reconsider their rules.")
    else:
        print_slow("You followed your parents' rules strictly, but it left you feeling limited in your social interactions and friendship opportunities.")

    print_slow("You love using social media platforms to connect with friends and express yourself, but your parents closely monitor your online activity and restrict your access to such platforms.")
    print_slow("This makes it challenging to stay in touch with friends and be a part of online communities.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Comply with your parents' restrictions and avoid using social media altogether.")
    print(spaces + "B) Create a private and anonymous social media account to connect with friends and express yourself freely.")
    print(spaces + "C) Discuss the benefits of responsible social media usage with your parents and ask for more freedom in this regard.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 5, "b": 15, "c": 25}
    
    PlayerObj.c2 += new_dict[ans.lower()]
    ans=ans.lower
    if ans == "b":
        print_slow("You decided to create a private and anonymous social media account to maintain your connections and express yourself freely.")
        print_slow("While it provided some freedom, be cautious as it might breach your parents' trust if they find out.")
    elif ans == "c":
        print_slow("Congratulations! You had a respectful discussion with your parents about responsible social media usage.")
        print_slow("They understood your point of view and allowed you more freedom to use social media responsibly.")
    else:
        print_slow("You chose to comply with your parents' restrictions and avoid using social media.")
        print_slow("While it keeps you in line with their rules, it may leave you feeling disconnected from your friends and online communities.")
    print_slow("Your school is organizing a mixed-gender event, and you are excited to attend and have a fun experience.")
    print_slow("However, your parents are strongly against your participation in such events.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Respect your parents' wishes and avoid attending the event, feeling disappointed about missing the fun experience.")
    print(spaces + "B) Attend the event against your parents' wishes, seeking support from understanding friends or cousins to accompany you.")
    print(spaces + "C) Convince your parents by explaining the event's significance and ensuring them of your responsible behavior during the occasion.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 10, "b": 15, "c": 25}
    ans=ans.lower()
    PlayerObj.c2 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to attend the mixed-gender event despite your parents' objections.")
        print_slow("You sought support from understanding friends or cousins to accompany you, making the experience enjoyable.")
        print_slow("While it may lead to disagreements with your parents, you valued the opportunity to have fun with your peers.")
    elif ans == "c":
        print_slow("Congratulations! You chose to have a respectful conversation with your parents.")
        print_slow("You explained the significance of the event and assured them of your responsible behavior.")
        print_slow("Your parents reconsidered their objections and allowed you to attend the event.")
    else:
        print_slow("You decided to respect your parents' wishes and avoid attending the mixed-gender event.")
        print_slow("While you felt disappointed about missing the fun experience, you valued your parents' trust and understanding.")
    print_slow("You find yourself developing feelings for someone outside of your cultural or religious background.")
    print_slow("However, your parents strictly discourage any romantic involvement with such individuals.")
    spaces = "            "
    os.system('cls')
    print_slow("What do you wish to do?")
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Suppress your feelings and avoid any romantic involvement to adhere to your parents' expectations.")
    print(spaces + "B) Enter into a secret relationship, keeping it hidden from your family and risking potential heartache if discovered.")
    print(spaces + "C) Initiate an open and honest conversation with your parents about your feelings, expressing your desire to find a balance between your personal happiness and cultural values.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 5, "b": 15, "c": 25}
    ans=ans.lower()
    PlayerObj.c2 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to enter into a secret relationship with the person you have feelings for.")
        print_slow("While it may bring happiness, be cautious as it carries the risk of heartache if discovered.")
    elif ans == "c":
        print_slow("Congratulations! You chose to have an open and honest conversation with your parents.")
        print_slow("You expressed your feelings and desire to find a balance between personal happiness and cultural values.")
        print_slow("This conversation allowed you and your parents to understand each other better.")
    else:
        print_slow("You decided to suppress your feelings to adhere to your parents' expectations.")
        print_slow("While you may maintain harmony in the family, it may also leave you feeling unfulfilled.")
    career()

def career():
    print_slow("Your school is organizing an art fair, and you are excited to participate and showcase your creativity.")
    print_slow("However, your parents believe that it is a waste of time and want you to prioritize household responsibilities.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Sacrifice sleep and personal time to prepare for the fair without neglecting household chores and duties.")
    print(spaces + "B) Prioritize household responsibilities over the art fair to avoid stress and pressure.")
    print(spaces + "C) Convince your friends to work on the project for the fair together to split the workload.")
    print(spaces + "D) Sign up for the fair, focus on the project, and neglect household duties.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, C, or D)"))
    new_dict = {"a": 15, "b": 10, "c": 20, "d": 30}
    ans=ans.lower()
    PlayerObj.c3 += new_dict[ans.lower()]
    if ans == "a":
        print_slow("You decided to sacrifice sleep and personal time to prepare for the art fair.")
        print_slow("While managing household chores and duties, your dedication to both aspects of life shows your responsibility.")
    elif ans == "c":
        print_slow("Congratulations! You convinced your friends to work on the project together.")
        print_slow("By splitting the workload, you can manage your responsibilities and participate in the art fair.")
    elif ans == "d":
        print_slow("You signed up for the fair and focused on the project, neglecting household duties.")
        print_slow("While you are passionate about the fair, your parents may feel disappointed by the neglect of responsibilities.")
    else:
        print_slow("You decided to prioritize household responsibilities over the art fair to avoid stress and pressure.")
        print_slow("While you maintain balance and harmony at home, you might feel a bit of regret for missing the art fair.")
    print_slow("You have created an art piece to submit for a well-known art exhibition.")
    print_slow("However, some members of the conservative community find it controversial and disrespectful to cultural norms.")
    print_slow("You fear your parents' disapproval and the judgment from the community.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Decide not to join the art exhibition to avoid potential controversy.")
    print(spaces + "B) Submit your artwork anonymously to get a sense of its reception without revealing your identity.")
    print(spaces + "C) Gather courage and openly participate in the art exhibition, standing by your artistic expression.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 0, "b": 15, "c": 25}
    ans=ans.lower()
    PlayerObj.c3 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to submit your artwork anonymously to gauge its reception.")
        print_slow("This way, you can still participate in the exhibition while keeping your identity hidden.")
    elif ans == "c":
        print_slow("Congratulations! You gathered the courage to openly participate in the art exhibition.")
        print_slow("You stood by your artistic expression despite potential controversies and judgments.")
    else:
        print_slow("You decided not to join the art exhibition to avoid potential controversy.")
        print_slow("While it keeps you away from judgment, it may also leave you feeling regretful about not showcasing your art.")
    print_slow("A scholarship is being offered to exceptional students with artistic flair in nearby cities.")
    print_slow("However, your parents are even more against the idea of sending you away for education.")
    print_slow("You are torn between your dream of applying for the scholarship and appeasing your parents to maintain family harmony.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Abandon your dream of applying for the scholarship to appease your parents and maintain family harmony.")
    print(spaces + "B) Apply for the scholarship secretly in hopes that you get it and your parents might change their minds.")
    print(spaces + "C) Seek support from your teacher to help convince your parents to support your educational and career aspirations.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 5, "b": 15, "c": 20}
    ans=ans.lower()
    PlayerObj.c3 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to apply for the scholarship secretly, hoping that you get it.")
        print_slow("You believe that your success might change your parents' minds about sending you away for education.")
    elif ans == "c":
        print_slow("Congratulations! You sought support from your teacher to help convince your parents.")
        print_slow("Your teacher's guidance and encouragement play a crucial role in bridging the gap between you and your parents.")
    else:
        print_slow("You decided to abandon your dream of applying for the scholarship.")
        print_slow("While it maintains family harmony, it may also leave you feeling unfulfilled about missing a great opportunity.")
    mar()

def mar():
    print_slow("Your family informs you about the arranged marriage proposal.")
    print_slow("They express their excitement and expectations, but you feel overwhelmed and uncertain about this significant life decision.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Smile and accept your family's announcement.")
    print(spaces + "B) Stay quiet and contemplative, not expressing your feelings right away.")
    print(spaces + "C) Burst into tears, showing visible signs of distress.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 10, "b": 15, "c": 5}
    ans=ans.lower()
    PlayerObj.c4 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to stay quiet and contemplative, not expressing your feelings right away.")
        print_slow("You are trying to process the information and understand your emotions before reacting.")
    elif ans == "c":
        print_slow("You decided to burst into tears, showing visible signs of distress.")
        print_slow("The weight of the decision and the overwhelming emotions took over, making your feelings evident.")
    else:
        print_slow("You decided to smile and accept your family's announcement.")
        print_slow("While you may feel uncertain inside, you choose not to reveal your reservations to maintain family harmony.")
    print_slow("At first, you resist the idea of an arranged marriage and express your concerns to your family.")
    print_slow("This leads to emotional conversations and potential conflicts.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Engage in a calm and diplomatic discussion with your family, expressing your concerns respectfully.")
    print(spaces + "B) Raise your voice and become visibly upset during the conversation.")
    print(spaces + "C) Choose to remain silent during the discussion, showing your resistance through non-verbal cues.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 20, "b": 5, "c": 10}
    ans=ans.lower()
    PlayerObj.c4 += new_dict[ans.lower()]
    if ans == "a":
        print_slow("You decided to engage in a calm and diplomatic discussion with your family.")
        print_slow("You express your concerns respectfully, trying to make them understand your perspective.")
    elif ans == "b":
        print_slow("You decided to raise your voice and become visibly upset during the conversation.")
        print_slow("Your emotions get the better of you, making the conversation tense and emotionally charged.")
    else:
        print_slow("You decided to remain silent during the discussion, showing your resistance through non-verbal cues.")
        print_slow("By staying silent, you make it clear that you are not in agreement with the proposal.")
    print_slow("You reach a crucial point where you must make a decision that will shape your life.")
    print_slow("Your choices will determine if you choose to assert your autonomy or succumb to external pressures.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Agree to the arranged marriage, putting aside your own desires for family harmony.")
    print(spaces + "B) Stand up for your autonomy and express your decision not to go through with the arranged marriage.")
    print(spaces + "C) Choose to delay the decision and continue exploring your options.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 10, "b": 25, "c": 15}
    ans=ans.lower()
    PlayerObj.c4 += new_dict[ans.lower()]
    if ans == "b":
        print_slow("You decided to stand up for your autonomy and express your decision not to go through with the arranged marriage.")
        print_slow("With courage and determination, you choose to follow your heart and make a bold decision for yourself.")
    elif ans == "c":
        print_slow("You decided to choose to delay the decision and continue exploring your options.")
        print_slow("Taking more time to understand your feelings and the situation allows you to make a well-informed decision later.")
    else:
        print_slow("You decided to agree to the arranged marriage, putting aside your own desires for family harmony.")
        print_slow("While this decision might bring short-term peace, it is essential to consider its long-term impact on your happiness.")
    bossbat()

def bossbat():
    global BossObj
    BossObj=Boss(PlayerObj)
    batcheck()


def batcheck():
    if (PlayerObj.hp<=0):
        print_slow("You have lost the fight")
        reb()
    if(BossObj.health<=0):
        print_slow("Congratulations, you have won the fight with {} HP remaining.".format(PlayerObj.hp))
        PlayerObj.c4+=PlayerObj.hp
        reb()
    else:
        batseq()

def batseq():
    print_slow("You have {} health remaining!".format(PlayerObj.hp))
    print_slow("Gaurav has {} health remaining!".format(BossObj.health))
    bossattacks()
    print_slow("What would you like to do?")
    print_slow2("A) Attack Him")
    print_slow2("B) Reaffirm Self")
    print_slow2("C) Check Inventory")
    print_slow2("D) Say something hurtful and take a risk")
    x=str(input("What do you do?"))
    x=x.lower()
    if x.lower()=="a":
        playerattack()
    if x.lower()=="b":
        print_slow("You have gained 13 hp")
        PlayerObj.hp+=13
    if x.lower()=="c":
        inventoryattack()
    if x.lower()=="d":
        k=random.randint(1,2)
        if k==1:
            print_slow("You hurt yourself in confusion, took some damage.")
            PlayerObj.hp-=random.randint(5,10)
        if k==2:
            print_slow("It worked!")
            BossObj.health-=random.randint(15,20)
    batcheck()
def inventoryattack():
    for i in range(len(PlayerObj.items)):
        print_slow2(str(i)+PlayerObj.items[i])
    z=int(input("Which item do you pick?"))
    k=PlayerObj.items[z]
    if k=="Tantrums":
        print_slow("You threw tantrums and bought yourself some time and full hp!")
        PlayerObj.hp=100
    if k=="Guilt Trip":
        print_slow("You wasted your turn....he wasn't affected.")
    if k=="Unleash Chaos":
        print_slow("You Scream. Very Loud.",0.2)
        print_slow("It does 30 damage.")
        BossObj.health-=30

def bossattacks():
    x=random.choice(BossObj.attacks)
    print_slow(x)
    print("Your player was hurt by the statement and takes {} damage".format(BossObj.dmg[x]))
    PlayerObj.hp-=BossObj.dmg[x]

def playerattack():
    player_responses = [
        "You can't control my life!",
        "I won't be silenced anymore!",
        "I am stronger than you think!",
        "I won't let you dictate my future!",
        "I deserve to make my own choices!",
        "I won't back down!",
        "My dreams matter, and I will pursue them!",
        "I am more than just a pawn in your plans!",
        "I won't let fear guide me!",
        "I am in charge of my destiny!",
        "I won't let you define who I am!",
        "I will break free from these chains!",
        "I have the right to be happy on my terms!",
        "I am not afraid of your threats!",
        "I won't compromise my happiness for your expectations!"
    ]
    choice=random.choice(player_responses)
    print_slow(choice)
    x=random.randint(5,15)
    print_slow("You did {} damage".format(x))
    BossObj.health-=x


def reb():
    print_slow("Your friends invite you to a party that starts at 10 pm.")
    print_slow("However, your parents have set an 11 pm curfew for you.")
    print_slow("You are torn between attending the social gathering with friends and respecting your parents' wishes.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Respect your parents' wishes and reluctantly reject your friends, abiding by the curfew and missing the party.")
    print(spaces + "B) Sneak out without telling your parents, risking severe consequences if you get caught.")
    print(spaces + "C) Attempt to discuss with your parents about making an exception this time, such as attending for a limited time under their supervision.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 10, "b": 5, "c": 20}
    ans=ans.lower()
    PlayerObj.c5 += new_dict[ans.lower()]
    if ans == "c":
        print_slow("Congratulations! You decided to have an open discussion with your parents.")
        print_slow("You attempted to make an exception by proposing to attend for a limited time under their supervision.")
        print_slow("This approach might lead to understanding and compromise.")
    elif ans == "b":
        print_slow("You decided to sneak out without telling your parents.")
        print_slow("While it may give you the chance to attend the party, remember that it also carries the risk of severe consequences if caught.")
    else:
        print_slow("You decided to respect your parents' wishes and reluctantly reject your friends.")
        print_slow("You chose to abide by the curfew, but it also means you'll miss out on the social gathering with friends.")
    print_slow("A few of your female friends are going together to get piercings and have invited you to join them.")
    print_slow("You are torn between joining your friends and worrying about explaining to your parents afterward, or explaining cultural restrictions and risking being chided.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Join your friends in getting piercings and worry about explaining to your parents afterwards.")
    print(spaces + "B) Explain to your friends that you cannot get piercings due to cultural restrictions and risk being chided.")
    print(spaces + "C) Attempt to seek your parents' approval in getting piercings.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))
    new_dict = {"a": 15, "b": 10, "c": 15}
    ans=ans.lower()
    PlayerObj.c5 += new_dict[ans.lower()]
    if ans == "c":
        print_slow("You decided to attempt seeking your parents' approval in getting piercings.")
        print_slow("By having an open conversation with them, you hope to find a way to respect your cultural restrictions while expressing your desires.")
    elif ans == "a":
        print_slow("You decided to join your friends in getting piercings.")
        print_slow("While you enjoyed the experience with your friends, remember that you'll need to address your parents' concerns later.")
    else:
        print_slow("You decided to explain to your friends about your cultural restrictions.")
        print_slow("Although you risk being chided, your true friends will understand and respect your decision.")
    print_slow("A boy confesses to you at school and asks if you would like to be in a relationship with him.")
    print_slow("You are torn between expressing your positive feelings towards the boy and agreeing to enter a relationship, rejecting the boy for now as you believe your parents should decide on your marriage partner, or engaging in a proper discussion with your parents about having the autonomy to decide on your own love life.")
    print_slow("What do you wish to do?")
    spaces = "            "
    os.system('cls')
    print('\n\n\n\n\n\n\n\n')
    print(spaces + "A) Express your positive feelings towards the boy and agree to enter a relationship.")
    print(spaces + "B) Reject the boy for now as you believe your parents should decide on your marriage partner.")
    print(spaces + "C) Engage in a proper discussion with your parents about whether you can be given the autonomy to decide on your own love life.")
    ans = str(input("What do you choose? (Please enter your answer as A, B, or C)"))

    new_dict = {"a": 10, "b": 15, "c": 20}
    ans=ans.lower()
    PlayerObj.c5 += new_dict[ans.lower()]
    if ans == "c":
        print_slow("Congratulations! You decided to have a proper discussion with your parents.")
        print_slow("By expressing your desire for autonomy in your love life, you hope to find understanding and support.")
    elif ans == "a":
        print_slow("You decided to express your positive feelings towards the boy and agree to enter a relationship.")
        print_slow("Enjoying the bliss of new romance, remember to consider your family's expectations and cultural values.")
    else:
        print_slow("You decided to reject the boy for now as you believe your parents should decide on your marriage partner.")
        print_slow("While it's essential to respect your family's wishes, keep in mind that open communication may help in finding common ground.")
    endgame()

def endgame():
    ending = ""

    # Graduate as a doctor/lawyer (60-100) vs. dropping out, not graduating (0-59)
    if 60 <= PlayerObj.c1 <= 100:
        ending += "YOU DID IT! YOU BECAME ONE OF THE BEST LAWYERS IN THE COUNTRY. "
    else:
        ending += "You did not manage to graduate, and your dreams were shattered. "

    # No friend/ lonely, parents happy (0-50) vs. have friends and parents are not happy (51-79) vs. have friends/ happy parents (80-100)
    if PlayerObj.c2 <= 50:
        ending += "You felt lonely without any friends, but your parents were happy with your life choices. "
    elif 51 <= PlayerObj.c2 <= 79:
        ending += "You had friends and found happiness in your own way, but your parents weren't fully supportive of your decisions. "
    else:
        ending += "You had wonderful friends and supportive parents, making your life fulfilling and joyous. "

    # Get a job (0-50) vs. no job (51-100)
    if PlayerObj.c3 <= 50:
        ending += "You struggled to find a job, and it became a source of stress in your life. "
    else:
        ending += "You were unable to secure a job, leaving you facing financial challenges. "

    # Get an arranged marriage parents happy (0-69) vs. marriage (run away), not happy parents (70-89) vs. married but parents happy (90-100)
    if PlayerObj.c4 <= 69:
        ending += "You reluctantly entered an arranged marriage to make your parents happy, but it wasn't what you truly desired. "
    elif 70 <= PlayerObj.c4 <= 89:
        ending += "You decided to run away and marry the person you loved, causing tension with your parents. "
    else:
        ending += "You managed to marry the person you loved, and your parents were happy with your choice. "

    # Get disowned (being kicked off from home) → not reconciled with parents (0-59) vs. run away (with my savings) (60-84) vs. happy ever after (everything satisfied) (85-100)
    if PlayerObj.c5 <= 59:
        ending += "You were disowned and couldn't reconcile with your parents, leaving you with a heavy heart. "
    elif 60 <= PlayerObj.c5 <= 84:
        ending += "You decided to run away with your savings, seeking a life of freedom and independence. "
    else:
        ending += "You managed to find happiness and reconciliation with your family, leading to a happy-ever-after ending. "

    # Print the final ending
    print_slow(ending)


main()