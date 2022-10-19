OUTPUT_TEMPLATE = "./data/svg/total.svg.template"
DIGIT_TEMPLATE_PREFIX = "./data/svg/digits/"
DIGIT_TEMPLATE_SUFFIX = ".svg.template"
DIGIT_SCALE = 4
DIGIT_WIDTH = 6.5 * DIGIT_SCALE
DIGIT_HEIGHT = 9 * DIGIT_SCALE


def create_and_write_svg(path: str, total_downloads: int, dark_mode: bool = False):
    with open(path, "w") as f:
        f.write(generate_svg(total_downloads, dark_mode))


def generate_svg(total_downloads: int, dark_mode: bool) -> str:
    digits, digit_count = generate_and_count_digits(total_downloads)
    with open(OUTPUT_TEMPLATE) as file:
        return file.read()\
            .replace("${content}", digits)\
            .replace("${width}", str(digit_count * DIGIT_WIDTH))\
            .replace("${height}", str(DIGIT_HEIGHT))\
            .replace("${foreground-color}", "white" if dark_mode else "black")


def generate_and_count_digits(total_downloads: int) -> (str, int):
    digits = [int(d) for d in str(total_downloads)]

    result = ""
    for i, digit in enumerate(digits):
        result += load_digit_template(digit, i * DIGIT_WIDTH, 0)

    return result, len(digits)


def load_digit_template(digit: int, x: float, y: float) -> str:
    with open(f"{DIGIT_TEMPLATE_PREFIX}{digit}{DIGIT_TEMPLATE_SUFFIX}") as f:
        return f.read()\
            .replace("${x}", str(x))\
            .replace("${y}", str(y))\
            .replace("${scale}", str(DIGIT_SCALE))
