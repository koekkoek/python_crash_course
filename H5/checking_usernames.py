current_users = ['admin', 'test', 'jan234', 'patetito', 'banana_eater']
new_users = ['test', 'pietje', 'yesplease']

# Tijdelijke lijst
users_tmp = current_users[:]
for i in range(5):
    users_tmp[i] = current_users[i].lower()

# users_temp = [user.lower() for user in current_users] --> dit had ook gekund

# Check if username is still available.
for user in new_users:
    if user.lower() in users_tmp:
        print(f"The username '{user}' is already taken. You will need to enter a new username.")
    else:
        print(f"This username ({user}) is still available.")