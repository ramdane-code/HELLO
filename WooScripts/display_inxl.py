"""
display_inxl.py

But: exporte n'importe quel dataset du package `wooldridge` vers Excel/CSV
et affiche le DataFrame dans le terminal. Nom générique et options CLI.

Objectif principal: écrire la totalité du DataFrame (toutes lignes/colonnes)
dans un fichier Excel sur le Bureau (sans lancer d'application).
"""

import argparse
import sys
import pandas as pd
from wooldridge import data
from pathlib import Path


def build_parser():
    p = argparse.ArgumentParser(description="Export Wooldridge dataset to Excel/CSV (full dataframe)")
    p.add_argument("--dataset", "-d", default="mroz", help="Name of the wooldridge dataset (e.g. mroz, recid)")
    p.add_argument("--max-rows", "-m", type=int, default=1000, help="Limit number of rows printed to terminal (default: 1000). Use 0 for no display.")
    p.add_argument("--no-export", action="store_true", help="Do not export files to disk")
    p.add_argument("--export-dir", default=str(Path.home() / "Desktop"), help="Directory to export files to (default: Desktop)")
    p.add_argument("--format", choices=["csv", "xlsx", "both"], default="xlsx", help="Export format: csv, xlsx or both (default: xlsx)")
    p.add_argument("--head", type=int, default=None, help="Show exactly the first N rows in terminal (overrides --max-rows)")
    p.add_argument("--index", action="store_true", help="Include DataFrame index in exported files")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    dataset_name = args.dataset
    max_rows = args.max_rows
    do_export = not args.no_export
    export_dir = Path(args.export_dir).expanduser()
    export_format = args.format
    head = args.head
    include_index = args.index

    # Load dataset
    try:
        df = data(dataset_name)
    except Exception as e:
        print(f"Error: cannot load dataset '{dataset_name}': {e}")
        print("Tip: vérifie le nom du dataset dans le package `wooldridge`.")
        sys.exit(1)

    # Terminal display control
    pd.set_option('display.max_columns', None)
    if head is not None:
        # show exactly first N rows
        if head == 0:
            print("(display suppressed by --head 0)")
        else:
            print(df.head(head))
    else:
        if max_rows == 0:
            print("(display suppressed by --max-rows 0)")
        else:
            if max_rows is None:
                pd.set_option('display.max_rows', None)
                print(df)
            else:
                pd.set_option('display.max_rows', max_rows)
                print(df.head(max_rows))

    # Always print info/describe summary
    print()
    print("--- info() ---")
    print(df.info())
    print()
    print("--- describe() ---")
    print(df.describe(include='all'))

    # Export full DataFrame to chosen dir
    if do_export:
        try:
            export_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Could not create export directory {export_dir}: {e}")
            do_export = False

    if do_export:
        # XLSX (full dataframe) - default
        if export_format in ("xlsx", "both"):
            xfile = export_dir / f"{dataset_name}.xlsx"
            try:
                df.to_excel(xfile, index=include_index, sheet_name=dataset_name, engine='openpyxl')
                print(f"✓ Excel exported (full dataframe): {xfile} (index={'yes' if include_index else 'no'})")
            except Exception as e:
                print(f"✗ Failed to export Excel ({xfile}): {e}")
        # CSV (full dataframe)
        if export_format in ("csv", "both"):
            cfile = export_dir / f"{dataset_name}.csv"
            try:
                df.to_csv(cfile, index=include_index)
                print(f"✓ CSV exported (full dataframe):   {cfile} (index={'yes' if include_index else 'no'})")
            except Exception as e:
                print(f"✗ Failed to export CSV ({cfile}): {e}")


if __name__ == '__main__':
    main()
