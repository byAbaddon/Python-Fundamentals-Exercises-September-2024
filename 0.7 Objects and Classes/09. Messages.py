users = {}
messages = []

while True:
    command = input()
    if command == "exit":
        break
    parts = command.split()

    if parts[0] == "register":
        username = parts[1]
        if username not in users:
            users[username] = []
    elif parts[1] == "send":
        sender_username = parts[0]
        recipient_username = parts[2]
        content = " ".join(parts[3:])

        if sender_username in users and recipient_username in users:
            messages.append((sender_username, recipient_username, content))

user1, user2 = input().split()

user1_messages = [msg for msg in messages if msg[0] == user1 and msg[1] == user2]
user2_messages = [msg for msg in messages if msg[0] == user2 and msg[1] == user1]

if not user1_messages and not user2_messages:
    print("No messages")
else:
    max_len = max(len(user1_messages), len(user2_messages))
    for i in range(max_len):
        if i < len(user1_messages):
            print(f"{user1}: {user1_messages[i][2]}")
        if i < len(user2_messages):
            print(f"{user2_messages[i][2]} :{user2}")


'''
register John
John send Harry harry_you_there?
register Harry
John send Harry harry?
register Donald
Harry send John yeah_sorry_was_out...
Harry send John wassup?
Donald send John Yo_John?
Donald send Jonh You_there?
John send Harry thank_god!!
John send Harry I_need_you!
exit
John Harry
'''
