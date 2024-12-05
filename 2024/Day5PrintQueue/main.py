def get_index(value, list):
    return [i for i, rule in enumerate(list) if value in rule]


def validate_rule(update, ordering_rules, rules_broken):
    local_rule_broken_count = 0
    rule_broken_count = rules_broken
    for i in range(0, len(update)):
        number = update[i]
        rule_indexes_containing_number = {number: get_index(number, ordering_rules)}
        for rule in rule_indexes_containing_number[number]:
            before, after = ordering_rules[rule].split(",")
            if number in before:
                if after in update[:i]:
                    local_rule_broken_count += 1
                    update.pop(update.index(after))
                    update.insert(i, after)
            elif number in after:
                if before in update[i:]:
                    local_rule_broken_count += 1
                    update.pop(update.index(before))
                    update.insert(i, before)
    if local_rule_broken_count > 0:
        return validate_rule(
            update, ordering_rules, rule_broken_count + local_rule_broken_count
        )
    else:
        return update, rule_broken_count


def main():
    with open("input.txt", "r") as file:
        ordering_rules = []
        print_updates = []
        correct_median_total = 0
        fixed_median_total = 0
        for line in file:
            if line.count("|") >= 1:
                ordering_rules.append(line.strip().replace("|", ","))
            elif line.count(",") >= 1:
                print_updates.append(line.strip().split(","))

        for update in print_updates:
            update, total_rule_broken_count = validate_rule(update, ordering_rules, 0)
            if total_rule_broken_count == 0:
                correct_median_total += int(update[len(update) // 2])
            else:
                fixed_median_total += int(update[len(update) // 2])
        print(f"Initially Correct Median Totals: {correct_median_total}")
        print(f"Fixed Median Totals: {fixed_median_total}")


if __name__ == "__main__":
    main()
