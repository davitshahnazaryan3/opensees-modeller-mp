import json
import pickle
import numpy as np
from scipy import stats
from scipy.interpolate import interp1d
from pathlib import Path
import warnings


def append_record(x, y):
    """Record selection issue related to the database of records
    whereby the two pairs of the records have different sizes
    To remedy the issue, the smallest of the records is appended with zeros

    Parameters
    ----------
    x : List
    y : List

    Returns
    -------
    List List
    """
    nx = len(x)
    ny = len(y)

    if nx < ny:
        x = np.append(x, np.zeros(ny - nx))
    if ny < nx:
        y = np.append(y, np.zeros(nx - ny))
    return x, y


def create_path(directory: Path):
    """Create a folder if it does not exist

    Parameters
    ----------
    directory : Path
        Directory to be created
    """
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except OSError:
        print("Error: Creating directory. ", directory)


def find_nearest(array, value: float):
    """Find index of nearest value in array

    Parameters
    ----------
    array : List
    value : float

    Returns
    -------
    List[int]
        Index of nearest value
    """
    value = np.asarray(value)
    array = np.asarray(array)
    idx = np.abs(array - value[:, np.newaxis]).argmin(axis=1)
    return idx


def read_text(name, usecols=None) -> np.array:
    """Reads a text file

    Parameters
    ----------
    name : str
        Filename
    usecols : sequence, optional
        Which columns to read, with 0 being the first.  For example,
        ``usecols = (1, 4, 5)`` will extract the 2nd, 5th and 6th columns.
        by default, None

    Returns
    -------
    np.array
        Content of file
    """
    return np.genfromtxt(name, invalid_raise=False, usecols=usecols)


def remove_directory_contents(directory: Path):
    if not directory.exists():
        return

    for item in directory.glob("*"):
        if item.is_file():
            item.unlink()
        else:
            item.rmdir()

    directory.rmdir()


def to_json_serializable(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = to_json_serializable(value)
    elif isinstance(data, list):
        return [to_json_serializable(item) for item in data]
    elif isinstance(data, np.ndarray):
        return data.tolist()
    elif isinstance(data, np.float_):
        return float(data)
    elif isinstance(data, np.float32):
        return float(data)
    elif isinstance(data, np.int32):
        return float(data)
    return data


def export_results(filepath: Path, data, filetype: str):
    """Exports results to file

    Parameters
    ----------
    filepath : Path
        Path where to export data to
    data : any
        Data to be stored
    filetype : str
        Filetype, e.g. npy, json, pkl, csv
    """
    if filetype == "json":
        data = to_json_serializable(data)

    if filetype == "npy":
        np.save(f"{filepath}.npy", data)
    elif filetype == "pkl" or filetype == "pickle":
        with open(f"{filepath}.pickle", "wb") as handle:
            pickle.dump(data, handle)
    elif filetype == "json":
        with open(f"{filepath}.json", "w") as json_file:
            json.dump(data, json_file)
    elif filetype == "csv":
        data.to_csv(f"{filepath}.csv", index=False)


def read_pickle(path):
    with open(path, "rb") as file:
        data = pickle.load(file)
    return data


def read_txt(path):
    with open(path, "r") as file:
        lines = file.readlines()

    integers = []

    for line in lines:
        integers.extend(map(int, line.strip().split(",")))

    return integers


def mlefit(median: float, dispersion: float, total_count: int, count: int,
           data) -> float:
    """Maximum likelihood method
    Performs a lognormal cumulative distribution function fit to the data
    points based on maximum likelihood method

    Parameters
    ----------
    median : float
        Median of the function, parameter of a statistical model to be found
    dispersion : float
        Standard deviation of the function, parameter of a statistical model
        to be found
    total_count : int
        Number of data points
    count : int
        Number of failures
    data: Union[List, np.ndarray]
        The function, data points

    Returns
    -------
    float
        Negative Log likelihood to be minimized
    """
    warnings.filterwarnings("ignore", category=RuntimeWarning)

    try:
        p = stats.norm.cdf(np.log(data), loc=np.log(median), scale=dispersion)
        likelihood = stats.binom.pmf(count, total_count, p)
        likelihood[likelihood == 0] = 1e-290
        loglik = -sum(np.log10(likelihood))

        warnings.resetwarnings()

        return loglik
    except OverflowError:
        warnings.resetwarnings()

        return 1e+8


def spline(x, y, size: int = 1000) -> tuple[np.ndarray, np.ndarray]:
    """Performs a spline

    Parameters
    ----------
    x : list
    y : list
    size : int, optional
        Number of interpolation points, by default 1000

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Fitted x and y
    """

    x_range = range(len(x))
    points = np.linspace(0, x_range[-1], size * x_range[-1])
    xi = interp1d(x_range, x)(points)
    yi = interp1d(x_range, y)(points)

    return xi, yi


def is_list_of_lists(lst):
    if isinstance(lst, np.ndarray):
        if lst.ndim > 1:
            return True
        return False

    for item in lst:
        if isinstance(item, list) or isinstance(item, np.ndarray):
            return True
    return False


def cdf_lognormal_norm(xs, median: float, beta: float) -> np.ndarray:
    prob = stats.norm.cdf((np.log(xs / median)) / beta)
    return prob
