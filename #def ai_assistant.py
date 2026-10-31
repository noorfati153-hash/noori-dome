#def ai_assistant 
#1.introduction
assistant_name="Zorbo"
print("="*60)
print(f"[{Zorbo}]"):hello!salam! im {zorbo},your AI buddy here to assist.")
print(f"[{Zorbo}]"):iam here to help you my dear pal with designing, brainstorming ,problem solving and giving the best advise or at least a good piece of advise.")
print("=" *60)
print()
#2.User identification
user_name=input("what is your name buddy?").stripe()
print(f"\n[{zorbo}]:what a sweet name nice to meet you dear,{user_name}!")
#3.Interactive menu
print(f"\n[{zorbo}]:whatsup dear old pal?")
print(f"\n[{zorbo}]:what would like to do today?")
print(" [1] solve a math problem")
print(" [2] Analyzise and generate a text(Word & character count)")
print("  [3] General problem solving plan")
print("[4] Code & Project design Blueprint")
choice = input(f"\n Enter your choice (1,2,3,or4):").strip()
print("\n"+ "-" * 60)
#4. Handle Choice1:Math solver
if choice =="1":
    print(f"[{zorbo}]: math mode on!")
    math_input=input("enter a mathematic problem(e.g.,20*25*2+2):")
    try:
        #Safely evaluate simple math expressions 
        result=eval(math_input)
        print(f"\n  [Solution]: {math_input}={result}")
        expect Expection:
              print(f"\n  [{zorbo}]: oops! couldn't calculate that.try again.")
#5.Handle Choice 2:TEXT analyzer
elif choice == "2":
    print(f"[{zorbo}]: text analysis mode activate!")
    text_input = input("type or paste ur text here:")
    word_count= len(text_input.split())
    char_count = len(text_input)
    print(f"\n [Text Analysis Report for {user_name}]:")
    print(f"  .Total Words:{word_count}")
    print(f"   .Total Characters(with spaces):{char_count}")
#6. Handle Choice 3: General problem Solver
elif choice =="3":
    print(f"[{zorbo}]: Analyzing'{problem}'...")
    problem = input("what s the matter?")
    print(f"\n[{zorbo}]:Analyizing '{problem}'...")
    time.sleep(1)#Simulate thinking
    print(f"\n[{zorbo} 's Custom Action Plan for{user_name}]:")
    print("Step1:identify the root cause of obstacle.")
    print("step2:Gather necessary resources , pros , experiences and break the task in small protion.")
    print(" Step3: Execute task , review result and evaluate probablity ofthe generated progress".)
    #7.Handle Choice 4:code &  project design mode
    elif choice == "4"
    print(f"[{zorbo}]:Code & Project Design Mode Activation!")
    project_idea=input("OH!splended which idea , application or project or systems you want to create.")
    print(f"\n[{Zorbo}]:Drafting architecture for'{project_idea}'...")
    time.sleep(1.5)#Simulate thinking
    print(f"\n[{Zorbo}'s System design blurprint for {user_name}]:")
    print(f"   .**Project Name**:{project_idea}")
print(f"  .**Phase1 : Requirments & Featurees** Define core inputs ,outputs and user flow.")
print(". **phase2 : File Structure**  Organize into modules/functions(e.g., 'main.py','utils.py'). ")
print(" .**phase3 : Data Management** Decide how data is stored(variables, lists,or databases).")
print(". **phase4: Minimum Viable Product (MVP)** Build the simplest working version first!")
#Handle Invalid Choices
else:
    print(f"\n [{ zorbo}]: impossible for a small ai like me but our team will be working sooner on my upgradation.")
    print("\n" + "=" * 60)
    print(f"[{zorbo}]:THANKS FOR CHITT CHATTING WITH ME, {user_name}! se you next time ,Goodbye!")
    # Run the program
    if--name--=="--main--":
        ai_assistant()
        

)
