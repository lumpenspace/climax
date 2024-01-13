import click
from clipboard_maximizer.clipboard_manager import copy_to_clipboard
import os

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--clipboard', default=None, help='Specify the clipboard program')
def main(files, clipboard):
    # add the getcwd() to the files
    files = [os.path.join(os.getcwd(), file) for file in files]
    copy_to_clipboard(files, clipboard)

if __name__ == '__main__':
    main()