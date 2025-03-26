from pathlib import Path

import pandas as pd


class DataSet:
    def __init__(self, filename: str, filepath: Path = None) -> None:
        self._dataset = self.read_data(filename, filepath)

    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, val: pd.DataFrame):
        self._dataset = val

    def read_data(
        self,
        filename: str,
        filepath: Path = Path("../dataset/raw"),
    ):
        full_path = filepath / filename
        ext = full_path.suffix.lower()
        if ext == ".csv":
            return pd.read_csv(full_path)
        elif ext == ".json":
            return pd.read_json(full_path)
        elif ext in [".xls", ".xlsx"]:
            return pd.read_excel(full_path)
        elif ext == ".feather":
            return pd.read_feather(full_path)
        else:
            raise ValueError(f"不支持的文件后缀名:{ext}")

    def __repr__(self) -> str:
        return f"DataSet(shape={self.dataset.shape}, columns={self.dataset.columns.tolist()})"


if __name__ == "__main__":
    print(
        DataSet(
            filename="processed_data.feather",
            filepath=Path("../dataset/processed"),
        ).info()
    )
