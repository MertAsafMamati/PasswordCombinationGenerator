import os
import itertools

char_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "a", "b", "c", "x", "y", "z", "X", "Y",
             "Z", "l", "_", "_", "!", "!", "X", "X", "X", "X", "X", "X", "T", "t", "R", "r"]
x = 0
while x <= 6:
    x += 1
    if x <= 5:
        word1 = input("Write something: ")
        if len(word1) > 2:
            char_list.extend(list(word1[2:]))
        else:
            char_list.extend(list(word1))
        word_combinations = list(itertools.product(*[(char.lower(), char.upper()) for char in word1]))
    else:
        file_path = f"C:/Users/{os.getlogin()}/Downloads/possible_passwords.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            word_length = len(word1)
            for length in range(6, 11):
                remaining_length = length - word_length
                if remaining_length >= 0:
                    combinations = itertools.product(char_list, repeat=remaining_length)
                    for comb in combinations:
                        for word in word_combinations:
                            combined = ''.join(word) + ''.join(comb)
                            file.write((combined + '\n'))
                    half_length = remaining_length // 2
                    front_combinations = itertools.product(char_list, repeat=half_length)
                    back_combinations = itertools.product(char_list, repeat=remaining_length - half_length)
                    for front in front_combinations:
                        for back in back_combinations:
                            for word in word_combinations:
                                combined = ''.join(front) + ''.join(word) + ''.join(back)
                                file.write((combined + '\n'))
                    for comb in combinations:
                        for word in word_combinations:
                            combined = ''.join(comb) + ''.join(word)
                            file.write((combined + '\n'))
                numeric_combinations = itertools.product("0123456789", repeat=8)
                for num_comb in numeric_combinations:
                    file.write(''.join(num_comb) + '\n')
                for num_comb in itertools.product("0123456789", repeat=2):
                    remaining_length = 8 - len(num_comb)
                    if remaining_length > 0:
                        char_combinations = itertools.product(char_list, repeat=remaining_length)
                        for comb in char_combinations:
                            combined = ''.join(num_comb) + ''.join(comb)
                            file.write((combined + '\n'))
            print("All combinations are saved in downloads.")
