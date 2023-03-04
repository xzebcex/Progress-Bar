# Prograss bar

import random
import time


BAR = chr(9642)  # chr ▪▪▪▪▪▪


def main():
    # Simulate the Download process
    print('Progress bar')
    bytes_downloaded = 0
    download_size = 4096  # (!) Add input()
    while bytes_downloaded < download_size:
        # Download a random amount of byte
        bytes_downloaded += random.randint(0, 100)

        # Get the progress bar
        bar_str = get_progress_bar(bytes_downloaded, download_size)

        # print string to the screen
        print(bar_str, end='', flush=True)
        time.sleep(0.2)

        # print backspaces to move the text cursotr to the line start
        print('\b' * len(bar_str), end='', flush=True)


def get_progress_bar(progress, total, bar_width=40):
    progress_bar = ''  # The progress bar will be the string value
    progress_bar += '|'  # Create the left end of the progress bar

    # Makes sure that the amount of progress is betweeen 0 and total
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate num of bar
    num_of_bar = int((progress / total) * bar_width)

    progress_bar += BAR * num_of_bar  # Add the progress
    progress_bar += ' ' * (bar_width - num_of_bar)  # Add empty space
    progress_bar += ']'  # Add the right end of the progress bar

    # Calculat4e the percentage complete
    percentage_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percentage_complete) + '%'

    # Add the number
    progress_bar += ' ' + str(progress) + '/' + str(total)
    return progress_bar


if __name__ == '__main__':
    main()
