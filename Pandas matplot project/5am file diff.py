import pandas as pd
import matplotlib.pyplot as plt
COL_CAT = 'Crime_Category'
COL_HEAD = 'Major_Heads'
COL_YTD = 'Cases_during _current_year_upto_July_2025'
COL_JULY24 = 'Cases_during_July_2024'
COL_JUNE25 = 'Cases_during_June_2025'
COL_JULY25 = 'Cases_during_July_2025'
def load_data():
    df = pd.read_csv('finalmod.csv')
    return df
def show_columns(df):
    print("\n--- TABLE COLUMNS ---")
    sr_no = 1
    for i in df.columns:
        print(sr_no, ".", i)
        sr_no += 1
def show_crime_categories(df):
    cats = df[COL_CAT].unique()
    print("\nAvailable Categories:")
    for i in range(len(cats)):
        print(i+1,end='')
        print(")",cats[i])
    sel = input("\nEnter category number to view major heads (or press Enter to return): ").strip()
    if sel:
        try:
            sel_i = int(sel)
            if 1 <= sel_i <= len(cats):
                chosen_cat = cats[sel_i - 1]
                majors = df[df[COL_CAT] == chosen_cat][COL_HEAD].unique()
                print("\nMajor Heads in", chosen_cat)
                for j in range(len(majors)):
                    print(j+1,'.',majors[j])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input, please enter a number.")
def search_crime(df):
    print("\n--- SEARCH CRIME DATABASE ---")
    query = input("Enter crime name to search (e.g., Theft, Murder): ").strip().lower()
    result = df[df[COL_HEAD].str.lower().str.contains(query)]
    if not result.empty:
        print("\nFound", len(result), "matching records:")
        print("-" * 60)
        for index, row in result.iterrows():
            print("Category:", row[COL_CAT])
            print("Crime:    ", row[COL_HEAD])
            print(" > Total Cases during current year up to July 2025:", row[COL_YTD])
            print(" > Cases in July 2025:    ", row[COL_JULY25])
            print(" > Cases in June 2025:    ", row[COL_JUNE25])
            print(" > Cases in July 2024:    ", row[COL_JULY24])
            print("-" * 60)
    else:
        print("No matching crimes found.")
def data_analysis(df):
    print("\n" + "="*50)
    print("      ADVANCED DATA ANALYSIS MENU      ")
    print("="*50)
    print("1. General Summary (Total, Avg, Max)")
    print("2. Month-on-Month Comparison (June '25 vs July '25)")
    print("3. Year-on-Year Comparison (July '24 vs July '25)")
    print("4. Show Top 10 Crimes (Highest Cases)")
    print("5. ALERT: Top 10 Crimes with Highest Increase (Growth)")
    print("6. Return to Main Menu")
    choice = input("\nEnter your choice (1-6): ")
    if choice == '1':
        print("\n--- GENERAL SUMMARY ---")
        print("Total Cases (2025 YTD):", int(df[COL_YTD].sum()))
        print("Average Cases per Head:", round(df[COL_YTD].mean(), 2))
        print("Max Cases in Single Head:", int(df[COL_YTD].max()))       
        sorted_df = df.sort_values(by=COL_YTD, ascending=False)
        max_row = sorted_df.iloc[0]        
        print("Highest Crime Record:", max_row[COL_HEAD], "(", max_row[COL_YTD], "cases )")
        print("Crime Category:", max_row[COL_CAT])
        data_analysis(df)       
    elif choice == '2':
        print("\n--- MONTHLY COMPARISON ---")
        diff = df[COL_JULY25].sum() - df[COL_JUNE25].sum()
        print("Total Cases June '25:", int(df[COL_JUNE25].sum()))
        print("Total Cases July '25:", int(df[COL_JULY25].sum()))
        if diff > 0:
            print("Observation: Crime has INCREASED by", int(diff), "cases.")
        else:
            print("Observation: Crime has DECREASED by", abs(int(diff)), "cases.")
        data_analysis(df)        
    elif choice == '3':
        print("\n--- YEARLY COMPARISON ---")
        diff = df[COL_JULY25].sum() - df[COL_JULY24].sum()
        print("Total Cases July '24:", int(df[COL_JULY24].sum()))
        print("Total Cases July '25:", int(df[COL_JULY25].sum()))        
        if diff > 0:
            print("Observation: Crime has INCREASED by", int(diff), "cases.")
        else:
            print("Observation: Crime has DECREASED by", abs(int(diff)), "cases.")
        data_analysis(df)        
    elif choice == '4':
        print("\n--- TOP 10 CRIMES (VOLUME) ---")
        top10 = df.groupby(COL_HEAD)[COL_YTD].sum().sort_values(ascending=False).head(10)
        rank = 1
        for name, count in top10.items():
            print(rank, ".", name, ":", int(count))
            rank += 1
        data_analysis(df)
    elif choice == '5':
        print("\n--- CRIME GROWTH ALERT (Highest Percentage Rise) ---")
        temp_df = df.copy()
        temp_df = temp_df[temp_df[COL_JULY24] > 0]
        temp_df['Growth_Pct'] = ((temp_df[COL_JULY25] - temp_df[COL_JULY24]) / temp_df[COL_JULY24]) * 100
        growth_df = temp_df.sort_values(by='Growth_Pct', ascending=False).head(10)
        print("Top 10 Crimes with Highest Percentage Rise (July '24 vs July '25):")
        print("-" * 70)        
        for index, row in growth_df.iterrows():
            if row['Growth_Pct'] > 0:
                print(" >", row[COL_HEAD])
                print("   Last Year:", int(row[COL_JULY24]), "| This Year:", int(row[COL_JULY25]))
                print("   GROWTH: +", round(row['Growth_Pct'], 2), "%")
                print("-" * 70)
        data_analysis(df)        
    elif choice == '6':
        return
    else:
        print("Invalid choice!")
        data_analysis(df)
def visualize_data(df):
    print("\n" + "="*50)
    print("      DATA VISUALIZATION MENU      ")
    print("="*50)   
    print("1. Bar Graph: Top 5 Major Crimes (2025)")
    print("2. Pie Chart: Crime Category Distribution")
    print("3. Bar Graph: Comparison between July 2024 and July 2025")
    print("4. Bar Graph: Specific Crime Analysis")
    print("5. Return to Main Menu")
    choice = input("\nEnter your choice (1-5): ")
    if choice == '1':
        top5 = df.groupby(COL_HEAD)[COL_YTD].sum().sort_values(ascending=False).head(5)
        plt.figure(figsize=(10, 6))
        bars = plt.bar(top5.index, top5.values, color='maroon', width=0.6)
        plt.xlabel("Major Crime Heads")
        plt.ylabel("Total Cases (2025)")
        plt.title("Top 5 Reported Crimes (Current Year)")
        for bar in bars:
            y = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, y + (max(top5.values) * 0.01), f"{int(y):,}",
            ha='center', va='bottom', fontsize=9)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        visualize_data(df)
    elif choice == '2':
        cat_data = df.groupby(COL_CAT)[COL_YTD].sum()
        plt.figure(figsize=(9, 9))
        plt.pie(cat_data.values, labels=cat_data.index, autopct='%1.1f%%', startangle=140)
        plt.title("Crime Distribution by Category")
        plt.show()
        visualize_data(df)
    elif choice == '3':
        total_24 = df[COL_JULY24].sum()
        total_25 = df[COL_JULY25].sum()
        plt.figure(figsize=(7, 6))
        bars = plt.bar(['July 2024', 'July 2025'], [total_24, total_25], color=['blue', 'orange'])
        plt.ylabel("Total Cases")
        plt.title("Comparison: Last Year vs This Year")
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom')
        plt.show()
        visualize_data(df)
    elif choice == '4':
        print("\n--- CRIME TREND ANALYSIS ---")
        print("Examples of crimes you can type: Murder, Theft, Robbery, Rioting, etc.")
        crime_name = input("Enter exact Major Head name to plot: ").strip()
        record = df[df[COL_HEAD].str.lower() == crime_name.lower()]
        if not record.empty:
            y_jun25 = record.iloc[0][COL_JUNE25]
            y_jul25 = record.iloc[0][COL_JULY25]
            x_labels = ['June 25', 'July 25']
            y_values = [y_jun25, y_jul25]
            plt.figure(figsize=(8, 6))
            bars = plt.bar(x_labels, y_values, color=['purple', 'orange'], width=0.5)
            plt.title("Recent Trend: " + str(crime_name))
            plt.ylabel("Cases Reported")
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, height, int(height), ha='center', va='bottom')
            plt.show()
        else:
            print("Crime not found! Check spelling.")
        visualize_data(df)
    elif choice == '5':
        return
    else:
        print("Invalid choice! Try again.")
        visualize_data(df)
def main_menu():
    df = load_data()
    while True:
        print("\n" + "="*40)
        print("   CRIME DATA ANALYSIS SYSTEM (CDAS)   ")
        print("="*40)
        print("1. Show Table Columns")
        print("2. Browse Crime Categories")
        print("3. Search for a Specific Crime") 
        print("4. Advanced Data Analysis")
        print("5. Data Visualization Dashboard")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ")
        if choice == '1':
            show_columns(df)
        elif choice == '2':
            show_crime_categories(df)
        elif choice == '3':
            search_crime(df)
        elif choice == '4':
            data_analysis(df)
        elif choice == '5':
            visualize_data(df)
        elif choice == '6':
            print("Exiting System...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main_menu()
