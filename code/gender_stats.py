def get_gender_breakdown():
    male = 0
    female = 0
    with open("./../data/all_current_genderize_result.csv", 'r', encoding="utf8") as f:
        for line in f:
            split_line = line.split(',')
            if float(split_line[-1].strip()) >= 0.99:
                gender = split_line[-2]
                if gender == "female":
                    female += 1
                else:
                    male += 1
    print("male: {0}, female: {1}".format(male, female))

def main():
    get_gender_breakdown()

main()