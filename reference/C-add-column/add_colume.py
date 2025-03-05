import os
import datetime
import pandas as pd

file = './example_files/example_20220131.txt'

def run(file):

  def get_file_date():
    ds = (os.path.splitext(file)[0]).split('_')[-1]
    if len(ds) != 8:
      raise ValueError(f'The date on the file name {file} needs to be 8 digits')

    try:
      ymd = (ds[0:4], ds[4:6], ds[6:])
      dt = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]))
    except Exception as e:
      raise ValueError(f'The date on the file name {file} is not valid')

    return dt.strftime('%Y/%m/%d')

  file_date = get_file_date()

  # Load file & add a column, treat all the data as string
  df = pd.read_csv(file, sep='|', dtype=str)
  df['Load Date'] = file_date

  print(df.head())
  print(df.shape)

  # Save it - overwrite
  df.to_csv(file, sep='|', index=False)
  print('Saved')

  # Load the file back and check the new column added
  print('Loading back to df')
  df = pd.read_csv(file, sep='|')

  print(df.head())
  print(df.shape)

  # Try to filter the data frame
  print('Filtered df')
  df = df[df['Mailing Opt Out Indicator'].notnull()]
  print(df.head())
  print(df.shape)

if __name__ == '__main__':
  run(file)