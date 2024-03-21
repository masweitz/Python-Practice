



def bin_len(strings: list[str]) -> dict[int, list[str]]:
    my_dict: dict[int, list[str]] = {}
    for word in strings:
        if len(word) in my_dict:
            my_dict[len(word)].append(word)
        else:
            my_dict[len(word)] = []
            my_dict[len(word)].append(word)
        
    print(my_dict)
    return my_dict

def main():
    bin_len({"na","id", "win", "gojo","satoru"})

if __name__ == '__main__':
    main()