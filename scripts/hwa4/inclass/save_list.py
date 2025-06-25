import numpy as np
import json
import pickle


def save_list(the_list: list, file_path: str, format: str):
    arr = np.array(the_list)

    match format:
        case "json":
            with open(file_path, "w") as fh:
                json.dump(the_list, fh)
        case "csv":
            np.savetxt(file_path, arr, delimiter=",")

        case "pickle":
            with open(file_path, "wb") as fh:
                pickle.dump(arr, fh)
        case _:
            raise ValueError(f"{format} is not supported")
