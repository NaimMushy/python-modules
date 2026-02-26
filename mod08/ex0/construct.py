import sys
import site


def main() -> None:

    """
    Comparing sys.prefix
    which refers to the virtual environment prefix (if running inside one)
    and sys.base_prefix which always refers to the base Python installation
    """

    matrix: dict = {}

    if sys.prefix == sys.base_prefix:

        """
        Displaying the instructions
        to create and activate a virtual environment
        """

        matrix = {
            "\nMATRIX STATUS": "You're still plugged in\n",
            "Current Python": sys.executable,
            "Virtual Environment": "None detected",
            "\nWARNING": (
                "You're in the global environment!\n"
                "The machines can see everything you install\n"
            ),
            "To enter the construct, run": (
                "python -m venv matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\n"
                "Scripts\n"
                "activate   # On Windows\n"
                "\nThen run this program again"
            )
        }

    else:

        """
        Displaying the current virtual environment's information:
        name, path, user base, global/local packages
        """

        matrix = {
            "\nMATRIX STATUS": "Welcome to the construct\n",
            "Current Python": sys.executable,
            "Virtual Environment": sys.prefix.split("/")[-1],
            "Environment Path": sys.prefix,
            "\nSUCCESS": (
                "You're in an isolated environment!\n"
                "Safe to install packages without "
                "affecting the global system\n"
            ),
            "Package installation path": f"\n{site.getsitepackages()[0]}"
        }

    for line_start, line_content in matrix.items():
        print(f"{line_start}: {line_content}")


if __name__ == "__main__":
    main()
