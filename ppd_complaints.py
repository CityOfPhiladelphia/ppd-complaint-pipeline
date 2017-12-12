import arrow

import petl
import click

complaints_headers = {
    'CAP Number': 'cap_number',
    'Date Received': 'date_received',
    'Dist Occurrence': 'dist_occurrence',
    'General CAP Classification': 'general_cap_classification',
    'Summary': 'summary'
}

disciplines_headers = {
    'CAP Number': 'cap_number',
    'PO INITIALS': 'po_initials',
    'PO RACE': 'po_race',
    'PO SEX': 'po_sex',
    'Allegations Investigated': 'allegations_investigated',
    'Investigative Findings': 'investigative_findings',
    'Disciplinary Findings': 'pbi_determination'
}

def convert_date(input_date):
    return arrow.get(input_date, 'M/D/YYYY').format('YYYY-MM-DDTHH:mm:ss') + 'Z'

@click.group()
def main():
    pass

@main.command()
@click.option('-f','--input-file', type=click.Path(exists=True))
def transform_complaints(input_file):
    # input_file None defaults to stdin
    (
        petl
        .fromcsv(source=input_file, encoding='Windows-1252')
        .rename(complaints_headers)
        .convert('date_received', convert_date)
        .tocsv(encoding='utf-8')
    )

@main.command()
@click.option('-f','--input-file', type=click.Path(exists=True))
def transform_disciplines(input_file):
    # input_file None defaults to stdin
    (
        petl
        .fromcsv(source=input_file, encoding='Windows-1252')
        .rename(disciplines_headers)
        .tocsv(encoding='utf-8')
    )

if __name__ == '__main__':
    main()
