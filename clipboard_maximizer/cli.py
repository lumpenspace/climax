import click
from clipboard_maximizer.clipboard_manager import copy_to_clipboard

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--clipboard', default=None, help='Specify the clipboard program')
def main(files, clipboard):
    copy_to_clipboard(files, clipboard)

if __name__ == '__main__':
    main()