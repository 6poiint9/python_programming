
operating_systems = ("windows", "gnu/linux", "macos", "openbsd", "freebsd")

for i, os in enumerate(operating_systems, start=69):
    print(f'{i}. {os}')

languages = ("Python", "C++", "Rust", "Go", "JavaScript")

for i, lang in enumerate(languages, start=1):
    print(f'{i}: {lang}') 

try: 
    choose = int(input("What language do you like the most? Enter the number: "))

    if choose >= 1 and choose <= len(languages) :
        print(f'You chose {languages[choose-1]}!')
    else:
        print("Invalid choice")

except ValueError:
    print("invalid input (NAN)")

