import importlib
import sys
import random


def check_deps() -> bool:

    """
    Checking dependencies required to analyse the matrix data
    (pandas, requests, matplotlib)
    """

    missing: list[str] = []

    deps: dict[str, str] = {
        "pandas": "Data manipulation",
        "requests": "Network access",
        "matplotlib": "Visualisation"
    }

    print("Checking dependencies...")

    # trying to import modules and adding them to the missing list if failing

    for dep_name, dep_msg in deps.items():

        try:
            dep = importlib.import_module(dep_name)

        except ImportError:
            missing.append(dep_name)
            print(f"[MISSING] {dep_name}")

        else:
            print(
                f"[OK] {dep_name} ({dep.__version__}) "
                f"- {dep_msg} ready"
            )

    # clear instructions in case of missing dependencies

    if missing:

        # checking if the program is running inside a virtual environment

        if sys.prefix == sys.base_prefix:

            # writing the missing dependencies to the requirement file for pip

            with open("requirements.txt", "w") as req:

                for dep_name in missing:
                    req.write(f"{dep_name}\n")

            print(
                "\nInstall required modules with "
                "'pip install -r requirements.txt'\n"
            )

        else:

            print(
                "\nInstall required modules with "
                "'poetry install'\n"
            )

        return False

    # cleaning the requirement file in case no modules are missing

    with open("requirements.txt", "w") as req:

        req.write("")

    return True


def analyse_data(data: dict) -> None:

    """ Analyzing matrix data using the different modules imported """

    import numpy
    import matplotlib.pyplot as plt
    import pandas as pd

    print("\nAnalyzing Matrix data...")

    # using pandas to tranform the data provided into a data frame

    matrix = pd.DataFrame(data)

    print("Processing 1000 data points...")
    print("Generating visualisation...")

    for x, y in matrix.to_numpy():

        # using numpy to extract coordinates from the data frame

        xpoints = numpy.array([0, x])
        ypoints = numpy.array([y, y])

        # using matplotlib to generate a graphic representation

        plt.plot(ypoints, xpoints)

    print("\nAnalysis complete!")

    # saving the graphic to an image file

    plt.savefig("matrix_analysis.png")

    print("Results saved to: matrix_analysis.png")


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    if not check_deps():
        return None

    # generating a random simulated matrix to analyze

    data: dict = {
        "xpoints": [random.randint(0, 100) for _ in range(1000)],
        "ypoints": [i for i in range(1000)]
    }

    analyse_data(data)


if __name__ == "__main__":
    main()
