import pandas as pd


def get_devc_line(idx, series):
    line = (f"&DEVC ID='H_F TREE_{idx}', XB={series.X_m}, {series.X_m}, {series.Y_m}, {series.Y_m}, 0, 50,"
            f" QUANTITY='FIRE DEPTH' /")
    return line


def main():
    for case in ["fia"]:
        dataframe = pd.read_csv(f"{case}_trees.csv")
        # focus on 100x100 in center
        dataframe = dataframe[(dataframe.X_m>50)&(dataframe.X_m<150)&(dataframe.Y_m>50)&(dataframe.Y_m<150)]
        devc_lines = []
        for index, row in dataframe.iterrows():
            devc_line = get_devc_line(index, row)
            devc_lines.append(devc_line)
        with open(f"{case}_devc_lines.txt", "w") as f:
            f.write("\n".join(devc_lines))


if __name__ == "__main__":
    main()
