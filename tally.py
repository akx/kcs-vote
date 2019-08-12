import argparse
import fractions
from collections import defaultdict, Counter
from tabulate import tabulate

ap = argparse.ArgumentParser()
ap.add_argument('file')
args = ap.parse_args()

votes = defaultdict(list)

with open(args.file) as infp:
	for line in infp:
		line = line.strip()
		if not line:
			continue
		name, num = line.split(None, 1)
		num = int(num)
		assert num <= 5
		frac = fractions.Fraction(1, num)
		votes[name.title()].append(frac)

table = [
	(
		name,
		float(sum(name_votes)),
		str(sum(name_votes)),
		', '.join([
			'%s: %d' % (vote, count)
			for (vote, count)
			in Counter('%d/%d' % (v.numerator, v.denominator) for v in name_votes).most_common()
		])
	)
	for name, name_votes
	in sorted(votes.items(), key=lambda p: sum(p[1]), reverse=True)
]
print(tabulate(table))