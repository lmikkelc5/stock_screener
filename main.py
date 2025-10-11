import screen
import pandas as pd
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

def main():
    #read in list 
    run_check = input('Do you want to check your list(Y or N): ')

    with open('data/cleaned_list.txt', 'r') as f:
        ticks = [line.strip() for line in f.readlines()]

    if run_check.upper() == 'Y':
        with open('data/cleaned_list.txt', 'w') as f:
            cleaned_list, invalid_list = screen.check_list(ticks)
            for sym in cleaned_list:
                f.write(sym + '\n')

        with open('data/invalid_list.txt', 'w') as f:
            for sym in invalid_list:
                f.write(sym + '\n')

    # if yes use clened_list if no use ticks
    if run_check.upper() == 'Y':
        lst = cleaned_list
    else:
        lst = ticks

    #create new df
    main_df = pd.DataFrame()

    for item in lst:
        new_row = screen.screener(item)
        main_df = pd.concat([main_df, new_row], ignore_index=True)

    print(main_df)
        
if __name__ == "__main__":
    main()
