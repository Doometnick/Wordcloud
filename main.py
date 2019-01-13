import re
import sys
import codecs
import wordcloud
import matplotlib.pyplot as plt

# regex pattern for carriet return
RE_PATTERN = re.compile(r"\\r[']*")


def load_from_text_file(file):
    f = codecs.open(file, encoding="utf-8")
    text = " ".join([repr(line) for line in f])
    return text


def wordcloud_figure(text, save=False):
    """
    Shows or saves a wordcloud figure.
    :param save: If true, figure will be saved to working directory.
    """
    # Remove carriet returns to avoid showing them in the wordcloud
    text = re.sub(RE_PATTERN, "", text)

    wc = wordcloud.WordCloud().generate(text)

    plt.figure(figsize=(16/2, 9/2))
    plt.imshow(wc, interpolation="quadric")
    
    if save:
        plt.savefig("wordcloud.png")
    else:
        plt.show()


if __name__ == "__main__":

    """
    Use: python main.py <textfile> 
    """

    try:
        text_file = sys.argv[1]
        text = load_from_text_file(text_file)
    except IndexError:
        print("Use: python main.py <textfile>")
        sys.exit()
    except FileNotFoundError:
        print("File could not be found. Path specified correctly?")
        sys.exit()
    
    wordcloud_figure(text)
