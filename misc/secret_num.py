sec_num = -9999999

print(int(input("What is the secret number? "(sec_num))))

while sec_num != 123:
    print("""
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    print("Ha ha! You're stuck in my loop!")

if sec_num == 123:
    print("Well done, muggle! You are free now.")
