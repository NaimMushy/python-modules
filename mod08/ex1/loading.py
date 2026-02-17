import importlib
import sys
import random


def check_deps() -> bool:

    missing: list[str] = []
    deps: dict[str, str] = {
        "pandas": "Data manipulation",
        "requests": "Network access",
        "matplotlib": "Visualisation"
    }

    print("Checking dependencies...")
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

    if missing:
        if sys.prefix == sys.base_prefix:
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

    with open("requirements.txt", "w") as req:
        req.write("")

    return True


def analyse_data(data: dict) -> None:

    import numpy
    import matplotlib.pyplot as plt
    import pandas as pd

    print("\nAnalyzing Matrix data...")

    matrix = pd.DataFrame(data)

    print("Processing 1000 data points...")
    print("Generating visualisation...")

    for x, y in matrix.to_numpy():
        xpoints = numpy.array([0, x])
        ypoints = numpy.array([y, y])
        plt.plot(ypoints, xpoints)

    print("\nAnalysis complete!")

    plt.savefig("matrix_analysis.png")

    print("Results saved to: matrix_analysis.png")


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")

    if not check_deps():
        return None

    data: dict = {
        "xpoints": [random.randint(0, 100) for _ in range(1000)],
        "ypoints": [i for i in range(1000)]
    }

    analyse_data(data)


if __name__ == "__main__":
    main()
