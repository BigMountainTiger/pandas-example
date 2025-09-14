from datetime import date, datetime, timedelta

args = {
    'start_date': '2025-09-13',
    'end_date': '2025-09-14'
}

iso_date_fmt = '%Y-%m-%d'

def get_date_range():
    start_date = args.get('start_date')
    end_date = args.get('end_date')

    if sum([1 if v is not None else 0 for v in [start_date, end_date]]) == 1:
        raise Exception('You must provide both the start_date and the end_date or neither')

    yesterday = date.today() - timedelta(days=1)
    start_date = datetime.strptime(start_date, iso_date_fmt).date() if start_date is not None else yesterday
    end_date = datetime.strptime(end_date, iso_date_fmt).date() if end_date is not None else yesterday

    if start_date > end_date:
        raise Exception('You provided a start_date later than the end_date?')

    return start_date, end_date

def main():
    start_date, end_date = get_date_range()
    
    the_day = start_date
    while the_day <= end_date:
        the_day_str = the_day.strftime(iso_date_fmt)
        print(f'Processing {the_day_str}')

        the_day = the_day + timedelta(days=1)

if __name__ == '__main__':
    main()