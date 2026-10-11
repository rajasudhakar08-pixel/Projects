topics = []
practice_times = []

with open("sessions.txt", "r") as file:
    for line in file:
        topic, minutes = line.strip().split(",")
        topics.append(topic)
        practice_times.append(int(minutes))

print("Loaded topics:", topics)
print("Loaded times:", practice_times)



while True:
    print('==============CODEQUEST===================')
    print('1. Add a coding session')
    print('2. View all sessions')
    print('3. View completed topics')
    print('4. Check total practice time')
    print('5. Exit')

    choice = input("Enter your choice: ")

    if choice == '1':
        topic = input('What topic did you practise?  ')
        topics.append(topic)
        minutes = int(input('How many minutes did you practise? '))
        practice_times.append(minutes)
        with open("sessions.txt", "a") as file:
            file.write(f"{topic},{minutes}\n")
    elif choice == '2':
        for i in range (len(practice_times)):
            print((i+1),' ==> You have leant the topic: ',topics[i])
            print((i+1),' ==> Your lesson was for:  ',practice_times[i],' minutes')
    elif choice == '3':
        print('Here are your completed topics')
    elif choice == '4':
        total = sum(practice_times)
        print("Total practice time:", total, "minutes")
    elif choice == '5':
        print('Goodbye! Thank you for using CodeQuest')
        break


print(topics)
print(practice_times)
