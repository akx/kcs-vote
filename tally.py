import argparse
import fractions
from collections import defaultdict, Counter
from tabulate import tabulate


def format_pos(position, primary_count):
    if primary_count:
        if position <= primary_count:
            return f"#{position}"
        return f"(#{position - primary_count})"
    return f"#{position}"


def format_table(votes, primary_count):
    table = [
        (
            format_pos(pos, primary_count),
            name,
            float(sum(name_votes)),
            str(sum(name_votes)),
            ", ".join(
                [
                    f"{vote}: {count}"
                    for (vote, count) in Counter(
                    f"{v.numerator}/{v.denominator}" for v in name_votes
                    ).most_common()
                ]
            ),
        )
        for pos, (name, name_votes) in enumerate(
            sorted(votes.items(), key=lambda p: sum(p[1]), reverse=True),
            1,
        )
    ]
    print(tabulate(table, headers=("Position", "Name", "Total", "Fraction", "Votes")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("-c", "--count", type=int, required=True)
    args = ap.parse_args()
    primary_count = args.count
    if primary_count < 1:
        raise ValueError("primary count must be >= 1")

    votes = defaultdict(list)

    with open(args.file) as infp:
        for line in infp:
            line = line.strip()
            if not line:
                continue
            name, num = line.split(None, 1)
            num = int(num)
            if not (1 <= num <= primary_count):
                raise ValueError(f"invalid line: {line}")
            frac = fractions.Fraction(1, num)
            votes[name.title()].append(frac)
    format_table(votes, primary_count=primary_count)


if __name__ == "__main__":
    main()
