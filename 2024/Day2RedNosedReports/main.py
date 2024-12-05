def main():
    with open("input.txt", "r") as file:
        total_safe = 0
        total_unsafe = 0
        for line in file:
            report_line = line.strip().split(" ")

            safe_popped_line = False
            for i in range(0, len(report_line)):
                working_line = report_line[:]
                working_line.pop(i)

                unsafe_count = 0
                desc_count = 0
                asc_count = 0
                for i in range(0, len(working_line) - 1):
                    diff = int(working_line[i]) - int(working_line[i + 1])

                    if abs(diff) > 3 or abs(diff) < 1:
                        unsafe_count += 1
                        break

                    if diff > 0:
                        desc_count += 1
                    elif diff < 0:
                        asc_count += 1

                unsafe_count += min(desc_count, asc_count)

                if unsafe_count == 0:
                    total_safe += 1
                    safe_popped_line = True
                    break

            if not safe_popped_line:
                total_unsafe += 1

        print(f"Total Safe: {total_safe}")
        print(f"Total Unsafe: {total_unsafe}")


if __name__ == "__main__":
    main()
