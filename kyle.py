#!/usr/bin/env python

import pathlib
import click
import rarfile

def get_filenames(current_path):
    """Get a list of filenames from all the rar files in set of sub
    directories.
    """

    filenames = []
    for filename in current_path.glob("**/*.rar"):
        with rarfile.RarFile(str(filename)) as rf:
            for rar_filename in rf.namelist():
                filenames.append(filename.parent / rar_filename)
    return filenames


def clean_files(filenames, run=False):
    """Remove a list of files."""

    for filename in filenames:
        if filename.exists() is False:
            print(f"file not found: {filename}")
        else:
            print(f"removing {filename}")
            if run is True:
                if filename.is_dir():
                    filename.rmdir()
                else:
                    filename.unlink()


@click.command()
@click.option("-d", "--delete", is_flag=True, default=False,
              help="Run Delete (default is trialrun)")
def main(delete):

    current_path = pathlib.Path().absolute()
    filenames = get_filenames(current_path)
    clean_files(filenames, delete)

    if delete is not True:
        print()
        print("Test run only, to delete files use -d or --delete")


if __name__ == "__main__":
    main()

