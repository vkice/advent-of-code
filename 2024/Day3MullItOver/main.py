import re


def main():
    with open("input.txt", "r") as file:
        split_matched_list = re.split(r"(do\(\)|don\'t\(\))", file.read())

    multiplied_total = 0
    proceed = True

    for entry in split_matched_list:
        if entry == "do()":
            proceed = True
        elif entry == "don't()":
            proceed = False
        else:
            if proceed:
                matched_list = re.findall(r"mul\(\d*,\d*\)", entry)
                for mul in matched_list:
                    val1, val2 = mul[4:-1].split(",")
                    multiplied_total += int(val1) * int(val2)

    print(multiplied_total)


if __name__ == "__main__":
    main()
