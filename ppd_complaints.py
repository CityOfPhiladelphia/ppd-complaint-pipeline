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
    'Disciplinary Findings': 'disciplinary_findings'
}

complaintant_headers = {
    'CAP Number': 'cap_number',
    'COMPL_SEX': 'complaintant_sex',
    'COMPL_RACE': 'complaintant_race',
    'COMPL_AGE': 'complaintant_age',
    'COMPL_INIT': 'complaintant_initials'
}

def convert_date(input_date):
    return arrow.get(input_date, 'M/D/YYYY').format('YYYY-MM-DDTHH:mm:ss') + 'Z'

@click.group()
def main():
    pass

@main.command('transform-complaints')
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

@main.command('transform-disciplines')
@click.option('-f','--input-file', type=click.Path(exists=True))
def transform_disciplines(input_file):
    # input_file None defaults to stdin
    (
        petl
        .fromcsv(source=input_file, encoding='Windows-1252')
        .rename(disciplines_headers)
        .tocsv(encoding='utf-8')
    )

@main.command('transform-complaintants')
@click.option('-f','--input-file', type=click.Path(exists=True))
def transform_complaintants(input_file):
    # input_file None defaults to stdin
    (
        petl
        .fromcsv(source=input_file, encoding='Windows-1252')
        .rename(complaintant_headers)
        .tocsv(encoding='utf-8')
    )

if __name__ == '__main__':
    main()
