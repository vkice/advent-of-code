def main():
    group_1 = []
    group_2 = []

    with open("input.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            group_1.append(int(parts[0]))
            group_2.append(int(parts[1]))

    group_1 = sorted(group_1, key=int)
    group_2 = sorted(group_2, key=int)

    paired_locations = zip(group_1, group_2)

    total_distance = 0
    for location in paired_locations:
        total_distance += abs(location[0] - location[1])

    print(f"Total distance between the two lists: {total_distance}")

    similarity_score = 0
    for i in group_1:
        similarity_score += i * group_2.count(i)

    print(f"Similarity score between the two lists: {similarity_score}")


if __name__ == "__main__":
    main()
