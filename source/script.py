import sys
from collections import OrderedDict
from .data import dimensions
from .utils import generate_combinations, question_format


def main():
    results = OrderedDict()
    questions = generate_combinations(dimensions)

    for i, q in enumerate(questions):
        while True:
            sys.stdout.write("-" * 80)
            sys.stdout.write("\n")
            sys.stdout.write("Question No #{} - Please select an answer (A/B):\n".format(i + 1))
            sys.stdout.write(question_format.format(id='A', question=q[0][1]))
            sys.stdout.write(question_format.format(id='B', question=q[1][1]))
            sys.stdout.write("\n")
            choice = input().upper()
            if choice in ('A', 'B'):
                selected = q[0] if choice == 'A' else q[1]
                sys.stdout.write("You choose '{}' \n".format(selected[1]))
                results.setdefault(selected[0], []).append(selected[1])
                break
            else:
                sys.stdout.write("Please respond with 'A' or 'B' \n")
    json_results = {k: len(results[k]) for k in results.keys()}

    sys.stdout.write("Your results are: \n")
    # print(results)
    print(json_results)


if __name__ == "__main__":
    main()
