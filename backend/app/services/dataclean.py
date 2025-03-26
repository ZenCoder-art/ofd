from pathlib import Path

class DataClean:
    def __init__(self) -> None:
        pass

    def remove_missing(self, dataset):
        pass

    def duplicate(self, dataset):
        print(f"处理重复值前的数据集形状为:{dataset.shape}")
        dataset.data.drop_duplicates(keep="first", inplace=True)
        print(f"删除重复值后的数据集形状为:{dataset.shape}")


if __name__ == "__main__":
    pass
