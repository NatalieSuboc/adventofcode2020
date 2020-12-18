def count_passports(file):
    criteria = ["byr", "iyr", "pid", "eyr", "hgt", "ecl", "hcl"]
    valid = 0
    with open(file) as txt:
        passports = txt.read().split('\n\n')
        for p in passports:
            v = True
            for c in criteria:
                if c not in p:
                    v = False
                    break
            if v:
                valid += 1
    return valid
