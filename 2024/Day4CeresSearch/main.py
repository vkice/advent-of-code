from collections import defaultdict


def main():
    with open("input.txt", "r") as file:
        search_word = "MAS"
        search_word_reverse = search_word[::-1]
        x_mas_total = 0
        horizontal_lines = []
        vertical_positional = defaultdict(list)
        vertical_lines = []

        # Horizontal
        for line in file:
            horizontal_lines.append(line.strip())

        # Vertical
        for line in horizontal_lines:
            for i in range(len(line)):
                vertical_positional[i].append(line[i])
        for i in vertical_positional:
            vertical_positional[i] = "".join(vertical_positional[i])
            vertical_lines.append(vertical_positional[i])

        # Diagonal
        # Char
        for i in range(0, len(horizontal_lines), 3):
            # Line
            for j in range(0, len(vertical_lines), 3):
                # Grid line
                for k in range(0, 3):
                    k += i
                    # Grid char
                    for m in range(0, 3):
                        m += j
                        diagonal_right_count = 0
                        diagonal_left_count = 0
                        index_error_count = 0
                        try:
                            diagonal_right = (
                                horizontal_lines[k][m]
                                + horizontal_lines[k + 1][m + 1]
                                + horizontal_lines[k + 2][m + 2]
                            )
                            diagonal_right_count += diagonal_right.count(
                                search_word
                            ) + diagonal_right.count(search_word_reverse)
                            diagonal_left = (
                                horizontal_lines[k][m + 2]
                                + horizontal_lines[k + 1][m + 1]
                                + horizontal_lines[k + 2][m]
                            )
                            diagonal_left_count += diagonal_left.count(
                                search_word
                            ) + diagonal_left.count(search_word_reverse)
                        except IndexError:
                            index_error_count += 1
                        if (
                            index_error_count == 0
                            and (diagonal_right_count + diagonal_left_count) == 2
                        ):
                            print(
                                f"Found X-MAS: {diagonal_right} and {diagonal_left} through {k+1} and {m+1}"
                            )
                            x_mas_total += 1

        print(x_mas_total)


if __name__ == "__main__":
    main()
